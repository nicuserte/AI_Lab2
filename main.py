import heapq

def find_best(pq, viz):
    #folosim un priority queue si un vector in care am marcat nodurile vizitate
    x=heapq.heappop(pq)
    #gasim cel mai apropiat vecin nevizitat:
    while viz[x[1]]:
        x = heapq.heappop(pq)
    return x

def write_sol(g, sol, cost):
    g.write(str(len(sol)) + '\n')
    for i in range(0, len(sol)):
        g.write(str(sol[i]))
        if i < len(sol) - 1:
            g.write(',')
    g.write('\n')
    g.write(str(cost))
    g.close()

def solve(filename, k, start, end):
    f = open(filename, "r")
    g = open("out.txt", "w")
    n = [int(x) for x in f.readline().split()][0]
    q=[]        #priority queue
    for i in range(0, n):
        line=f.readline().split(',')
        q.append([])
        for j in range(0, n):
            d=int(line[j])
            if j!=i:
                heapq.heappush(q[i], (d, j))    #ordonam dupa distanta
    cost = 0
    viz = [0 for i in range(0, n)]
    if k==1:    #pentru prima cerina, incepem din primul nod
        start=1
    sol = [start]
    start = start - 1   #folosim indexarea de la zero
    end = end - 1
    viz[start] = 1
    node = start
    if k==1:    #prima cerinta
        while len(sol)<n:
            next=find_best(q[node], viz)    #cel mai apropiat vecin
            cost+=next[0]       # primul element din tupple reprezinta costul, al doilea este nodul
            sol.append(next[1]+1)
            node=next[1]
            viz[next[1]]=1  #marcam nodul ca fiind vizitat
        viz[0] = 0  #ne intoarcem la primul nod, deci il marcam ca fiind nevizitat
        next = find_best(q[node], viz)
        cost += next[0]
    elif k==2:  #cerinta 2, cazul in care trebuie sa ajungem la nodul 'end'
        while node != end:
            next = find_best(q[node], viz)
            cost += next[0]
            sol.append(next[1] + 1)
            node = next[1]
            viz[next[1]] = 1
    write_sol(g, sol, cost)
