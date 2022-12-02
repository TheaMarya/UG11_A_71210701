def cetakHuruf():
    kataInput = input('masukkan kata :')
    x = len(kataInput)
    if x %2 ==0:
        kanan = kataInput[-3::]
        kiri = kataInput[0:3]
        print('Huruf yang diambil pada kata', kataInput, 'adalah',kiri,'dan',kanan)
    
    elif x%2 ==1:
        y = x//2
        kata = (kataInput[y-1:y+2])
        print('Huruf yang diambil pada kata',kataInput,'adalah',kata)

cetakHuruf()