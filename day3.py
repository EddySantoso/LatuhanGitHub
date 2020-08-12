# soal nomor 1
# import math
# input_number = int(input('Masukan angka : '))
# print(input_number % 100 * 100 + input_number // 100)

# soal nomor 2
# from math import pi
# r = float(input("input the radius of the circle : "))
# formula = pi * r**2
# print("The area of the circle with radius " + str(r) + ' is ' + str(formula))

# Soal nomor 3
# x = int(input("Input first number (2 digit): "))
# y = int(input("Input second number (2 digit): "))

# a = x // 10 # ambil angka awal di 2 angka pertama
# b = x % 10 # ambil angka akhir di 2 angka pertama
# c = y // 10 # ambil angka awal di 2 angka kedua
# d = y % 10 # ambil angka akhir di 2 angka kedua

# print(a*1000 + c*100 + b * 10 + d)

# Soal nomor 4
# input_kalimat = input("Input kalimat:")
# replace = input('remove word: ')
# print(input_kalimat.replace(replace,""))

# SOal nomor 5
# input_kalimat = input("Input kalimat:")
# list_kata = input_kalimat.split()
# print(list_kata[1]+ " "+list_kata[0])


# Assignment Operator
# Logical Operator
# Comparison Operator
# If Else (Conditional Expression)

# Assigment Operator
# +=, /=, -=, %=. *=
# selalu membaca variabel pertama dan di equal ke variabel

# Exp 1
# a = 8
# a += 10
# a -= 4
# a /= 7
# a *= 2
# a %= 2
# print(a)
# Exp 2
# nama = "lingard"
# nama += " wayne"
# print(nama)

# Comparison Operator
# menghasilkan true or false
## == (punya nilai yang sama dan type data sama)
## > (lebih dari)
## < (kurang dari)
## >= (lebih besar sama dengan)
## <= (kurang dari sama dengan)
## != (tidak sama dengan)

# a = 7
# b = "eddy"
# c = '8'

# print (a == b)
# print(a > int(c))
# print(a < int(c))
# print(a >= int(c))
# print(a <= int(c))
# print(a != int(c))

# Logical Operator
## and ( both fo them, if both expression true)
## or (if one of them true, result true)
## not (reverse sebuah boole True/False)
## not in (not inside in condition)
## in (inside of condition)
# Exp

# print(a == b and int(c)< 7)
# print(a == b or int(c) > a)
# print(a == b or int(c) > a > a or int(c) < a)

# Conditional Expression (If, Else, ELse if)
## kerika di execute biasanya ada sebuah conditional statement

# kerangka conditional
# if (condition A) : 
#     Syntaxx
# else if condition B:
#     syntaxx
# else : 
#     syntaxx

# if (condition A) : 
#    if condition :
#        if cpndition :
#            if condition :
#         else :

# else if condition B:
#     syntaxx
# else : 
#     syntaxx

# membuat 2 kondisi
## Exp
# a = 50

# if a > 60 :
#     print('Good')
# else : 
#     print('Bad')

# a = 70

# if a >= 70 :
#     print('Lulus')
# elif a < 70 :
#     print('Tidak Lulus')
# else :
#     print('Not Define')

# inputannya input angka pertama & angka 2
## pilih operasi +, -, /, %. *

# x = int(input('input first : '))
# y = int(input('input sec : '))
# operasi = input('Pilih Operator +, -, /, *, % ')

# if (operasi == '+') :
#     print('Hasinya adalah' + str(x + y))
# elif (operasi == '-'):
#     print(str(x - y))
# elif (operasi == '/'):
#     print(str(x / y))
# elif (operasi == '%'):
#     print(str(x % y))
# elif (operasi == '*'):
#     print(str(x * y))
# else :
#     print('Wrong')

# Soal Slide 1
# angka = input('Masukan Angka : ')

# if angka.isdigit() == True :
#     if int(angka) % 2 == 0 :
#         print(f'Angka (angka) tergolong bilangan genap!')
#     if int(angka) % 2 != 0 :
#         print(f'Angka (angka) tergolong bilangan ganjil!')
# else :
#     print('Tolong Masukan Angka')
    
    
# Soal Slide 2

import math
massa = float(input("Masukan Massa(kg) : "))
tinggi = float(input( "Masukan Tinggi(cm): "))/100
imt = round(massa / (tinggi * tinggi),2)
massa_tinggi = 'Massa ' + str(massa) + ' kg dan' + ' Tinggi ' + str(tinggi) + ' m'
hasil = ('imt anda adalah ' + str(imt) + ' Berat Badan' + ' ')

print("Penelitian IMT")

if   ( imt <= 18.5 ) :
    hasil += 'Kurang'
elif (18.5 <= imt < 25 ) :
    hasil += 'ideal'
elif (25 <= imt < 30 ) :
    hasil += 'Berlebih'
elif (30 <= imt < 40 ) :
    hasil += 'Sangat berlebih'
elif (imt >= 40 ) :
    hasil += 'Obesitas'
print(massa_tinggi)
print(hasil)

# Looping
# # While Looping
# # For Loop
# # while - > always  execute when  the condition or statement true
# ## Dont forget to give an exit way
# List , Array

# Example

# angka = 0
# while angka <= 10 :
#     print(angka)\

#     angka += 2










































































