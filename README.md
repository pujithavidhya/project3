# PROJECT 3 – REPEATED TRANSACTION DETECTION

## About the Project
The Repeated Transaction Detection project is designed to identify duplicate transactions in a given list of transaction records. It checks whether the same transaction amount occurs multiple times and displays the repeated transactions. This helps in detecting duplicate entries and maintaining accurate transaction records.

## Technologies Used
- **Python** – Used to develop the program.
- **Lists** – Used to store transaction records.
- **Loops** – Used to check each transaction.
- **Conditional Statements** – Used to identify repeated transactions.
- **Sets** – Used to track previously checked transactions.

## Main Features
- Accepts multiple transaction records.
- Stores transaction details in a list.
- Checks for repeated transaction amounts.
- Identifies duplicate transactions.
- Displays the repeated transaction details.
- Shows whether duplicate transactions are found or not.

## Algorithm
1. Start the program.
2. Get the number of transactions.
3. Enter the transaction details.
4. Store all transactions in a list.
5. Create an empty set to track visited transactions.
6. Check each transaction in the list.
7. If a transaction is already present in the set, identify it as repeated.
8. Otherwise, add it to the set.
9. Display the repeated transactions.
10. Stop the program.

## Sample Output
```text
Enter number of transactions: 6

Enter transaction amounts:
100
200
300
100
500
200

----- TRANSACTION REPORT -----

Repeated Transactions: 100, 200

Duplicate Transactions Found.
```

## Conclusion
This project helps identify repeated transactions and detect duplicate entries in transaction records. It demonstrates the use of Python lists, sets, loops, and conditional statements for basic duplicate detection.
