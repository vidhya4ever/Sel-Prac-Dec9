class math_operation:
 def evenodd(self, start,end):
    for n in range(start,end):
        if n % 2 == 0:
            print(f"{n} is even")
        else:
             print(f"{n} is odd")

obj = math_operation()
obj.evenodd(1,10)