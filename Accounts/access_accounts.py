import accounts as acc


def main():
    sa = acc.SavingsAccount
    print("Enter the following data for a savings account.")
    account_num = input("Account Number: ")
    sa.set_account_num(account_num)
    int_rate = input("Interest rate: ")
    sa.set_interest_rate(int_rate)
    bal = input("Balance: ")
    sa.set_balance(bal)

    #print(accounts.get_account_num())
    
main()
