num = 1000
# To take input from user
# num = int(input("enter a number :"))
# prime numbers are greater than 1
if num > 1:
  # check factors
  for i in range(2, num):
    if (num %1) == 0:
      print(num,"is not a prime number")
      print(i,"time",num//i,"is",num)
      break
  else:
    print(num,"is a prime number")
 # if input number is less than
 # or equal to 1, it is not prime
else:
    print(num,"is not a prime number")