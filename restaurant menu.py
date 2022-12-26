#Restaurant Billing System

veg=['Fried Rice','Dal Makhani','Burger','Gulaab Jamun','Dosa','Soup','Paneer Do Pyaza']
vp=[100,120,60,15,120,60,180]
nveg=['chicken','egg','fish']
np=[200,30,150]
snack=['Manchurain','SpringRoll','Paani-Puri']
sp=[130,70,110]

n=int(input('Enter no of veg items ordered: '))
for a in range(len(veg)):
    veg[a]=veg[a].upper()
    
for b in range(len(nveg)):
    nveg[b]=nveg[b].upper()

for c in range(len(snack)):
    snack[c]=snack[c].upper()

menu={}
for x in range(n):
    name=input('Enter veg dish name: ')
    name=name.upper()
    quantity=int(input('Enter quantity: '))
    for a in range(len(veg)):
        if veg[a]==name:
            menu.update({name:quantity*vp[a]})

p=int(input('Enter no of non-veg items ordered: '))
for x in range(p):
    name=input('Enter non-veg dish name: ')
    name=name.upper()
    quantity=int(input('Enter quantity: '))
    for a in range(len(nveg)):
        if nveg[a]==name:
            menu.update({name:quantity*np[a]})

s=int(input('Enter no of snack items ordered: '))
for x in range(s):
    name=input('Enter snack dish name: ')
    name=name.upper()
    quantity=int(input('Enter quantity: '))
    for a in range(len(snack)):
        if snack[a]==name:
            menu.update({name:quantity*sp[a]})

print('Ordered Menu')
for a,b in menu.items():
    print(a,':',b)
total=0
for x in menu.values():
    total=total+x
print('Total Bill=',total)
