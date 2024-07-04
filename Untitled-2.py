LG=["Ilorin west","Ekiti","OKe-oro","Ifelodun","Barutee","Asa","Ilorin South","Kayama","Sare"]
# # LG in even position
length=len(LG)
# for i in range(length):
#     print(LG[i])
# This is mine
# for i in range(1,9,2):
#     print(LG[i])

# Another code
# for i in range(length):
#     if (i+2) % 2 == 0:
#         print(LG[i])
# Code1
# for i in range(length):
#     if i % 2 ==0:
#         print(LG[i])
# #Code2
# for i in range(0,length,2):
#     print(LG[i])  
#State that start with vowel leter
#Case1
# Vowels = 'aeiou'
# for i in range(length):
#     if LG[i][0] in 'aeiou':
#         print(LG[i])
# for i in range(0,length,1):
#     if i+1 == 2:
#       print(LG[i])
#     else:
vowels = 'AEIOU'
for i in range (length):
    if LG [i][0] in 'AEIOU':
        print(LG[i])

for lg in LG:
    if lg[0] in vowels:
        print(lg)
    



        

    

  



