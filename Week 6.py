# a=1
# while (a<=10):
#     b=1
#     while (b<=10):
#         print(a*b, end=' ')
#         b+=1
#     print()
#     a+=1


# for i in range (2, 10, 3):
#     print (i)

print('')
print('tugas nomor 1')
print('')

numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 
 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390,
 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 
 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 
 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 
 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 
 380, 126, 721, 328, 753, 470, 743, 527]
a = 0
b = 553
while a < len(numbers):
    if numbers [a] % 2 != 0 and numbers[a] <= b:
        print(numbers[a], end=' ')
    a+=1

print('')
print('tugas nomor 2')
print('')

hasil = 0
for i in range(1, 20, 2):
    hasil += i
    print(i,end=(' + '))
print('=', hasil)
print('1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19=', hasil)

print('')
print('tugas nomor 3')
print('')

value= int(input('masukan jumlah baris: '))
for a in range (value):
    for b in range(a+1):
        print(' *', end='')
    print()

# i = 0
# while i < len(numbers):
#     if numbers[i] == 553:
#         break
#     if numbers[i] % 2 == 1:
#         print(numbers[i])
#     i+=1

# jumlah_baris = int(input("Masukkan jumlah baris: "))

# for baris in range(1, jumlah_baris + 1):
#     for bintang in range(baris):
#         print("*", end="")
#     print()