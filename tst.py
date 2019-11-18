import sys
mypdir = sys.executable
myver = sys.version
myverinfo = sys.version_info

print ( "dir: " + str(mypdir))
print ( "ver: " + str(myver))
print ( "ver info: " + str(myverinfo))

def fib_din(n):
    fib = [1, 2] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        
    print(n, fib[-1])
    print(fib)
fib_din(15)
