user ={} #Variable dictionary yang menampung nilai username dan value password

def registrasi (): #fungsi untuk registrasi
    nama = input ('Masukkan Nama: ')
    password = input ('Masukkan Password:')
    user [nama] = password #Variable yang memberikan tampungan nilai username dan password kepada user
    print ('Registrasi telah selesai!')

def login (): #Fungsi untuk login
    username = input ('Masukkan Nama: ')
    password1 = input ('Masukkan Password: ')

    #kondisi pengecekkan username dan password sesuai yang di input pada registrasi
    if username in user and user[username] == password1 : 
        print ('Login anda telah berhasil')
    else:
        print('Data yang anda masukkan tidak terdaftar.')

while True:
    print ('Tentukan Pilihan Anda dari 1 atau 2:')
    print ('1. Registrasi')
    print ('2. Login')
    print ('3. Berhenti')

    pilihan = input ('Masukkan pilihan Anda 1/2:') #input untuk pemanggilan fungsi registrasi/login

    #kondisi yang memanggil fungsi
    if pilihan == '1':
        registrasi()
    elif pilihan == '2':
        login()
    elif pilihan == '3':
        break
    else:
        print ('Silahkan masukkan angka yang benar.')
