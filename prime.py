n=60
if(n>=2):
  print("The number is greater or euqal than 2")
  for i in range(2,n):
    if(n%i==0):
      print("The number is not prime")
      break
    else:
        print("The number is prime")
        break

    n=1
if(n>0):
  for i in range(5):
    print(i)
  print("The number is positive")
elif(n<0):
 print("The number is negative")   

