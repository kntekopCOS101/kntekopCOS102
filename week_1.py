solve = input("wILL YOU LIKE TO SOLVE SIMPLE INTEREST, COMPOUND INTEREST OR ANNUITY PLAN? ")
if solve == "SIMPLE INTEREST":
   principal = int(input("enter principal amount "))
   rate = int(input("enter the rate ")) / 100
   time = int(input("enter the time "))

   amount = principal * (1 + (rate/100)) ** time


   print("Amount is ", int(amount))

elif solve == "COMPOUND INTEREST":
    principal = int(input("enter the principal amount "))
    rate = int(input("enter the rate ")) / 100
    time = int(input("enter the time "))
    n = int(input("how many times is the input compounded per year? "))

    amount = principal * (1 + rate/n) ** (n * time)


    print("Amount is ", int(amount))

elif solve == "ANNUITY":
    pmt = int(input("please enter your regular payment amount "))
    rate = int(input("please enter your rate ")) / 100
    time = int(input("enter the time "))
    n = int(input("how many times is the input compounded per year? "))

    amount = pmt * ((1 + rate/n) ** (n * time) - 1) / (rate/n)

    print("Amount is ", amount)

else :
    print("failed to read input")

