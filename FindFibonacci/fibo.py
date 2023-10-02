frst = int(input("Select first fibonacci number : "))
scnd = int(input("Select scnd fibonacci number : "))

total = 0

for x in range(30):
  print(frst,scnd)
  total = frst + scnd
  frst = scnd
  scnd = total
