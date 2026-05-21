# Banking-End-To-End-Pipeline

Minimal end-to-end banking transaction pipeline implementation.

## What it does

`run_end_to_end_pipeline` processes raw transaction records and returns:
- updated account balances
- suspicious high-value transactions
- rejected records with reasons
- count of processed transactions

## Run tests

```bash
python -m unittest discover -s tests -v
```
