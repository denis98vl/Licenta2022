import random
import time



i = 0
while i<600:
        voltage = open("voltage.txt", "w")
        tensiune = str(random.randint(1, 5))
        voltage.write(tensiune)
        print(tensiune)
        i += 1
        voltage.close()
        time.sleep(1)
