import banky
import time
enter = False

accs = []

checkAcc = input("Do you have an account with us?: ")

if checkAcc == ("no") or checkAcc == ("n"):
    name = input("What's your name?: ")
    bank = input("How much money would you like to deposit?: ")
    passs = input("Please create a password: ")
    accs.append(banky.Account(name, bank, passs))
    print("NS Bank of Canada")
    checkName =input("What is your name: ")
    checkPasss =input("What is your password: ")
    enter = True
elif checkAcc == ("yes") or checkAcc == ("y"):
    print("NS Bank of Canada")
    checkName
    checkPasss
    enter = True
else:
    checkAcc

while enter == True:
    if name == checkName and passs == checkPasss:
        print("Welcome,"+name)
        time.sleep(2)
        deposity = input("How much money would you like to deposit?: ")
        banky.Account.deposit
        withdrawly = input("How much money would you like to withdrawl?: ")
        banky.Account.withdrawl
        print(banky.Account.balance)
