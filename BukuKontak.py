if __name__ == '__main__':
    # Variable dengan tipe data dictionary
    kontak = dict()

    while True:
        print('BUKU KONTAK')
        print('1. Tambah Kontak')
        print('2. Update Kontak')
        print('3. Pencarian Sederhana')
        print('4. Pencarian Kompleks')
        print('5. Daftar Kontak')  # Opsi untuk melihat daftar kontak
        print('0. Berhenti')
        pilihan = int(input('Masukkan Pilihan : '))

        if pilihan == 0:
            print('Program dihentikan...')
            break
        elif pilihan == 1:
            print('Tambah Kontak Baru')
            nomor = input('Masukkan Nomor : ')
            if not nomor in kontak:
                nama = input('Masukkan Nama : ')
                kontak[nomor] = nama
                print('Tambah kontak berhasil')
            else:
                print('Tambah kontak gagal, nomor sudah terdaftar')
        elif pilihan == 2:
            print('Update Kontak')
            nomor = input('Masukkan Nomor : ')
            if nomor in kontak:
                print('\nData Kontak :\nNama :', kontak[nomor],'\nNomor :', nomor)
                print('\nPilih Update')
                print('1. Update Nama')
                print('2. Update Nomor')
                print('3. Update Nama dan Nomor')
                print('4. Batal Update')
                pilihan = int(input('Masukkan Pilihan : '))

                if pilihan == 1:
                    nama = input('Masukkan Nama : ')
                    kontak[nomor] = nama  # Update nama
                    print('Update berhasil')
                elif pilihan == 2:
                    nomorBaru = input('Masukkan Nomor Baru : ')
                    if not nomorBaru in kontak:
                        nama = kontak[nomor]  # Simpan nama sebelum dihapus
                        del kontak[nomor]
                        kontak[nomorBaru] = nama  # Simpan nomor baru
                        print('Update berhasil')
                    else:
                        print('Gagal update, karena nomor baru yang dimasukkan sudah terdaftar')
                elif pilihan == 3:
                    nomorBaru = input('Masukkan Nomor Baru : ')
                    if not nomorBaru in kontak:
                        del kontak[nomor]
                        nama = input('Masukkan Nama : ')
                        kontak[nomorBaru] = nama
                        print('Update berhasil')
                    else:
                        print('Gagal update, karena nomor baru yang dimasukkan sudah terdaftar')
                elif pilihan == 4:
                    print('Update dibatalkan')
                else:
                    print('Pilihan Tidak Valid, Gagal Update')
            else:
                print('Nomor Belum Terdaftar')
        elif pilihan == 3:
            print('Pencarian Sederhana')
            nama = input('Masukkan Nama : ')

            hasil = ""
            for key, value in kontak.items():
                if value == nama:
                    if hasil == "":
                        hasil = nama + " - " + key
                    else:
                        hasil += "\n" + nama + " - " + key

            if hasil != "":
                print('Hasil Pencarian :')
                print(hasil)
            else:
                print('Tidak ada', nama, 'di buku kontak')
        elif pilihan == 4:
            print('Pencarian Kompleks')
            nama = input('Masukkan Nama : ')

            hasil = ""
            for key, value in kontak.items():
                if nama in value:
                    if hasil == "":
                        hasil = value + " - " + key
                    else:
                        hasil += "\n" + value + " - " + key

            if hasil != "":
                print('Hasil Pencarian :')
                print(hasil)
            else:
                print('Tidak ada nama dengan prefiks', nama, 'di buku kontak')
        elif pilihan == 5:
            print('Daftar Kontak:')
            if not kontak:
                print('Tidak ada kontak yang tersimpan.')
            else:
                for nomor, nama in kontak.items():
                    print(f'Nama: {nama}, Nomor: {nomor}')
        else:
            print('Pilihan Tidak Valid')
        print()
