#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Silvanna Zharay Olaya Mantilla"
edad = 14
estatura = 1.60
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = (" _silvanna_15")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "atrapado", "artista": "anuel", "duracion": "3:06"},
{"titulo": "la boda", "artista": "Cosculluela", "duracion": "5:52"},
{"titulo": "tendencia global", "artista": "Bless", "duracion": "3:54"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
