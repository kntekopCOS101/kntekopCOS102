print("Welcome Staff!")
age = int(input("Please enter your age "))
years = float(input("Please enter your working experience in years "))
if years >= 25 and age >= 55 :
    print("Your Annual Tax Revenue is 5,600,000")
elif years >= 20 and age >= 45 :
    print("Your Annual Tax Revenue is 4,400,000")
elif years > 10 and age >= 35 :
    print("Your Annual Tax Revenue is 1,500,000")
else :
    print("Your Annual Tax Revenue is 550,000")
