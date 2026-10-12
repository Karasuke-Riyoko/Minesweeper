import random
def mines(n):
    k=[]
    d= (n**2)//2 +random.randint(0,n)
    c=[]
    for i in range(n):  
        c.append('o')
    for ik in range(n):
        k.append(c.copy())
    
    l=[]

    while True:
        if d ==0:
            break
        a=(random.randint(0,n-1),random.randint(0,n-1))
        if l.count(a) == 0:
            l.append(a)
            d-=1
            k[a[0]][a[1]] ='x'
    for i in k:
        for j in range(0,n):
            print(i[j],'   ',end='')
        print()
    print()
    k1=((n-1,0),(n-1,n-1),(0,n-1),(0,0))
    for i in range(n):
        for j in range(n):
            if k[i] [j] =='x':
                continue
            
            for op in range(n):
                loki = [(i-1,j-1),(i,j-1),(i+1,j-1),(i-1,j),(i,j),(i+1,j),(i-1,j+1),(i,j+1),(i+1,j+1)]
                kon = loki.copy()
                for komi in kon:
                    if komi[0] <0 or komi[1]<0 or komi[0]>n-1 or komi[1]>n-1 :
                        loki.remove(komi)
                        
            fein = []
            for moto in loki:
                fein.append(k[moto[0]] [moto[1]])
            k[i][j] =str(fein.count('x'))
    for i in k:
        for j in range(0,n):
            print(i[j],'   ',end='')
        print()




# Edit this for difficulty
while True:
    a =input('Choose your difficulty :- \n1. Human \n2. Deity \n3. God \n')
    if a == '1' or a.lower()=='human':
        mines(7)

    elif a == '2' or a.lower()=='deity':
        mines(9)
   
    elif a == '3' or a.lower()=='god':
        mines(13)

    else:
        print('Get your eyes checked moron')
        


