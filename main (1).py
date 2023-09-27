#FINDING SUM OF ALL ITEMS IN A DICTIONARY#
def dict_sum(dict):
  sum=0
  for i in dict.values():
     sum=sum+i
  return sum
dict={'a':150, 'b':210, 'c':130, 'd':90}
print("FINDING SUM OF ALL ITEMS IN A DICTIONARY")
print("-------------------------------------------")
print("Sum of all items in a dictionary:", dict_sum(dict))
