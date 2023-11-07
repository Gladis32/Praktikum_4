#mencari bilangan terbesar dari 3 bilangan 
bilangan1 = int(input("masukkan bilangan pertama:"))
bilangan2 = int(input("masukkan bilangan kedua:"))
bilangan3 = int(input("masukkan bilangan ketiga:"))

bilangan_terbesar = bilangan1
if bilangan2 > bilangan_terbesar:
    bilangan_terbesar = bilangan2

if bilangan3 > bilangan_terbesar:
    bilangan_terbesar = bilangan3

print("bilangan terbesar adalah: ", bilangan_terbesar)