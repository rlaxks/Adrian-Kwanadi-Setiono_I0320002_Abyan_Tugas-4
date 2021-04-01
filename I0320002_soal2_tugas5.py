#menginput nama dan nilai

nama = input("Masukkan nama Anda: ")
nilai = float(input("Masukkan nilai Anda: "))

#menginput grading

grading_1 = "E"
grading_2 = "C"
grading_3 = "C+"
grading_4 = "B"
grading_5 = "B+"
grading_6 = "A"
grading_7 = "A+"

if nilai < 60:
    print("Halo,", nama, "!", "Nilai Anda setelah dikonversi adalah", grading_1)
elif 60 <= nilai < 65:
    print("Halo,", nama, "!", "Nilai Anda setelah dikonversi adalah", grading_2)
elif 65 <= nilai < 70:
    print("Halo,", nama, "!", "Nilai Anda setelah dikonversi adalah", grading_3)
elif 70 <= nilai < 75:
    print("Halo,", nama, "!", "Nilai Anda setelah dikonversi adalah", grading_4)
elif 75 <= nilai < 80:
    print("Halo,", nama, "!", "Nilai Anda setelah dikonversi adalah", grading_5)
elif 80 <= nilai < 85:
    print("Halo,", nama, "!", "Nilai Anda setelah dikonversi adalah", grading_6)
elif 85 <= nilai <= 100:
    print("Halo,", nama, "!", "Nilai Anda setelah dikonversi adalah", grading_7)
else:
    print("Tidak Valid")