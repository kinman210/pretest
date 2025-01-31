def fib_gen(n): #generator function to provide first n fib numbers
   fib_nums = [1,1]

   for i in range(2, n):
       next_fib = fib_nums[-1] + fib_nums[-2]
       fib_nums.append(next_fib)

   return fib_nums[:n]

#test:
n = int(input("please enter a positive integer: n= "))
for num in fib_gen(n):
    print(num, end=",")

print()
print(f"sum of first {n} fib number is: {sum(x for x in fib_gen(n))}")