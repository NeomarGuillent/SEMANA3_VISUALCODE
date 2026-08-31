#fUNCIÓN SIN RETORNO Y SIN PARAMETROS
def titulo():
    print("="*40)
    print("UNIVERSIDAD PRIVADA DEL NORTE")
    print("="*40)
#función con retorno y parametros en ella....
def validar_nota(mensaje):
    while True:
        try:
            nota=float(input(mensaje))
            if nota>=0 and nota<=20:
                return nota
            else:
                print("ERROR: Nota fuera de rango [0-20]")
        except ValueError:
            print("ERROR: El valor ingresado debe ser númerico..!!")
#función con retorno para el examen final
def calcular_EF(ProyectoFinal,Lab):
    nota_EF=ProyectoFinal*0.6+Lab*0.4
    return nota_EF
#función con retorno
def bono_cisco(nota_EF, tiene_cisco):
    if tiene_cisco=="s":
        nota_EF+=1
        if nota_EF>=20:
            nota_EF=20
    return nota_EF
#función con retorno
def promedio_final(t1,t2,t3,EP,EF):
    promedio=t1*0.1+t2*0.1+t3*0.1+EP*0.2+EF*0.5
    return promedio
#función con retorno
def estado_aca(promedio):
    if promedio>=12:
        estado="APROBADO"
    else:
        estado="DESAPROBADO"
    return estado

titulo()
alumno=input("INGRESAR NOMBRE DEL ESTUDIANTE:  ")
print("===DIGITE LAS NOTAS===")
t1=validar_nota("NOTA T1 [10%]:  ")
t2=validar_nota("NOTA T2 [10%]:  ")
t3=validar_nota("NOTA T3 [10%]:  ")
ep=validar_nota("EXAMEN PARCIAL [20%]:  ")
print("ingresar notas del examen final:  ")
proyecto_final=validar_nota("INGRESE LA NOTA DEL PROYECTO FINAL [60%EF]:  ")
nota_lab=validar_nota("INGRESAR NOTA DEL LABORATORIO [40%]:  ")

while True:
    curso_cisco=input("tiene el certificado del curso CISCONETACADEMY:  [S-N]").lower()
    if curso_cisco in ["s","n"]:
        break
    print("ERROR: Los caracteres permitidos son [S-N]")
nota_EF=calcular_EF(proyecto_final, nota_lab)
nota_EF_Cisco=bono_cisco(nota_EF,curso_cisco)
promedio_ponderado=promedio_final(t1,t2,t3,ep,nota_EF_Cisco)
estado_acad=estado_aca(promedio_ponderado)

print("**"*40)
print("REPORTE DE NOTAS")
print("**"*40)
print("Estudiante", alumno)
if curso_cisco=="s":
    print("FELICIDADES")
print("Nota EF", nota_EF_Cisco)
print("Tu promedio ponderado es de:", promedio_ponderado)
print("Usted ha: ",estado_acad)
print("**"*40)


