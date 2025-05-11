tiket_tujuan = (input("Masukan tiket tujuan yang ingin dipesan: "))
jumlah_tiket = int(input("Masukan tiket yang ingin dipesan: "))

surbaya    = 50000
malang     = 60000
bali       = 90000
yogyakarta = 90000
solo       = 80000

sby = jumlah_tiket * surbaya
mlg = jumlah_tiket * malang
bal = jumlah_tiket * bali
yog = jumlah_tiket * yogyakarta
sol = jumlah_tiket * solo

sby2 = sby - (sby * (10/100))
mlg2 = mlg - (mlg * (10/100))
bal2 = bal - (bal * (15/100))
yog2 = yog - (yog * (5/100))
sol2 = sol - (sol * (5/100))

if tiket_tujuan == "surabaya" :  
    if sby >= 300000 and sby < 600000 :
        print ("harga tiket ke surabaya yang anda dapat adalah Rp",sby2)
    elif sby >= 600000 :
        print ("harga tiket ke surabaya yang anda dapat adalah Rp",sby2 - (sby2 * 10/100))
    else :
        print ("harga tiket ke surabaya yang anda dapat adalah Rp",sby)
elif tiket_tujuan == "malang" :
    if mlg >= 300000 and mlg < 600000 :
        print ("harga tiket ke malang yang anda dapat adalah Rp",mlg2)
    elif mlg >= 600000 :
        print ("harga tiket ke malang yang anda dapat adalah Rp",mlg2 - (mlg2 * 10/100))
    else :
        print ("harga tiket ke malang yang anda dapat adalah Rp",mlg)    
elif tiket_tujuan == "bali" :
    if bal >= 450000 and bal < 900000 :
        print ("harga tiket ke bali yang anda dapat adalah Rp",bal2)
    elif bal >= 900000 :
        print ("harga tiket ke bali yang anda dapat adalah Rp",bal2 - (bal2 * 10/100))
    else :
        print ("harga tiket ke bali yang anda dapat adalah Rp",bal)
elif tiket_tujuan == "yogyakarta" :
    if yog >= 250000 and yog < 500000 :
        print ("harga tiket ke yogyakarta yang anda dapat adalah Rp",yog2)
    elif yog >= 500000 :
        print ("harga tiket ke yogyakarta yang anda dapat adalah Rp",yog2 - (yog2 * 10/100))
    else :
        print ("harga tiket ke yogyakarta yang anda dapat adalah Rp",yog)
elif tiket_tujuan == "solo" :
    if sol >= 250000 and yog < 500000 :
        print ("harga tiket ke solo yang anda dapat adalah Rp",sol2)
    elif sol >= 500000 :
        print ("harga tiket ke solo yang anda dapat adalah Rp",sol2 - (sol2 * 10/100))
    else :
        print ("harga tiket ke solo yang anda dapat adalah Rp",sol)
