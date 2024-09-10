import random

b = random.randint(1,100)
i = 1

while(True):
    a = int(input("vpisi stevilo:"))
    
    if(a == b):
        print(f"BRAVO! uganil si v {i} poskusih")
        break
    if(a < b):
        print("vecje")
    if(a > b):
        print("manjse")
        
    i = i + 1