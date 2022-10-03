def compound_interest(principle, rate, time):

    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    return CI


p = int(input("Enter the principal: "))
r = float(input("Enter the rate: "))
t = int(input("Enter the time: "))

result = compound_interest(p, r, t)
print("Compound interest is", result)
