mahasiswa = {
    "27102005": "nabila",
    "11700858": "faylaka",
    "71427107": "fikri"
}

nilai = {
    "27102005": [80, 78, 80, 79],
    "11700858": [80, 85, 90, 97],
    "71427107": [88, 94, 87, 80]
}

rata_mahasiswa = {}

for nim in nilai:
    rata = sum(nilai[nim]) / len(nilai[nim])
    rata_mahasiswa[nim] = rata

nim_terbaik = max(rata_mahasiswa, key=rata_mahasiswa.get)

print("Mahasiswa Terpintar :")
print("nim   :", nim_terbaik)
print("nama  :", mahasiswa[nim_terbaik])
print("nilai :", round(rata_mahasiswa[nim_terbaik], 2))


jumlah_mk = len(next(iter(nilai.values())))

rata_mk = []

for i in range(jumlah_mk):
    total = 0
    for nim in nilai:
        total += nilai[nim][i]
    rata = total / len(nilai)
    rata_mk.append(rata)

mk_terkecil = rata_mk.index(min(rata_mk))

print("\nMata Kuliah Nilai Terkecil :")
print("mk", mk_terkecil + 1)
print("Nilai :", round(rata_mk[mk_terkecil], 2))