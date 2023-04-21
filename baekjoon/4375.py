def answer(input: str):
    for n in map(int,input.split()):
        m = 1
        while True:
            if m%n == 0:
                print(len(str(m)))
                break
            
            m*=10
            m+=1
    
        
answer("1 3 7 9901")
