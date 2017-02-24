#project name: Blastoff
#programmer: Yang Tang
#date: 2/16/2017
#description: ask user enter loan amount and period to get the total payments and interest rate
import math
# yt: import math to use math.pow function, which is x to the power of y, it has same usage as **

def LoanInterest():
    loanAmt = 0
    ans="y"
    # yt: the initial vaule
    while ans is "y" or ans is "Y":
        # yt: use while loop to have infinity input unless user decide to quit
        loanAmt=float(input("Enter the amount (greater than 0) of the loan :"))
        # yt: input the loan amount
        numYears=int(input("Enter the year as an integer :"))
        # yt: input the number of years
        Rates=[4,5,6,7,8]
        # yt: use list to store different rates
        print("anualRate", "\t monthlyPayment", "\t totalPayment")
        # yt: print the header of the solution
        for anualRate in Rates:
            # yt: use for loop to calculate the different rate
            monthlyRate=float(anualRate/1200)
            # yt: convert the annual rate to monthly rate and take out the % symbol
            monthlyPayment=loanAmt * monthlyRate/(1-math.pow(1/(1+monthlyRate),numYears*12))
            # yt: the calculation of the monthlyrate using math.pow
            totalPayment=monthlyPayment* numYears *12
            # yt: the calculation of the total rate
            monthlyPayment="%.2f"%monthlyPayment
            # yt: make the monthlypayment to have .xx precision
            totalPayment="%.2f"%totalPayment
            # yt: make the totalpayment to have .xx precision
            print(anualRate,"%","\t\t",monthlyPayment,"                 ",totalPayment)
            # yt: print out the calculation result
        ans=str(input("Do you wanna create another table,Y/N"))
        # yt: ask user if they want to input another data


LoanInterest()