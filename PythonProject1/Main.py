k = int(input("Wie viele Tassen Kaffee hattest du heute?"))

if 4 <= k <= 8:
    print (f"Ich hatte {k} Tassen Kaffee. Man kann mit mir sprechen.")

# das f davor ist notwendig bei dynamischen (veränderlichen) Elementen wie dem {k}

# if k <= 3:
#        print ("Ich hatte noch nicht genug Kaffee. Komm später wieder.")
#
# else:
#    print ("Ich hatte zu viel Kaffee. Mir ist schlecht.")
#
# so bezieht sich das else nur auf das if davor, man kann aber alle drei miteinander
# verknüpfen durch elif

elif k <= 3:
    print ("Ich hatte noch nicht genug Kaffee. Komm später wieder.")

else:
    print ("Ich hatte zu viel Kaffee. Mir ist schlecht.")


