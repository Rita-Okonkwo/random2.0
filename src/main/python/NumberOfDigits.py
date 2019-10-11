  #python code to print out the number of digits in a number
  number = int(input("Enter a number:"))
  count = 0
  while(number > 0):
    #dont be confused, the double forward slash is for integer division in python
    number = number // 10
    count = count + 1
  print(count)

