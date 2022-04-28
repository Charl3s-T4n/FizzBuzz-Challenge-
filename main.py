#Write your code below this row 👇

for number in range(1,101):
  if number % 15 == 0:     #Have to put this condition first: E.g: If 3 is placed first instead of 15, number 15 will output Fizz instead of FizzBuzz due to if-elif condition
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
