mylist = [64, 34, 25, 12, 22, 11, 90, 5] # 8 items
#.       [0,   1,  2, 3,  4,  5,  6, 7]

n = len(mylist) # 8

for i in range(n-1): # 0, 1, 2, 3, 4, 5, 6
  for j in range(n-i-1): # range(7) -> range (6)

    # 0.          1
    if mylist[j] > mylist[j+1]: # 64 > 34
      
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j] # 34, 64


print(mylist)