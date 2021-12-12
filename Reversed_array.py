def digitize(n):
    n = str(n)
    lst = []
    for i in n:
        lst.append(int(i))
    print(lst[::-1])
digitize(348597)