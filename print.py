
b = 1
a = b
c = b
d = c
b = d

damir = 5 + 1
darina = 6 - damir
mochila = damir - darina
mochila_starshiy = damir + darina + mochila

#print ('Результат будет ' + str (mochila_starshiy))

flag = (True and False) or (not True or not False)
flag_new = (flag and True) and (flag or False) and True

print ('Результат логического выражения - ' + str (flag_new))
