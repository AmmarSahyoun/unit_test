

def bubblesort(mylist, dec = 0):
    length = len(mylist)
    for i in range(0, length-1):
        for j in range(0, length-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1]=mylist[j+1],mylist[j]
    if dec:
        mylist.reverse()

    return mylist