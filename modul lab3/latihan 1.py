import random 
n = int(input("masukkan nilai n:"))

count = 0 
while count < n:
    random_number = random.random()
    if random_number < 0.5:
        print(random_number)
        #menambahkan satu kali penghitung
        count += 1
    print("selesai")