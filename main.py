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
print('кто брат для "c"?')
print(brother(X,'c')) # кто брат для 'c'?
print('\n')
print('все кузины в дереве')
print(cousin(X,Y)) # все кузины в дереве
print('\n')
print('для кого "e" является внуком?')
print(grandson('e',Y)) # для кого 'e' внук?
print('\n')
print('кто потомки "a"?')
print(descendent(X, 'a')) # кто потомки 'a'?


