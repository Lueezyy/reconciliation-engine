ours = [{"ref": "PAY001", "amount": 50},
    {"ref": "PAY002", "amount": 75},
    {"ref": "PAY003", "amount": 120},]
theirs = [{"ref": "PAY001", "amount": 50},
    {"ref": "PAY003", "amount": 120},
    {"ref": "PAY004", "amount": 30},]

print("Ours:", ours)
print("Theirs:", theirs)

our_refs = [payment["ref"] for payment in ours]
their_refs = [payment["ref"] for payment in theirs]

for payment in ours:
    ref = payment["ref"]
    amount = payment["amount"]
    print("Checking", ref)
    if ref in their_refs:
        print(f"{ref} (${amount}): matched")
    else:
        print(f"{ref} (${amount}): missing from theirs")

for payment in theirs:
    ref = payment["ref"]
    amount = payment["amount"]
    if ref not in our_refs:
        print(f"{ref} (${amount}): missing from ours")