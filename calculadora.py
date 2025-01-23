def suma(a, b):
  return a + b

def resta(a, b):
  return a - b

def multiplicacion(a, b):
  return a * b

def division(a, b):
  if b != 0:
    return a / b
  else:
    return "Error: División entre cero no permitida"

def main():
  print("Bienvenido a la calculadora")
  print("Opciones:")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")
  
  opcion = input("Selecciona una opción (1/2/3/4): ")
  
  if opcion in ['1', '2', '3', '4']:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    if opcion == '1':
      print(f"El resultado de la suma es: {suma(num1, num2)}")
    elif opcion == '2':
      print(f"El resultado de la resta es: {resta(num1, num2)}")
    elif opcion == '3':
      print(f"El resultado de la multiplicación es: {multiplicacion(num1, num2)}")
    elif opcion == '4':
      print(f"El resultado de la división es: {division(num1, num2)}")
  else:
    print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")

if __name__ == "__main__":
  main()
