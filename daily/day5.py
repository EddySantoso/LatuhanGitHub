# contoh segitiga
#  *  *  *  *  *
#  *  *  *  *
#  *  *  *
#  *  *
#  *
#  *  *
#  *  *  *
#  *  *  *  *
#  *  *  *  *  *
# z = ''
# for i in range (5,0,-1):
#     if i > 1 :
#         for j in range (0,i):
#             z += ' * '
#         z += '\n'
#     elif i == 1 :
#         for k in range(0,5):
#             for i in range (0,k+1):
#                 z += ' * '
#             if k == 4 :
#                 break
#             z += '\n'
# print(z)
# ------------------------------ * ------------------------------
# --------------------------- *  *  * ---------------------------
# ------------------------ *  *  *  *  * ------------------------
# --------------------- *  *  *  *  *  *  * ---------------------
# ------------------ *  *  *  *  *  *  *  *  * ------------------
# --------------- *  *  *  *  *  *  *  *  *  *  * ---------------
# ------------ *  *  *  *  *  *  *  *  *  *  *  *  * ------------
# --------- *  *  *  *  *  *  *  *  *  *  *  *  *  *  * ---------
# ------ *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * ------
# --- *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * ---
z = ''
for i in range(0,10) :   #0,1,2,3,....,9 --> 10 kali looping
    for j in range (0,21): #0,1,2,3,....,20 --> 20 kali looping
        if j >= 10-i and j <= 10 + i :   # j>= 8 dan j<= 12 -> 8,9,10,11 
            z += ' * '
        # bikin spasi
        else :
            z += '   '
    z += '\n'
print(z)
# for i in range(0,10):
#     for k in range (0,21):
#         if k >= 1+ 10 and k <= 10 + i :
#              z += ' * '
#         else :
#             z += '   '
# print(z)

#pertanyaan mentoring
# kenapa tidak beraturan segitiga sama kaki yg saya cobain
# apakah segitiga belah ketupat logikanya sama dengan segitiga bayangan


## function