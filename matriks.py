def input_matriks(baris, kolom):
    matriks = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            val = int(input(f"masukkan elemen [{i+1}][{j+1}]: "))
            row.append(val)
        matriks.append(row)
    return matriks


def tampilkan(m):
    print("\nhasil:")
    for row in m:
        print(row)


def menu():
    while True:
        print("\n===> MENU LIST <===")
        print("1. penjumlahan")
        print("2. pengurangan")
        print("3. perkalian")
        print("0. keluar")

        pilihan = input("masukkan angka: ")

        if pilihan == '0':
            print("program sudah selesai")
            break

        elif pilihan in ['1', '2', '3']:
            print("\nmasukkan ukuran matriks")
            baris = int(input("Baris: "))
            kolom = int(input("Kolom: "))

            print("\nmatriks A")
            A = input_matriks(baris, kolom)

            print("\nmatriks B")
            B = input_matriks(baris, kolom)

            hasil = []

            for i in range(baris):
                row = []
                for j in range(kolom):
                    if pilihan == '1':
                        row.append(A[i][j] + B[i][j]) 
                    elif pilihan == '2':
                        row.append(A[i][j] - B[i][j])  
                    elif pilihan == '3':
                        row.append(A[i][j] * B[i][j])  
                hasil.append(row)

            tampilkan(hasil)

        else:
            print("pilihan tidak ditemukan!")


if __name__ == "__main__":
    menu()