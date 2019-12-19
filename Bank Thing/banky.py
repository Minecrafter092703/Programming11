class Account():
    def __init__(self,owner,balance,password):
        self.owner = owner
        self.balance = balance
        self.password = password

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print("Deposit accepted")

    def withdrawl(self,wd_amt):
        if wd_amt < self.balance:
            self.balance == wd_amt
            print("Withdrawl accepted -- Thank You: ", self.owner)
        elif wd_amt == self.balance:
            self.balance -= wd_amt
            print("Account Closed -- Thank You: ", self.owner)
        else:
            print("Funds unavailable -- Check you Math: ", self.owner)
