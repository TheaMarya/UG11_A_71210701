def hitungKata():
    kataInput = input('Masukkan sebuah kalimat/kata :')
    kataDihitung = input('Masukkan kata yang ingin di hitung :')
    total = kataInput.count(kataDihitung)
    print('Terdapat sebanyak',total,'kata',kataDihitung,'di dalam kalimat')

def ubahKata():
    kataInput = input('Masukkan sebuah kalimat/kata :')
    kataDiganti = input('Masukkan kata yang ingin di ubah :')
    kataPengganti = input('Masukkan kata pengganti :')
    hasil = kataInput.replace(kataDiganti,kataPengganti)
    print('String berhasil diubah menjadi :',hasil)

print('====== Program Manipulasi String ======')
print('Pilihan Menu :')
print('1. Hitung Kata')
print('2. UIbah Kata')
pilihan = int(input('Pilihan anda :'))

if pilihan == 1:
    hitungKata()
elif pilihan == 2:
    ubahKata()
else :
    print('Pilihan yang anda input tidak terdaftar di daftar nilai')