#  Let's understand some things about how python passes lists

def mutate_list(l):
    if len(l) > 1:
        l[len(l)-2] = "Second to Last!"
    return l

def mutate_list_comprehensively(m):
    n = [m[i] if i%2!=0 else 'even!' for i in range(len(l))]
    print(m, 'arg list from function')
    print (n, 'mutated from function')
    return n

l = []
for i in range(10):
    l.append(i)

print(l)
l = mutate_list(l)
print(l)

p = mutate_list_comprehensively(l)
print(p, 'from main')

print('Now mutate without return')
print(p, 'before calling mutate_list.')
mutate_list(p)
print(p)
