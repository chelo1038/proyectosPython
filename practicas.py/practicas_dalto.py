#ejercicio curso 

otros_cursos_minimo = 2.5
otros_cursos_max = 7
otros_cursos_promedio =4
dalto_curso = 1.5

#diferencia de duracion 

diferencia_min = 100 - dalto_curso/ otros_cursos_minimo*100
diferencia_max = 100- dalto_curso*1000 // otros_cursos_max /10
diferencia_promedio = 100- dalto_curso/ otros_cursos_promedio*100
print ("el curso de dalto dura ", diferencia_min,"%" " menos que el mas rapido" )
print ("el curso de dalto dura un", diferencia_max,"%" " que el curso mas lento")
print("el curso de dalto dura", diferencia_promedio,"%" " menos que el promedio " )



print("--------------")