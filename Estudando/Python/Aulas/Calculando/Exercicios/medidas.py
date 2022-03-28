from ast import Num


num = float(input('Digite um valor em metros: '))
dam = num / 10
hm = dam / 100
km = hm / 1000
dm = num * 10
cm = num * 100
mm = num * 1000
print(f'A medida de {num}m corresponde a\n{km}km\n{hm}hm\n{dam}dam\n{dm}dm\n{cm}cm\n{mm}mm')