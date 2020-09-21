pris = float(input('Skriv varans pris: '))
moms = float(input('Skriv varans moms i procent: '))

emoms = pris / (moms / 100 + 1)

print(f'Priset exklusive moms: {emoms}')
print(f'Momsen är: {pris - emoms} ')