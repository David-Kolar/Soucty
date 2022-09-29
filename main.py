s = 0
def formula(x):
    return (x+1)**2*2**(x+1) - 8*(x*2**x - 2**x + 1) - 2**(x+2) + 2

for x in range(10):
    s += x**2*2**x
    print(s, formula(x))