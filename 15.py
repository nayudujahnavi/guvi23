lower=int(input(" "))
upper=int(input(" "))
for num in range(lower+1,upper):
  if(num>1):
    for i in range(2,num):
      if(num %i)==0:
else:
  print(num)
