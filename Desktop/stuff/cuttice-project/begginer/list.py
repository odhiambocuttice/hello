#list slicing
family = [ 'dad', 'daughter', 'son', 'cousin', 'mum', 'uncle']
print(family[0:3])
print(family[4], family[3])
print(family[2:])
print(family[1:6:2])

print(family[5:0:-2])
print(family[:-1], family[0:6])
print(family[:])
print('5' not in family)
print(len(family))

#list inside a list
a =['b',[2,3],'s','r']
print (a[1][1])

#negative list
print(family[-6:-2])

#reversing a list
print(family[::-1])

#concertination
print(family + ['aunt','nephew'])
print(family.append('mister'))

#min max
#print(min(family))

#mutable list #replacemnet
family[0]='child'
family[1:3]=['dadi','dada', 'sun']
print(family)

#inserting a list in a list
family[0]=['me','you'',us','we']
print(family)
print(family.insert(1,'toto'))

#deleting 
del family[0]
print (family)


#insert 4,child,time,spoon inbetween 
b=['tema','fool']
b[1:1]=[4,'child','timesave']
print(b)
b.insert(2,'boy')
print(b)

b_joined=','.join(family)
print(b_joined)