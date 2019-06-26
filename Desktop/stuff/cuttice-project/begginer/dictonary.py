intern={
	2:'vicky',
	44:'till',
	909:'kimani',
	83:'collins',
}
print(intern[2],  intern[83] )

#adding a new obj
intern[31]='thanos'
print(intern)

#updAting an existing obj
intern[909]='cate'
print(intern)

#deleting
del intern[2]
print(intern)

#list inside a dict
men={'cat':['cheetah','lion','leopard'],'pets':{'coco':'cow','dodo':'dog'}}
print(men['cat'])
print(men['pets']['coco'])
print(men['cat'][-1])

print(men.values())
print(men.update(intern))
del men['cat']
print(men)


men['sungura']="sunguch"
print(men)

for key, value in men.items():
	print(key,value)

