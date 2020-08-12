# # variabel

# # name = "eddy" #string
# # tanggal_lahir = 29 #interger
# # married = False # Boolean
# # berat_badan = 65 # float

# # # Ini adalah fungsi untuk mencetak dan memunculkan apapun yang dimasukan ke dalam fungsi print
# # print(married) 
# # print(type(married))
# # print(name)
# # print(type(name))
# # print(tanggal_lahir)
# # print(type(tanggal_lahir))
# # print(berat_badan)
# # print(type(berat_badan))

# # operasi matematika
# # +, -, *, / , %


# angka_1 = 5
# angka_2 = 10
# angka_3 = "5"
# angka_4 = "10"

# x = angka_3+angka_4

# print(angka_1+angka_2) 
# print(angka_3+angka_4)
# print(type(x)) 
# print(angka_1 - angka_2)

# # interger
# print('Hasil interger')
# print(angka_1+int(angka_3))
# # string
# print('Hasil string')
# print(str(angka_1)+angka_3)

# # perkalian
# print(angka_1*angka_3)
# print(angka_2*angka_1)

# # pembagian
# print(angka_1/angka_2)

# # Modulus (sisa hasil bagi dari pembagian)
# print(angka_2%angka_1)


# # Input

# name = input('Masukan Nama Anda : ')
# age = input('Masukan Umur Anda : ')
# Sex = input('Laki-laki/Perempuan : ')
# Position = input('Masukan Posisi Anda : ')
# Overall = input('Masukan Status Anda : ')

# # print('Nama Saya'  + name +', '+' umur saya ' + age + ' tahun '+' saya adalah '+ Sex +' posisi saya '+ Position +' dan status saya '+ Overall)
# print(f'Nama saya {name}, umur saya {age}, saya adalah {Sex}, posisi saya {Position} Stats saya {Overall}')

# print('Name =' + name)
# print('age = ' +age)
# print('sex = ' +Sex)
# print('Position = ' +Position)
# print('Overall = ' +Overall)

# # Function Math in Python
# # ceil, pow, sqrt, round

# import math

# # pembulatan ke atas untuk angka desimal
# x = 5.3
# print('Function Ceil from Math')
# print(math.ceil(x))
# # pembulatan kebawah untuk angka desimal
# x = 5.7
# print('Function Floor from Math')
# print(math.floor(x))

# # # pemangkatan angka
# x = 6 
# # print('Fucntion Pow from Math')
# print(math.pow(7,2))

# # Pengakaran akar
# x = 49
# print('Function sqrt from Math')
# print(math.sqrt(x))

# # Function round (pembulatan otomatis angka desimal)
# x = 5.3
# y = 5.7
# print(round(x))
# print(round(y))




# # # import math

# # # #



# # # string

# # # nama = 'eddy santoso'

# # # # hitung karakter termasuk spasi
# # # print(len(nama))
# # # # lower case  untuk string
# # # print(nama.lower(x))
# # #


# # Split function untuk membagi string menjadi sebuah list
# ## In case split berdasarakan spasi dari string nama
# # # print(nama.split(''))

# nama = 'marion jola'
# # # akan menjadi sebuah list
# list_nama = nama.split('nama')
# print(list_nama)
# nama_bersatu = list_nama[0] + list_nama[1]
# print(len(nama_bersatu))


#print(len(nama.split('nama')[0] + nama.split('nama')[1]))

# # string indexing
# # nama = 'anugrah!anugrah#nurhamid'
# # print(nama[7:])
# # print(nama[7])
# # print(nama[8:15])
# # print(nama[8:15])
# # print(nama[:15])
# # print(nama.split('!'))

# # String Quotes
# # singleQuotes = 'ini adalah single quotes'
# # doubleQuotes = "ini adalah double quotes"
# # combineQuotes = "Let's go to school"

# # print(singleQuotes)
# # print(doubleQuotes)
# # print(combineQuotes)

# # soal




#Input Number with arit opr.
# angka_1 = input('Masukan angka pertama : ')
# angka_2 = input('Masukan angka kedua :')
# pertambahan = int(angka_1) + int(angka_2)
# pengurangan = int(angka_1) - int(angka_2)
# pembagian = int(angka_1) / int(angka_2)
# modulus = int(angka_1) % int(angka_2)

# print(f'penjumlahan antara angka pertama dan angka kedua adalah {pertambahan}')
# print(f'pengurangan antara angka pertama dan angka kedua adalah {pengurangan}')
# print(f'pembagian antara angka pertama dan angka kedua adalah {pembagian}')

# # soal no 1

# x = 4
# y = 3
# z = 2

# w = ((x+y*z)/(x*y))**z
# print(round(w,3))

# # soal no 2
# angka = int(input('silahkan masukan angka berapapun : '))
# print('Kuadrat dari ' + str(angka) + ' = ' + str(angka**2))

# # soal no 3

# ## total 485 hari dijadikan satu persatu ke tahun, ke bulan, ke hari
# import math
# total_hari = int(input('masukan total hari : '))
# tahun = str(math.floor(total_hari/360))
# bulan = str(math.floor(total_hari/12))
# minggu = str(math.floor(total_hari/7))
# hari = str(total_hari)

# print(f'Hasilnya adalah {tahun} tahun, {bulan} bulan, {minggu} minggu, {hari} hari' )











import math
total_hari = int(input('Masukan Jumlah hari : '))
tahun = str(math.floor(total_hari/360))
bulan = str(math.floor((total_hari % 360)/30))
minggu = str(math.floor(((total_hari % 360)% 30) /7))
hari = str((math.floor(total_hari % 360) % 30) % 7)

print(f'Hasilnya adalah {tahun} tahun, {bulan} bulan, {minggu} minggu, {hari} hari' )



x= 'eddy'



















