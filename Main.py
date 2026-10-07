import csv
import sys
from decimal import Decimal

def load_payments(path):
    payments = {}
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            ref = row["ref"]
            amount = Decimal(row["amount"])
            if ref not in payments:
                payments[ref] = []
            payments[ref].append(amount)
    return payments

ours_path = sys.argv[1] if len(sys.argv) > 1 else "ours.csv"
theirs_path = sys.argv[2] if len(sys.argv) > 2 else "theirs.csv"

ours = load_payments(ours_path)
theirs = load_payments(theirs_path)

matched = []
missing_from_theirs = []
missing_from_ours = []

for ref in ours:
    if ref in theirs:
        matched.append(ref)
    else:
        missing_from_theirs.append(ref)

for ref in theirs:
    if ref not in ours:
        missing_from_ours.append(ref)

sections = [
    ("MATCHED", matched),
    ("MISSING FROM THEIRS", missing_from_theirs),
    ("MISSING FROM OURS", missing_from_ours),]

for title, refs in sections:
    print(f"{title} ({len(refs)})")
    for ref in refs:
        amounts = ours[ref] if ref in ours else theirs[ref]
        shown = " ".join(f"${amount}" for amount in amounts)
        print(f"  {ref} {shown}")