for i in range(int(input())):
    a = int(input())
    if a >= 38:
        nex = 5 * (a//5 + 1)
        if (nex - a) < 3:
            #print('loop er bhitore dhukchi')
            a = nex
    print(a)
