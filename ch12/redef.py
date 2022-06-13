def count(num):
    if num>=1:
        print(num,end=' ')
        count(num-1)
    else:
        return
count(10)
print("\n")
count(20)

def genFunc():
    yield 1
    yield 2
    yield 3

print("\n")
print(list(genFunc()))