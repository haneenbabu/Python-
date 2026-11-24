list_1= input("enter the first list of integers (separated by comma): ")
list1= [int(x) for x in list_1.split(",")]
list_2 = input("enter the second list of integers (separated by comma): ")
list2= [int(x) for x in list_2.split(",")]
if len(list1) == len(list2):
  print("the lists are same length:", len(list1))
else:
  print("the lists are not same length")
print("the sum of elements of lists1:", sum(list1))
print("the sum of elements of list2:", sum(list2))

if sum(list1) == sum(list2):
   print("the sum of lists are same")
else:
   print("the sum of lists are not same")
common=[]
for value in list1:
    if value in list2:
      common.append(value)
if common:
  print("the common values in both lists:", common)
else:
  print("no common value found in both lists")

