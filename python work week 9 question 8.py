def f(x) :
return g(x) + math.sqrt(h(x))
def g(x) :
return 4 * h(x)
def h(x) :
return x * x + k(x) - 1
def k(x) :
return 2 * (x + 1)

x1 = f(2)
