def tampil_kontak(list_kontak):
    for kontak in list_kontak:
        print("====================")
        print(f"Nama : {kontak['Nama']}")
        print(f"Email : {kontak['Email']}")
        print(f"Nomor : {kontak['Nomor']}")


def baru_kontak():
    nama = input("Nama: ")
    email = input("Email: ")
    nomor = input("Nomor: ")
    kontak = {
        "Nama": nama,
        "Email": email,
        "Nomor": nomor
    }
    return kontak


def hapus_kontak(list_kontak):
    nomor = input("No telepon yang akan dihapus: ")

    index = -1

    for i in range(0, len(list_kontak)):
        kontak = list_kontak[i]
        if nomor == kontak["Nomor"]:
            index = 1
            break

    if index == -1:
        print("sorry bro ga ketemu")
    else:
        del list_kontak[index]
        print('yeayyy berhasil di hapus')


def cari_kontak(list_kontak):
    nama_dicari = input("nama yang anda cari: ")

    for kontak in list_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_dicari.lower()) != -1:
            print("===================")
            print(f"Nama : {kontak['Nama']}")
            print(f"Email : {kontak['Email']}")
            print(f"Nomor : {kontak['Nomor']}")
