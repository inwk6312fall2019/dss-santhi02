num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


'''def chop(nom):
    del nom[0]
    del nom[-1]
    print nom

print chop(nom)'''


def middle(nom):
    t = nom[1:-1]
    return t

print (middle(num))
