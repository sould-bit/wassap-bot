#%%

import random

def remember (keyword):
    # recordatorio , con el parametro key  el tipo de saludo enfocado a un area escoguida 
    letra_aleatoria = chr(random.randint(97,122))
    # utilizamos chr para convertir codigo ASCII , lo que nos devolvera una letra , y sera aleatoria con random.randint
    gretting =   {
        'algebra':['propiedad reflexiva \n la igualdad entre dos partes se mantiene aunque se cambien de lado  \n'
                    ' toda cantidad es igual a si misma  ',

                    'propiedad simetrica ' '\n \nsi dos cantidades son iguales ,\n entonces se puede intercambiar  el orden de la operacion sin afectar el resultado de ello  ',
                    'porpiedad asimetrica ' '\n si se aplica la misma operacion matematica a ambos lado ,la igualdad sigue cierta'],
                 }
    aleatory_al = random.choice(gretting[keyword])
    #usamos un dict  clave-valor ,   y devolvemos  los valores  en este caso listas aleatorias 
    reminder = f'remember\n the '+ aleatory_al + '\n dont forget \n'

    

    return reminder

