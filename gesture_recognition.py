balance = 100000

while True:
    action = int(input("""User options:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
""")
)
    if action == 1:
        print(f"Current Balance: {balance}")
        
    if action == 2:
        deposit = int(input("Enter your deposit amount: "))
        balance += deposit
        print(f"Current Balance after Deposit: {balance}")
        
    if action == 3:
        withdrawal = int(input("Enter your withdrawal amount: "))
        if withdrawal > balance:
            print("Withdrawal amount is more than balance")
        else:
            balance -= withdrawal
            print(f"Current Balance after withdrawal: {balance}")
            
    if action == 4:
        print("No actions")
        break