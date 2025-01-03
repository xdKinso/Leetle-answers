#code fizzbuzz
#time comlexity 0(n)
list = range(1, 101)
def fizzbuzz():
    for i in list:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()

    