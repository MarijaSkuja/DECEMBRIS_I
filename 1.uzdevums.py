# Lietotājs ievada skaitli
ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

# Inicializē saskaitīšanas summu
saskaitisana = 0

# Izmanto for ciklu, lai saskaitītu no 13 līdz ievadītajam skaitlim
for skaitlis in range(13, ievaditais_skaitlis + 1):
    saskaitisana += skaitlis

# Izvada rezultātu
print(f"Saskaitīšanas rezultāts no 13 līdz {ievaditais_skaitlis} ir: {saskaitisana}")
