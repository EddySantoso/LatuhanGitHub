# # z = ''
# # for i in range(0,10) :   #0,1,2,3,....,9 --> 10 kali looping
# #     for j in range (0,21): #0,1,2,3,....,20 --> 20 kali looping
# #         if j >= 10-i and j <= 10 + i :   # j>= 8 dan j<= 12 -> 8,9,10,11 
# #             z += ' * '
# #         # bikin spasi
# #         else :
# #             z += '   '
# #     z += '\n'
# # print(z)


# #soal nomor 4
# # z = ''
# # for i in range(10,-1,-1)
# #    for j in range (0,21): #0,1,2,3,....,20 --> 20 kali looping
# #         if j >= 10-i and j <= 10 + i :   # j>= 8 dan j<= 12 -> 8,9,10,11 
# #             z += ' * '
# #         # bikin spasi
# #         else :
# #             z += '   '
# #     z += '\n'
# # print(z)

# # soal nomor 5
# # z = ''
# # for i in range(0,11) :   #0,1,2,3,....,9 --> 10 kali looping
# #     if i < 10 :
# #         for j in range (0,21): #0,1,2,3,....,20 --> 20 kali looping
# #             if j >= 10-i and j <= 10 + i :   # j>= 8 dan j<= 12 -> 8,9,10,11 
# #                 z += ' * '
# #             # bikin spasi
# #             else :
# #                 z += '   '
# #         z += '\n'
# #     else :
# #         for i in range(10,-1,-1):
# #             for j in range (0,21): #0,1,2,3,....,20 --> 20 kali looping
# #                 if j >= 10-i and j <= 10 + i :   # j>= 8 dan j<= 12 -> 8,9,10,11 
# #                     z += ' * '
# #                 # bikin spasi
# #                 else :
# #                     z += '   '
# #             z += '\n'
# # print(z)
# #pertanyaan mentoring: bagaimana membuat persis seperti nomor 5

# # soal no 6

# # inputan : 'NikiZefanya'

# def duplicate_string(text):
#     out = ''
#     lower = text.lower()
#     for i in range (len(lower)):
#         for j in range (i+2):
#             out += lower[i]
#     print(out)

# duplicate_string('NikiZefanya')

# def duplicate_string(text):
#     out = ''
# #     lower = text.upper()
# #     for i in range (len(lower)):
# #         for j in range (i+1):
# #             out += lower[i]
# #     print(out)

# # duplicate_string('NikiZefanya')
# # duplicate_string('EddySantosohp')

# # a = [6,4,7,8,4,2,2,1,5,6,7]

# # def sort_ascending(list_angka):
# #     for i in range(len(list_angka)):
# #         for j in range(i+1,len(list_angka)):
# #             if list_angka[i] > list_angka[j]:
# #                 list_angka[i], list_angka[j] = list_angka[j], list_angka[i]
# #     return list_angka
# # # TANYA MASALAH PRINT DAN RETURN DI LIST_ANGKA
# # print(sort_ascending(a))

# # def sort_descending(list_angka):
# #     for i in range(len(list_angka)):
# #         for j in range(i+1,len(list_angka)):
# #             if list_angka[i] < list_angka[j]:
# #                 list_angka[i], list_angka[j] = list_angka[j], list_angka[i]
# #     return list_angka
# # # TANYA MASALAH PRINT DAN RETURN DI LIST_ANGKA
# # print(sort_descending(a))

# # def mysorted(list_angka,sortedby='asc'):
# #     for i in range(len(list_angka)):
# #         for j in range(i+1,len(list_angka)):
# #             if  sortedby == 'asc':
# #                 if list_angka[i] > list_angka[j]:
# #                     list_angka[i], list_angka[j] = list_angka[j], list_angka[i]
# #             elif  sortedby == 'desc':
# #                 if list_angka[i] < list_angka[j]:
# #                     list_angka[i], list_angka[j] = list_angka[j], list_angka[i]
# #     return list_angka

# # print(mysorted(a,sortedby='asc'))
# # print(mysorted(a,sortedby='desc'))


# # # FUNCTION
# # # formula 
# # # def namafucntion(parameter,parameter,parameter)
# #         #code


# def remove_character(text,remove):
#     rmv = text.replace(remove,'')
#     return rmv
# print(remove_character('Eddy','d'))

# def remove_character2(text,remove):
#     rmv = text.replace(remove[0],'')
#     rmv1 = rmv.replace(remove[1],'')
#     rmv2 = rmv1.replace(remove[2],'')
#     return rmv2
# print(remove_character2('eddysantoso',['s','o','e']))

# # mainsuit('gunting','batu') jika 

# def mainSuit(player1,player2):
#     if player1 == player2:
#         print('Hasilnya Draw')
#     elif player1 == 'Kertas':
#         if player2 == 'Gunting':
#             print(f'Player 1 memilih {player1}, dan player 2 memilih {player2}, Player 1 Menang!')
#         elif player2 == 'Batu':
#             print(f'Player 1 memilih {player1}, dan player 2 memilih {player2}, Player 2 MEnang!')
#     elif player1 == 'Gunting':
#         if player2 == 'Kertas':    
#             print(f'Player 1 memilih {player1}, dan player 2 memilih {player2}, Player 1 Menang!')
# print(mainSuit('Gunting', 'Kertas'))

# buah_buah = ['Jeruk', 'Apel', 'Mangga','Pear', 'Semangka', 'Jambu' ]
# print(type(buah_buah))
# print(buah_buah[1])
# print(buah_buah[2])
# print(buah_buah[:])
# print(buah_buah[3:])


# buah_buah = ['jeruk', 'apel',['apel merah','apel hijau'], 'semangka',['semangka berbiji', ['semangka merah', 'semangka kuning']],['jambu']]
#  #tanya soal index di list dalam list
# print(buah_buah[4][0])

# #list
# ## append, pop, insert

buah_buah = ['Jeruk', 'Apel', 'Mangga','Pear', 'Semangka', 'Jambu' ]
print(buah_buah.append('Duren'))
# print(buah_buah)
# # # Pop = Remove value in the list
# buah_buah.pop(3)
# print(buah_buah)
# #insert = Adding value with index
# buah_buah.insert(3,'Kurma')
# print(buah_buah)
# # Copy = Copy list
# x = buah_buah.copy

# merk_mobil = ['Honda', ['Sedan', ['accord', 'City']], ['MiniBus'['CRV', 'Jazz']], 'Toyota', ['Sedan', ['Vios']], ['Minibus', ['Avanza', 'Alphard']]]
# print(merk_mobil[0])
