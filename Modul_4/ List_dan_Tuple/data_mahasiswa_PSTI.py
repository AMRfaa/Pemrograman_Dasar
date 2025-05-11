mahasiswa_list = []
while True:
    nama_mahasiswa = input("Masukkan nama mahasiswa          : ")
    nim_mahasiswa  = input("Masukkan NIM mahasiswa           : ")
    tanggal_lahir  = input("Masukkan tanggal lahir mahasiswa : ")
    mahasiswa_list.append([nama_mahasiswa, nim_mahasiswa, tanggal_lahir])
    tanya          = input("Apakah ingin memasukkan data lagi? (y/n): ")
    if tanya != 'y':
        break
print()
for mahasiswa in mahasiswa_list:
    print("Nama          : ",mahasiswa[0])
    print("NIM           : ",mahasiswa[1])
    print("Tanggal Lahir : ",mahasiswa[2])
    print()
