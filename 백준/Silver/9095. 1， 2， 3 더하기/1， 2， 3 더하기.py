d = {1:1, 2:2, 3:4}
def f(x):
    if x in d:
        return d[x]
    else:
        d[x] = f(x-1) + f(x-2) + f(x-3)
    return d[x]

if __name__ == "__main__":
    t = int(input())
    while t:
        n = int(input())
        print(f(n))
        t -= 1