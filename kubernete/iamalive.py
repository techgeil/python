import time
import projekt as p
i = 0

time.sleep(5)


while True:
    if i != 10:
        print("Hej, jeg er i live! " + str(i), flush=True)
    else:
        print("Hej, jeg har vært i live i " + str(i) + " sekunder", flush=True)
        p.smile()
    i += 1
    time.sleep(1)
    
        