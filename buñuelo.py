def aguacate():
  caracter = input("Ingrese un carácter: ")
  byte = ord(caracter)
  print(f"La representación en byte de '{caracter}' es: {bin(byte)[2:]:>08}")

def pandebono():
  palabra = input("Ingrese una palabra: ")
  bytes_palabra = ' '.join([bin(ord(caracter))[2:].zfill(8) for caracter in palabra])
  print(f"La representación en byte de '{palabra}' es: {bytes_palabra}")

def menu():
  while True:
      print("\nMenú:")
      print("1. Generar la representación en byte de un carácter")
      print("2. Generar la representación en byte de una palabra")
      print("0. Salir del programa")

      opcion = input("Seleccione una opción (0-2): ")

      if opcion == '1':
          aguacate()
      elif opcion == '2':
          pandebono()
      elif opcion == '0':
          print("Saliendo del programa. ¡Hasta luego!")
          break
      else:
          print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
  menu()
