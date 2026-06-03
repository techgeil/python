import time

i = 0


while True:
    print("Hej, jeg er i live! " + str(i), flush=True)
    i += 1
    time.sleep(1)