dinero = 2000
precio_helado = 100
hambre = edad = 9
contador = 0
while (dinero >= precio_helado and hambre < 85):
    dinero = dinero - precio_helado
    hambre = edad + hambre
    precio_helado = precio_helado + 0.2 * precio_helado
    contador = contador +1
    print("me he comido "+str(contador)+ " helados y tengo hambre: " + str (hambre))
    print("ahora tengo " + str(dinero) + " monedas") 

if (dinero <= precio_helado ):
    print("no puedo comprar más helados,me he quedado sin dinero" + str(dinero))
else:
    print("Me he quedado sin hambre: " + str(hambre))
