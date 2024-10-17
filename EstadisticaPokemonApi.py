import requests

pokemon = input("Dime el nombre o número del POKEMON a buscar: ").lower()


# recogemos informacion del poken y imprimimos sus estadisticas
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
# si tiene conexion ejecuta, sino que salte error de que no hay
if response.status_code == 200:
    
    data = response.json() # convierte el json en un diccionario
    #me meto en el apartado estadisticas del pokemon, busco el valor de la estadistica y lo imprimo
    # los numeros entre corchetes son los indicices del diccionario stats
    print("Puntos de salud: ", data["stats"][0]["base_stat"])
    print("Ataque: ", data["stats"][1]["base_stat"])
    print("Defensa: ", data["stats"][2]["base_stat"])
    print("Ataque especial: ", data["stats"][3]["base_stat"])
    print("Defensa especial: ",data["stats"][4]["base_stat"])
    print("Velocidad: ",data["stats"][5]["base_stat"])

    
else:
    print(f"Error: {response.status_code}; el pokemon {pokemon} no se ha encontrado")