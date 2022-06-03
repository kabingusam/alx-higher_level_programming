def fizzbuzz():
    for num in range (1,101):
        # multiple of 3  print Fizz
        # multiple of 5 print Buzz
        # multiple of both 3 and 5 print FizzBuzz
        if num % 3 == 0 and num % 5 == 0:
            print(("FizzBuzz"),end=" ")
        elif num % 3 == 0:
            print(("Fizz"),end=" ")
        elif num % 5 == 0:
            print(("Buzz"),end=" ")
        else:
            print("{}".format(num),end=" ")