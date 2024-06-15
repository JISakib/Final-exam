
class Users:
    def __init__(self,name,email,address,account_type,account_no):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.account_no=account_no
        self.balance=0
        self.loan=0
        self.loanAmount=0
        self.transaction=[]


    def deposite(self,amount):
        self.balance+=amount
        print(f"{amount} taka deposite successfully")
        self.transaction.append(Transaction(f"Deposite: {amount}"))

    def withdraw(self,amount):
        if amount>self.balance:
            print("Withdraw amount exceeded !!")    
        else:
            self.balance=self.balance-amount
            print(f"withdrawl of {amount} done")  
            self.transaction.append(Transaction(f"Withdraw:{amount}"))  
            

    def take_loan(self,amount):
        if self.loan>=2:
            print("Your loan limit gone")
        elif bank.loanActive==False:
            print("Loan option is currently unavailable !!")
        elif self.balance<amount:
            print("You are bankrupt")   
        else:
            print(f"{amount}tk Loan recived successfully")
            self.balance+=amount
            self.loan+=1
            self.loanAmount += amount
            self.transaction.append(Transaction(f"Loan:{amount}"))
                              
    def check_balance(self):
        print(f"Available balance: {self.balance}")
    

    def transfer_money(self,amount,recipient_account):
        if amount > self.balance:
            print("Insufficient balance !!")
        else:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction.append(Transaction(f"Transfer : {amount}"))
            print(f"Transfer of {amount} to {recipient_account.name} successful.")
            self.check_balance()  
            recipient_account.check_balance()  

    def view_transaction_history(self):
        print("Transiction History")
        for transaction in self.transaction:
            print(f"Amount: {transaction.amount}")


class Bank:
    def __init__(self,name):
        self.name=name
        self.total_amount=0
        self.loanActive=True
        self.total_loan=0
        self.loanActive=True
        self.users=[]
        self.bankrupt=False
           
    
    
    def create_account(self,name,email,address,account_type,account_no):
        user=Users(name,email,address,account_type,account_no)
        self.users.append(user)
        print(f"Account :{account_no} open succesfully!!")
        return user
    
    def delete_account(self,account_no):
        for user in self.users:  
            if user.account_no == account_no:
                self.users.remove(user)
                print(f"This account :{account_no} deleted")
                return
        print("Account didnt existed")

    def all_accounts(self):
        for user in self.users:
            print(f"Account name:{user.name} Account no:{user.account_no}")
    
    def check_total_balance(self):
        self.total_amount=sum(user.balance  for user in self.users)
        print(f"Total balance in bank:{self.total_amount}")
    
    
    def see_total_loan(self):
        self.total_loan_amount=sum(user.loanAmount for user in self.users)  
        print(f"Total loan ammount is:{self.total_loan_amount}")                                                    
    
    def off_loan(self):
        self.loanActive = False
        print("Loan feature is off.")

    def on_loan(self):
        self.loanActive = True
        print("Loan feature is on.")       


class Transaction:
    def __init__(self, amount):
        self.amount = amount



bank=Bank("WWE")
while True:
    print("Welcome to the WWE Bank")
    print("1.ADMIN")
    print("2.User")
    print("3.Exit")    
    
    choice=int(input("Enter your choice: "))

    if choice==1:
        print("Admin ")
        print("1.Create account")
        print("2.Delete account")
        print("3.Show all account")
        print("4.Check balance ")
        print("5.Check total loan amount ")
        print("6.Turn off loan option")
        print("7.Turn on loan option")


        admin=int(input("Enter admin choice: "))

        if admin ==1:
            print()
            account_no = int(input("Enter account number: "))
            name=input("Enter user name: ")
            email= input("Enter user email: ")
            address = input("Enter user address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account( name, email, address, account_type,account_no)

        elif admin ==2:
            print()
            account_no=int(input("Enter account number: "))
            bank.delete_account(account_no)

        elif admin==3:
            bank.all_accounts()

        elif admin==4: 
            bank.check_total_balance()  

        elif admin==5: 
            bank.see_total_loan()

        elif admin==6: 
            bank.off_loan()

        elif admin==7: 
            bank.on_loan()    
        
        else:
            print("Invalid choice")  


    elif choice==2:
        print("User")
        print("1.Create account")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Check available balance")
        print("5.Take loan")
        print("6.Transfer money")
        print("7.Check transiction history")

        customer=int(input("Enter your choice: "))

        if customer ==1:
            print()
            account_no = int(input("Enter account number: "))
            name=input("Enter user name: ")
            email= input("Enter user email: ")
            address = input("Enter user address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account( name, email, address, account_type,account_no)

        elif customer==2:
            print()
            account_no=int(input("Enter account Number: "))
            amount=int(input("Enter amount to Deposit: "))
            for user in bank.users:
                if user.account_no==account_no:
                    user.deposite(amount)
                    break
            else:
                print("Error.Account does not exists")
            
        elif customer==3:
            print()
            account_no=int(input("Enter account number: "))
            amount=int(input("Enter the amount want to withdraw: "))
            for user in bank.users:
                if user.account_no==account_no:
                    user.withdraw(amount)
                    break
            else:
                print("Error.Account doest not exists")  

        elif customer==4:
            print()
            account_no=int(input("Enter account number: "))
            for user in bank.users:
                if user.account_no==account_no:
                    user.check_balance()
                    break
            else:
                print("Error.Account doest not exists")          
        
        elif customer==5:
            print()
            account_no=int(input("Enter account number: "))
            amount=int(input("Enter the loan amount: "))
            for user in bank.users:
                if user.account_no==account_no:
                    user.take_loan(amount)
                    break
            else:
                print("Error.Account doest not exists")

        elif customer==6:
            print()             
            account_number = int(input("Enter your account number: "))
            recipient_account_number = int(input("Enter recipient account number: "))
            amount = int(input("Enter amount to transfer: "))
            sender_account = None
            recipient_account = None
            for user in bank.users:
                if user.account_no == account_number:
                    sender_account = user
                elif user.account_no == recipient_account_number:
                    recipient_account = user
            if sender_account is not None and recipient_account is not None:
                sender_account.transfer_money(amount,recipient_account)
            else:
                print("Account does not exist")
        elif customer==7:
            account_no=int(input("Enter account number: "))
            for user in bank.users:
                if user.account_no==account_no:
                    user.view_transaction_history()
                    break
            else:
                print("Error.Account doest not exists")

        else:
            print("Invalid choice")                        

    elif choice==3:
        break
    else:
        print("Invalid choice")    
    

 


