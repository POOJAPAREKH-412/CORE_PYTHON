l=[1,2,1.2,1.5,"tops",True,"python",1,2,False]

print(l)
l.append(100)
print(l)
# l.clear()
# print(l)
l1=l.copy( )
print(l1)
l1.append(200)
print(l)
print(l1)
l2=l
print(l2)
l2.append(300)
print(l)
print(l2)
print(l.count(1))
l3=[1000,2000,3000]
l.extend(l3)
print(l)
print(l.index(1.2))
l.insert(5,101)
print(l)
l.pop( )
print(l)
l.pop(3)
print(l)
l.remove(101)
print(l)
l.reverse( )
print(l)


