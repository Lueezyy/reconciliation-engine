import csv
import sys
from decimal import Decimal

def load_payments(path):
    payments = {}
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            payment = {"ref": row["ref"], "amount": Decimal(row["amount"])}
            payments[payment["ref"]] = payment
    return payments

ours_path = sys.argv[1] if len(sys.argv) > 1 else "ours.csv"
theirs_path = sys.argv[2] if len(sys.argv) > 2 else "theirs.csv"

ours = load_payments(ours_path)
theirs = load_payments(theirs_path)

matched = []
missing_from_theirs = []
missing_from_ours = []

for ref, payment in ours.items():
    if ref in theirs:
        matched.append(payment)
    else:
        missing_from_theirs.append(payment)

for ref, payment in theirs.items():
    if ref not in ours:
        missing_from_ours.append(payment)

sections = [
    ("MATCHED", matched),
    ("MISSING FROM THEIRS", missing_from_theirs),
    ("MISSING FROM OURS", missing_from_ours),]

for title, payments in sections:
    print(f"{title} ({len(payments)})")
    for payment in payments:
        print(f"  {payment['ref']} ${payment['amount']:.2f}")