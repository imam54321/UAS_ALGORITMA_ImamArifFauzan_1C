data =  []

while True:
    mahasiswa = input('Masukan Nama Mahasiswa : ')
    nim = int(input('Masukan NIM Mahasiswa : '))

    data.append(mahasiswa, nim) 
    tanya = input('Apakah ingin menambahkan y/n? :')
    if tanya == "n" :
        print(mahasiswa , nim)
        break


