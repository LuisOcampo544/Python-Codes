n1 = int(input('Ingresa tu calificación -->'))

if n1 > 100:
    print('Calificación no valida')
elif n1 == 100:
    print('Excelente, felicidades')
elif n1 <= 99 & n1 >= 90:
    print('Muy bien')
elif n1 <= 89 & n1 >= 80:
    print('Bien')
elif n1 <= 79 & n1 >= 70:
    print('Alumno regular')
else:
    print('Alumno no aprobado')