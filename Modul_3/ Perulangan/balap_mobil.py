kelas = str(input("Pilih kelas yang diinginkan: "))
if kelas == "kelas stock" :
    kelas_stock = 3
    total_bahan_bakar = 100
    putaran = 0
    i = 5
    while total_bahan_bakar >= 3 : 
        total_bahan_bakar -= 3
        putaran += 1
        if (putaran == 1*i):
            i += 5
            total_bahan_bakar += 5
    print("banyak putaran  yang dapat ditempuh: ",putaran)

elif kelas == "kelas semi pro" :
    kelas_semi_pro = 4
    total_bahan_bakar = 100
    putaran = 0
    i = 5
    while total_bahan_bakar >= 4: 
        total_bahan_bakar -= 4
        putaran += 1
        if (putaran == 1*i):
            i += 5
            total_bahan_bakar += 5
    print("banyak putaran  yang dapat ditempuh: ",putaran)

elif kelas == "kelas profesional" :
    kelas_profesional= 5

    total_bahan_bakar = 100
    putaran = 0
    i = 5
    while total_bahan_bakar >= 5 : 
        total_bahan_bakar -= 5
        putaran += 1
        if (putaran == 1*i):
            i += 5
            total_bahan_bakar += 5
    print("banyak putaran  yang dapat ditempuh: ",putaran)
