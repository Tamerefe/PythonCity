frst = int(input("Select first fibonacci number : "))
scnd = int(input("Select second fibonacci number : "))

for x in range(30): 
  print(frst)  
  total = frst + scnd 
  frst = scnd  
  scnd = total 