import calculation as ca

USER_DATA = {
    "username": "admin",
    "acc.no": 123456,
    "pin": 1234,
    "balance": 10000
}


def user_info():
    if USER_DATA and USER_DATA["username"]:
        return f"\nHi User {USER_DATA['username']} Your Account no Is {USER_DATA['acc.no']}"
    else:
        print("User Not Found")


def deposit(deposite_amount):
    if deposite_amount:
        amount = ca.deposit_calc(USER_DATA['balance'], deposite_amount)
        USER_DATA['balance'] = amount
        return amount
    else:
        print("Amount Not Found")


def withdraw(withdraw_amount):
    if withdraw_amount:
        amount = ca.withdraw_calc(USER_DATA['balance'], withdraw_amount)
        USER_DATA['balance'] = amount
        return amount
def check_balance():
    return USER_DATA["balance"]

def main():
  print("welcome to tp atm")
  pin_no=int(input("enter the pin no:"))

  if USER_DATA and USER_DATA["pin"]==pin_no:
      print(f"user_info: {user_info()}")
      while True:
        choice=int(input("""
    1. Deposit
    2. Withdraw
    3. Check Balance
    4. Exit
    Enter Your Choice : """))
        match choice:
            case 1:
                amount = int(input("Enter The Amount :"))
                print(f"Deposite successfully, your total balance is: {deposit(amount)}")

            case 2:
                amount = int(input("Enter The Amount :"))
                print(f"Withdraw successfully, your total balance is: {withdraw(amount)}")

            case 3:
                print(f"Your Total Balance is: {check_balance()}")

            case 4:
                print("Thanks For Using TP ATM")
                break

            case _:
                print("Invalid Choice, please select between 1 to 4")

  else:
      print("Invalid Pin No.")

if __name__ == "__main__":
    main()
