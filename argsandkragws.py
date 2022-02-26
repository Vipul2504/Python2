def funargs(nrml1,*args):
    print(nrml1)
    for i in args:
        print(i)
        
pawan = ["pawan1","pawan1","pawan1","pawan1","pawan1","pawan1","pawan1"]        
funargs(*pawan)