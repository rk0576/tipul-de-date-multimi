A=set(input())
B=set(input())
a,b=set(),set()
for i in A:
    if i.isdigit():
        a.add(i)
for i in B:
    if i.isdigit():
        b.add(i)
print('reuniunea mulţimilor A şi B->',a.union(b))
print('intersectia multimilor->',a.intersection(b))
print('diferenţa mulţimilor A şi B->',a.difference(b))
print('diferenţa mulţimilor B şi A->',b.difference(a))