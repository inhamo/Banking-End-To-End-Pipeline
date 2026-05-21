from decimal import Decimal
import unittest

from banking_pipeline import run_end_to_end_pipeline


class BankingPipelineTests(unittest.TestCase):
    def test_pipeline_processes_credits_and_debits(self) -> None:
        output = run_end_to_end_pipeline(
            raw_transactions=[
                {"account_id": "A1", "amount": "300.50", "transaction_type": "credit"},
                {"account_id": "A1", "amount": "100.25", "transaction_type": "debit"},
            ],
            opening_balances={"A1": "200"},
        )

        self.assertEqual(output.balances["A1"], Decimal("400.25"))
        self.assertEqual(output.processed_transactions, 2)
        self.assertEqual(output.rejected_records, [])

    def test_pipeline_rejects_invalid_or_insufficient_records(self) -> None:
        output = run_end_to_end_pipeline(
            raw_transactions=[
                {"account_id": "A1", "amount": "x", "transaction_type": "credit"},
                {"account_id": "A1", "amount": "-10", "transaction_type": "debit"},
                {"account_id": "A1", "amount": "1000", "transaction_type": "debit"},
                {"account_id": "", "amount": "10", "transaction_type": "credit"},
            ],
            opening_balances={"A1": "100"},
        )

        reasons = [item["reason"] for item in output.rejected_records]
        self.assertEqual(
            reasons,
            ["invalid_amount", "non_positive_amount", "insufficient_funds", "invalid_record"],
        )
        self.assertEqual(output.processed_transactions, 0)

    def test_pipeline_flags_large_transactions(self) -> None:
        output = run_end_to_end_pipeline(
            raw_transactions=[
                {"account_id": "A1", "amount": "9999", "transaction_type": "credit"},
                {"account_id": "A1", "amount": "10000", "transaction_type": "credit"},
            ],
            opening_balances={"A1": "0"},
        )

        self.assertEqual(len(output.flagged_transactions), 1)
        self.assertEqual(output.flagged_transactions[0].amount, Decimal("10000"))


if __name__ == "__main__":
    unittest.main()
