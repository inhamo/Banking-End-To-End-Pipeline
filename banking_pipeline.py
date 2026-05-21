from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Any


@dataclass(frozen=True)
class Transaction:
    account_id: str
    amount: Decimal
    transaction_type: str


@dataclass(frozen=True)
class PipelineOutput:
    balances: dict[str, Decimal]
    flagged_transactions: list[Transaction]
    rejected_records: list[dict[str, Any]]
    processed_transactions: int


def _to_decimal(value: Any) -> Decimal:
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def run_end_to_end_pipeline(
    raw_transactions: list[dict[str, Any]],
    opening_balances: dict[str, Any],
    alert_threshold: Decimal = Decimal("10000"),
) -> PipelineOutput:
    balances = {account_id: _to_decimal(amount) for account_id, amount in opening_balances.items()}
    flagged_transactions: list[Transaction] = []
    rejected_records: list[dict[str, Any]] = []
    processed_transactions = 0

    for record in raw_transactions:
        account_id = record.get("account_id")
        amount_raw = record.get("amount")
        transaction_type = str(record.get("transaction_type", "")).lower()

        if not account_id or transaction_type not in {"credit", "debit"}:
            rejected_records.append({"record": record, "reason": "invalid_record"})
            continue

        try:
            amount = _to_decimal(amount_raw)
        except (InvalidOperation, ValueError, TypeError):
            rejected_records.append({"record": record, "reason": "invalid_amount"})
            continue

        if amount <= 0:
            rejected_records.append({"record": record, "reason": "non_positive_amount"})
            continue

        balances.setdefault(account_id, Decimal("0"))

        if transaction_type == "debit":
            if balances[account_id] < amount:
                rejected_records.append({"record": record, "reason": "insufficient_funds"})
                continue
            balances[account_id] -= amount
        else:
            balances[account_id] += amount

        transaction = Transaction(account_id=account_id, amount=amount, transaction_type=transaction_type)
        if amount >= alert_threshold:
            flagged_transactions.append(transaction)
        processed_transactions += 1

    return PipelineOutput(
        balances=balances,
        flagged_transactions=flagged_transactions,
        rejected_records=rejected_records,
        processed_transactions=processed_transactions,
    )
