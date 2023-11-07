from pyDatalog import pyDatalog as py
py.create_terms("brother,father,cousin,grandson,descendent,X,Y,Z,W,a,b,c,d,e,f,g")
+father('a','b')
+father('a','c')
+father('a','g')
+father('b','d')
+father('b','e')
+father('c','f')
brother(X,Y) <= (father(Z,X)) & (father(Z,Y)) & ~(X==Y)
cousin(X,Y) <= (father(Z,X)) & (father(W,Y)) & (brother(Z,W))
grandson(X,Y) <= (father(Y,Z)) & (father(Z,X))
descendent(X,Y) <= (father(Y,X))
print(brother(X,'c')) # кто брат для 'c'?
print('|----|')
print(cousin(X,Y)) # все кузины в дереве
print('|----|')
print(grandson('e',Y)) # для кого 'e' внук?
print('|----|')
print(descendent(X, 'a')) # кто потомки 'a'?