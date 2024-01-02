import krishna
krishna.add(10,20)
krishna.pro(30,40)

import krishna,cherry
print(cherry.x)
krishna.add(30,49)

import krishna as r
print(r.a)
r.add(10,30)
r.pro(10,30)

from krishna import a
print(a)

from krishna import a, add, pro
print(a)
add(10,20)
pro(10,60)

from krishna import a as x,add as b, pro as c
print(x)
b(3,8)
c(4,8)

from krishna import *
print(a)
add(10,44)
pro(3,8)
