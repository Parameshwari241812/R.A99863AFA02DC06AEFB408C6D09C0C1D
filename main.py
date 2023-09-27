# CONSTRUCT A PATTERN USING NESTED LOOP #
print("CONSTRUCT A PATTERN USING NESTED LOOP")
print("-------------------------------------")
num=int(input("Enter number of rows:"))
for i in range(num):
  for j in range(i+1):
    print(i+1,end="")
    print()