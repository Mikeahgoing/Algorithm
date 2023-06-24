def hanoi(n:int,a:str,b:str,c:str):
    if n>0:
        hanoi(n-1,a,c,b)
        print("moving from %s to %s" %(a,c))
        hanoi(n-1,b,a,c)
hanoi(3,"A","B","C")
