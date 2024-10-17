
import json
import os

# creamos primera clase
class Usuario:
    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
    # devolvemos una representación de cadena (string) de una instancia de una clase
    def __str__(self):
        return f'Nombre: {self.nombre}, Correo: {self.correo},  Telefono: {self.telefono}'
    

#segunda clase 
class FuncionalidadUsuarios:
# inicializa una lista vacia para guardar los datos
    def __init__(self):
        self.usuarios = []
#definimos metodos 
    def anadir_usuarios(self, nombre, correo, telefono):
        nuevo_usuario = Usuario(nombre, correo, telefono)
        self.usuarios.append(nuevo_usuario)
        print(f'Usuario {nombre} agregado.')

    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                print(usuario)
                return usuario
        print(f'Usuario {nombre} no encontrado.')

    def actualizar_usuario(self, nombre):
        
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                correo=input("Introduce correo: ")
                telefono=input("Introduce telefono: ")
                FuncionalidadUsuarios.eliminar_usuario(self, nombre)
                FuncionalidadUsuarios.anadir_usuarios(self, nombre,correo,telefono)
                break
            else:
                print(f"El contacto {nombre} no existe.")

    def eliminar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                self.usuarios.remove(usuario)
                print(f'Usuario {nombre} eliminado.')
                return
        print(f'Usuario {nombre} no encontrado.')


    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:")
            for usuario in self.usuarios:
                print(usuario) 
              

# definimo 2 metodos para generar y leer json
nombre_archivo="ListaUsuarios.json"

def generar_json(nombre):
    # generar y guardar
    try:
        funcion = FuncionalidadUsuarios()
        usuarios=funcion.buscar_usuario(nombre)
        
        lista_datos=[] # inicializamos una lista vacia
        for usuario in usuarios:
            datos = {

                    "Nombre": usuario.nombre,
                    "Correo": usuario.correo,
                    "Telefono": usuario.telefono
            }
            lista_datos.append(datos) # guardamos todos los usuarios
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(lista_datos, f, ensure_ascii=False, indent=4)
        print(f'Archivo {nombre_archivo} generado con éxito.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')


def leer_json():        
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as json_data:
            lista_usuarios=json.load(json_data)
        for usuario in lista_usuarios:    
            datos = {
                "Nombre": usuario["nombre"],
                "Correo": usuario["correo"],
                "Telefono": usuario["telefono"]
            }
        print(datos.__dict__)
    except Exception as e:
        print(f'Ocurrió un error: {e}')

   

# Ejecutamos aplicacion main
def mi_aplicacion():
    funcion = FuncionalidadUsuarios()
    
    while True:
        print("\nOpciones:")
        print("1. Anadir usuario")
        print("2. Consultar usuario")
        print("3. Actualizar usuario")
        print("4. Borrar usuario")
        print("5. Mostrar todos los usuarios")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                while True:
                    nombre = input("Introduce el nombre del usuario: ", lambda n: n.strip() != "")
                    if nombre:
                        break
                    print("El nombre no puede estar vacío.")
                #esta funcion lambda sirve para quitar espacios al principio y al final del string
                while True:
                    correo = input("Introduce el correo del usuario: ", lambda n: n.strip() != "")
                    if correo:
                        break
                    print("El correo no puede estar vacio")

                while True:  
                    #recogemos el numero como si fuera un string para despues poder usar el metodo isdigit()   
                    telefono = input("Ingrese telefono del usuario(max 9 digitos): ")
                    if telefono.isdigit() and 0 < len(telefono) <= 9: 
                        print("Numero correcto")
                        break
                    else:
                        print("Debes introducir un número de teléfono válido de máximo 9 dígitos.")
                funcion.anadir_usuarios(nombre, correo, telefono)
                generar_json(nombre)
                leer_json() 
            case "2":
                nombre = input("Ingrese el nombre del usuario a buscar: ")
                funcion.buscar_usuario(nombre)
            case "3":
                nombre = input("Ingrese el nombre del usuario a actualizar: ")
                funcion.actualizar_usuario(nombre)    
            case "4":
                nombre = input("Ingrese el nombre del usuario a eliminar: ")
                funcion.eliminar_usuario(nombre)
            case "5":
                funcion.mostrar_usuarios()
            case "6":
                print("Saliendo del programa.")
                break    
            case _:
                print("Opción no válida. Intente de nuevo.")


mi_aplicacion()






