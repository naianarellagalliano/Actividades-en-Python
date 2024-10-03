calificaciones = []
while true:
    calificacion = input("Ingrese la calificacion (o 'Fin' para finalizar):")
    if calificacion() == 'Fin';
        break
    calificaciones.append(float(calificacion))
    calificaciones.sort()
    print("Califcaciones ordenadas de menor a mayor:", calificaciones)
    promedio = sum(calificaciones)/len(calificaciones)
    print("Promedio de calificaciones:", promedio)
    num_calificaciones = len(calificaciones)
    print("Numeros de calificaciones ingresadas:", num_calificaciones)
    calificaciones_str = ','.join(map(str, calificaciones))
    print("Calificaciones en cadena:", calificaciones_str)
    aprobados = sum(1 for calificacion in calificaciones if calificacion => 6)
    print("Alumnos aprobados:", aprobados)
    calificacion_minima = min(calificaciones)
    calificacion_max = max(calificaciones)
    print("La nota más alta fue:", calificacion_max, "La nota más baja fue:", calificacion_minima)
    calificaciones.clear()