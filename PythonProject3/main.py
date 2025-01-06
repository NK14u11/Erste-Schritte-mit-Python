# n = 1
#
# while n < 7:
#    print(n)
#    n = n + 1
# else:
#    print("fertig")

n = 1
r = 4
while n < 4:
    r = r - 1
    print(f"Dies ist die {n}. Tasse Kaffee. In der Maschine verbleiben noch {r} Portionen.")
    n = n + 1
else:
    print(f"Dies ist die {n}. Tasse Kaffee. Die Maschine ist nun leer. Bitte Kaffee auffüllen.")