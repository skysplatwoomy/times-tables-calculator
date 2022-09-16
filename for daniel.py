print("aight daniel here's your program")
try:
    timestables = int(input("what timestables do you want? "))
except ValueError:
    print("why you trying to find the timestables to words man")
    input("press enter to exit ")
    from sys import exit
    exit(0)
n = 0
for x in range(1,13):
    n += 1
    print(f"{n} x {timestables} = {n*timestables}")
input("press enter to exit ")
