class timer(Exception):
    def timer():
        import os
        import time
        count = 0.0
        while True:
            count += 0.1
            time.sleep(0.1)
            os.system('cls')
            print(round(count,2))

