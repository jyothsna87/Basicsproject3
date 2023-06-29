# import keyword
# print(keyword.kwlist)
thislist = ["apple", "banana", "cherry"]
print(thislist)
#  allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# indexing
thislist = ["banglore ", "chennai", "vizag"]
print(thislist[1])
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple","box", "plank", "book", "paper", "pen"]
# print(thislist[:4])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# remove
# .remove

for i in range(len(thislist)):
  print(thislist[i])
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
# ****************************************************
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


