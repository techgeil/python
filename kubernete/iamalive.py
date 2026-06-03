import time
import projekt as p
i = 0
#help(p.smile)
#time.sleep(5)


while True:
    if i == 10:
        print("Hej, jeg har vært i live i " + str(i) + " sekunder", flush=True)
        p.smile(5)
    else:
        print("Hej, jeg er i live! " + str(i), flush=True)
        
        
    i += 1
    time.sleep(1)
    
        