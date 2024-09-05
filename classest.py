'''CustomerList=['varada','vallabha']
InitialBalance=[100,100]
def BankOp():
    k=input("name of customer : ")
    if k in CustomerList:
        m=input("Debit/Credit/BalanceChecking")
        if m == 'Debit':
            Debit_Amount= int(input("Amount to be debited: "))
            R= CustomerList.index(k)
            print(type(InitialBalance[R]))
            print(type(Debit_Amount))
            InitialBalance[R]=InitialBalance[R]- Debit_Amount
            print("Debited : ",Debit_Amount,'Balance is : ',InitialBalance[R])
            return InitialBalance
        if m=="Credit":
            Credit_Amount=int(input("amount to be credited: "))
            R=CustomerList.index(k)
            InitialBalance[R]=InitialBalance[R]+ Credit_Amount
            print("Credited : ", Credit_Amount, 'Balance is : ', InitialBalance[R])
            return InitialBalance
        if m=="BalanceChecking":
            R=CustomerList.index(k)
            print("Balance is : ",InitialBalance[R])

BankOp()'''




