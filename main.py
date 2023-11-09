year = 52
amount = 100000

for i in range(year):
    amount = amount + (amount * 0.12)
    if(i > 10):
        print(str(i + 18) + " age: " + str(round(amount, 2)))