class triangle2(Exception):
    def triangle2(number):
        first = 0
        count = 0
        n0 = number
        for j in range(number):
            for x in range(count - 1):
                if first == 0:
                    print(" ", end='')
                    first == 1
            print(" ", end='')
            count += 1
            for i in range(n0):
                print("#", end='')
            print("#")
            n0 -= 2
            