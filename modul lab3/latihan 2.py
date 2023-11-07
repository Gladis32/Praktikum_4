#menampilkan bilangan terbesar dari n buah data yang diinputkan 
max_number = None
while True:
    input_number = int(input("masukkan angka (0 untuk berhenti): "))
    if input_number == 0:
        break
 #periksa apakah saat ini lebih besar dari yang sebelumnya
    if max_number is None or input_number > max_number:
        max_number = input_number

if max_number is not None:
    print("bilangan terbesar adalah:", max_number)
else:
    print("tidak ada bilangan yang dimasukkan.")