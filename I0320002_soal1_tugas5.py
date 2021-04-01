#menginput nama dan jenis kelamin

nama = input("Masukkan nama Anda: ")
jenis_kelamin = input("Masukkan jenis kelamin Anda: ")

if jenis_kelamin == "Perempuan" or "P":
    print("Selamat datang, Tuan", nama + "!")
elif jenis_kelamin == "Laki-laki" or "L":
    print("Selamat datang, Nyonya", nama + "!")
else:
    print("Tidak Terdaftar")