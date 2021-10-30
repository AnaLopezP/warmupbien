import random

a = ([[4,9],[8.5,10],[5,9],[8.5,9.5],[3,7],[4,9],[3,8],[7.5,8],[5,9],[0,6]])
b = ([[5,10],[4,4],[7,9],[2,8],[6,9.5],[8.5,10],[8,10],[0,7],[3,9],[0,3]])
c = ([[4,7],[6,8],[6,9],[6.5,9],[2,6],[6.5,9],[5.5,9],[9.5,9.5],[5,9],[4,9]])


def Monte_carlo (rango_calidad):
    variables=['dinero', 'ubicación', 'trato', 'condiciones_trabajo', 'compañeros', 'crecimiento_carrera', 'tipo_puesto', 'impacto_social', 'repercusión_atmósfera', 'viajes']
    importancia=[0.2, 0.2, 0.1, 0.1, 0.02, 0.02, 0.01, 0.1, 0.15, 0.1]
    resultado=[]
    for i in range(len(variables)): 
        valor = importancia[i] * (random.uniform(rango_calidad[i][0], rango_calidad[i][1]))
        resultado.append(valor)
    resultado_final = sum(resultado)
    return resultado_final


trabajo_1 = Monte_carlo(a)
trabajo_2 = Monte_carlo(b)
trabajo_3 = Monte_carlo(c)

print("El primer trabajo tiene un valor de " + str(trabajo_1))
print("El segundo trabajo tiene un valor de " + str(trabajo_2))
print("El tercer trabajo tiene un valor de " + str(trabajo_3))

if trabajo_1 > trabajo_3 and trabajo_1 > trabajo_2:
    print("Me quedo con el trabajo 1.")
if trabajo_2 > trabajo_3 and trabajo_2 > trabajo_1:
    print("Me quedo con el trabajo 2.")
if trabajo_3 > trabajo_2 and trabajo_3 > trabajo_1:
    print("Me quedo con el trabajo 3.")