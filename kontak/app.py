import function

list_kontak = []
list_kontak.append({
    "Nama": "Kusen",
    "Email": "kusena@gmail.com",
    "Nomor": "082264330546"

})

while True:
    print('======MENU======')
    print('1. daftar kontak')
    print('2. tambah kontak')
    print('3. hapus kontak')
    print('4. cari kontak')
    print('0. keluar program')

    menu = input('pilih menu :')
    if menu == '0':
        break
    elif menu == "1":
        function.tampil_kontak(list_kontak)
    elif menu == "2":
        kontak = function.baru_kontak()
        list_kontak.append(kontak)
    elif menu == "3":
        function.hapus_kontak(list_kontak)
    elif menu == "4":
        function.cari_kontak(list_kontak)
    else:
        print("menu tidak tersedia")
print("program telah berhenti")
