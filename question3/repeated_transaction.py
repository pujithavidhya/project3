
# Repeated Transaction Detection

transactions = [101, 102, 103, 101, 104, 102, 105]

print("Transaction IDs:", transactions)

duplicates = []

for i in range(len(transactions)):
    if transactions[i] in transactions[:i]:
        if transactions[i] not in duplicates:
            duplicates.append(transactions[i])

print("\nRepeated Transactions:")

if len(duplicates) > 0:
    for item in duplicates:
        print(item)
else:
    print("No repeated transactions found.")

print("\nSuspicious Transactions:")

for item in duplicates:
    print("Transaction ID:", item)
