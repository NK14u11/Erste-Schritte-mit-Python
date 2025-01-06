n = 1

while n <= 100:
    if (n % 3 == 0 and n % 5 == 0):
        print("Digital History")
    elif (n % 3 == 0):
        print("Digital")
    elif (n % 5 == 0):
        print("History")
    else:
        print(f"{n}")

    n = n + 1
