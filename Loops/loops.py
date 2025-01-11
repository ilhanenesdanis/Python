#for loop

for each in range(1,11):
    print(each)


lists=[1,2,4,56,7,3,13,44,53]

sum_list=sum(lists)

print(sum_list)

count=0
for each in lists:
    count=count+each
    print(count)

#while loop

i=0
while (i<=10):
    print(i)
    i=i+1
each=0
totalCount=0
listCount=len(lists)
while (each<listCount):
   totalCount=totalCount+lists[each]
   each=each+1

print(totalCount)