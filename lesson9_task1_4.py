def qwe(n):
    for i in range(n):
        if i%7 == 0:
            yield i
itr=qwe(100)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
