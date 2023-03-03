set1 = {"k"}
set2 = {"k"}


def create(se, n):
    for i in range(n):
        a = int(input(f"Enter values for {se} : "))
        se.add(a)
    se.remove("k")
    return se


def add(se):
    a = int(input("Enter values to add in the set : "))
    se.add(a)
    return se


def remove(se):
    a = int(input("Enter values to remove from the set : "))
    se.remove(a)
    return se


def intersection(x, y):
    x.intersection_update(y)

    return x


def union(x,y):
    set3 = x.union(y)
    print(set3)


def symmetric_difference(x,y):
    z = x.symmetric_difference(y)
    return z


n = int(input("How many elements do you want in the set1: "))
print(create(set1, n))

n = int(input("How many elements do you want in the set1: "))
print(create(set2, n))


print("------MENU-------")
k = int(input("Choose an action to perform: \n 1) Add \n 2) Remove \n 3)Contains \n 4)Length of Set \n 5) Union \n 6) Intersection \n 7) Symmetric Difference \n 8) Check if Subset\n:"))

if(k==1):
    g = input("Enter which set you want to add the value in : ")
    print(add(k))
elif(k==2):
    g = input("Enter which set you want to remove the value from : ")
    print(remove())
elif(k==3):
    g = input("Enter set : ")
    v = int(input("Enter value to check : "))
    if(v in g):
        print(f"{v} is present in {g}")
elif(k==4):
    g = input("Enter set : ")
    print(len(g))
elif(k==5):
    print(union(set1, set2))
elif(k==6):
    print(intersection(set1, set2))
elif(k==7):
    print(symmetric_difference(set1, set2))
elif(k==8):
    z = set1.issubset(set2)
    print(z)




