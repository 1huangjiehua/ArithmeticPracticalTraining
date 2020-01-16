def chushu():
    count=0
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                for l in range(1,10):
                    for m in range(1,10):
                        for n in range(1,10):
                            for o in range(1, 10):
                                for p in range(1, 10):
                                    for q in range(1, 10):
                                        if (i != j and i!= k and i!= l and i!= m and i!= n and i!=o and i!=p and i!=q):
                                            if(j!=k and j!=l and j!=m and j!=n and j!=o and j!=p and j!=q):
                                                if (k!=l and k!=m and k!=n and k!=o and k!=p and k!=q):
                                                    if (l!=m and l!=n and l!=o and l!=p and l!=q):
                                                        if (m!= n and m!=o and m!=p and m!=q):
                                                            if (n!= o and n != p and n != q):
                                                                if(o!=p and o!=q):
                                                                    if(p!=q):
                                                                        if(i/(j*10+k)+l/(m*10+n)==o/(p*10+q)):
                                                                            print(i, j, k, l, m, n,o,p,q)
                                                                            count=count+1
    return count

chushu()
print(chushu())

