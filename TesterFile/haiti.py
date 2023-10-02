import time
for x in range (0,5):  
    b = "Working" + "." * x
    print (b, end="\r")
    time.sleep(1)
