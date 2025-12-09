
def evenodd(start,end):
    for n in range(start,end):
        if n % 2 == 0:
            print(f"{n} is even")
        else:
             print(f"{n} is odd")

evenodd(10,20)