# Lietotājs ievada skaitli
ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

# Pārbauda, vai skaitlis ir nepāra
if ievaditais_skaitlis % 2 != 0:
    print(f"{ievaditais_skaitlis} ir nepāra skaitlis.")
else:
    print(f"{ievaditais_skaitlis} ir pāra skaitlis.")

# Pārbauda, vai skaitlis dalās ar 5 un 9
if ievaditais_skaitlis % 5 == 0 and ievaditais_skaitlis % 9 == 0:
    print(f"{ievaditais_skaitlis} dalās ar 5 un 9.")
else:
    print(f"{ievaditais_skaitlis} nedalās ar 5 un 9.")