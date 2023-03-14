def cetak_papan (papan):
    #Fungsi yang mencetak papan permainan
    print("-------------")
    print("|", papan[0], "|", papan [1], "|", papan [2],"|")
    print("-------------")
    print("|", papan[3], "|", papan [4], "|", papan [5],"|")
    print("-------------")
    print("|", papan[6], "|", papan [7], "|", papan [8],"|")
    print("-------------")

def pemenang (papan, pemain):
    #Kondisi yang memeriksa pemenang dari horizontal, vertikal, dan diagonal
    menang = False
    if ((papan[0] == pemain and papan[1] == pemain and papan[2] == pemain) or
        (papan[3] == pemain and papan[4] == pemain and papan[5] == pemain) or
        (papan[6] == pemain and papan[7] == pemain and papan[8] == pemain) or
        #vertical check
        (papan[0] == pemain and papan[3] == pemain and papan[6] == pemain) or
        (papan[2] == pemain and papan[5] == pemain and papan[8] == pemain) or
        #diagonal check
        (papan[0] == pemain and papan[4] == pemain and papan[8] == pemain) or
        (papan[2] == pemain and papan[4] == pemain and papan[6] == pemain)):
        menang = True
    return menang

def main ():
    #Fungsi utama yang mengatur jalannya permainan
    papan = ["a","b","c","4","5","6","7","8","9"]
    pemain_awal = "X"
    akhir_game = False
    
    #Perulangan untuk mencari siapa pemenang
    while not akhir_game:
        cetak_papan(papan)
        print ("Sekarang giliran " + pemain_awal + " bermain")
        giliran = input("Masukkan angka 1-9: ")
        
        #perulangan input yang dimasukkan oleh user harus 1-9
        while giliran not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or papan[int(giliran)-1] in ['X', 'O']:
            giliran= input("Angka tidak valid, masukkan angka 1-9: ")

        papan [int(giliran)-1] = pemain_awal #kondisi yang menggantikan angka inputan user menjadi "X" atau "O"

        if pemenang(papan, pemain_awal):
            cetak_papan(papan)
            print(pemain_awal + " menang!")
            akhir_game = True
        
        elif all (x in ['X', 'O'] for x in papan): #kondisi untuk mengecek tie apabila tidak ada pemenang
            cetak_papan(papan)
            print("It's a tie!")
            akhir_game =True

        else:
            #kondisi yang merubah pemain dari X menjadi O
            pemain_awal = 'O' if pemain_awal == 'X' else 'X'
    
if __name__ == '__main__': #konstruksi yang menjalankan fungsi utama
    main()
