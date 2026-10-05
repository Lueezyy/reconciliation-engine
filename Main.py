import csv

def load_payments(path):
    payments = []
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            payment = {"ref": row["ref"], "amount": int(row["amount"])}
            payments.append(payment)
    return payments

ours = load_payments("ours.csv")
theirs = load_payments("theirs.csv")

print(f"Ours: {ours}")
print(f"Theirs: {theirs}")

our_refs = [payment["ref"] for payment in ours]
their_refs = [payment["ref"] for payment in theirs]

matched = []
missing_from_theirs = []
missing_from_ours = []

for payment in ours:
    if payment["ref"] in their_refs:
        matched.append(payment)
    else:
        missing_from_theirs.append(payment)

for payment in theirs:
    if payment["ref"] not in our_refs:
        missing_from_ours.append(payment)

sections = [
    ("MATCHED", matched),
    ("MISSING FROM THEIRS", missing_from_theirs),
    ("MISSING FROM OURS", missing_from_ours),]

for title, payments in sections:
    print(f"{title} ({len(payments)})")
    for payment in payments:
        print(f"  {payment['ref']} ${payment['amount']}")