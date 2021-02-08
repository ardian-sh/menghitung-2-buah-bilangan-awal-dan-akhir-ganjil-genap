even = int(input("total even number : "))
print(even, "first even number : ",end="")
for i in range(2,even*2,2):
    print (i,end=", ")
print(even*2)