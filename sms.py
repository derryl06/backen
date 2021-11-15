aksi = ['kirim smms', 'kirim pulsa']
tujuan = ['82264330546', '85274839847', '8238271912']
k_pulsa = [5000, 10000, 20000]
pulsa = 15000
while True:
    print('=========Mau apa ?===========')
    for i in range(0, len(aksi)):
        print(f'{i+1}, {aksi[i]} ')
    beraksi = input('pilih aksi')
    if beraksi == '1':
        for i in range(0, len(tujuan)):
            print(f'{i+1} . {tujuan[i]}')
        no = int(input('masukan tujuan'))
        pesan = input('massukann pesann')
        print(f' pesan kepada {tujuan[no-1]} telah terkirim')
        continue
    elif beraksi == '2':
        for i in range(0, len(tujuan)):
            print(f'{i+1}, {tujuan[i]}')
        no = int(input('masukan no tujuan'))
        for i in range(0, len(k_pulsa)):
            print(f'{i+1}, {k_pulsa[i]}')
        jumlah = int(input('masukan jumlah pulsa yang dikirimkan'))
        if pulsa < k_pulsa[jumlah-1]:
            print('pulsa anda kurang anjir!!')
        else:
            print('tunggu sabar lur sedang di proses...')
            break
