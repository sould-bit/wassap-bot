from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from    reminders import remember

app = Flask(__name__)

@app.route('/bot' ,methods=['POST'])
def bot():
    incoming_msg  = request.values.get('Body', '').lower()
    # menajes entrantes ,  obtenemos el mensaje ingresado por el usuario , con el metodo request y lo pasamos a minusculas 
    resp = MessagingResponse()
    #instanciamos la clase , que ayuda a generar la respuesta al usuario
    msg =  resp.message()
    # msg.body('this  is the response TEXT')
    # # metodo de message para contruir el cuerpo del mensaje 
    # msg.media('')
    # # metodo de message para captar urls , 

    responded = False
    
    msg.body("\u26A1  ")
    try:
        if "hello" in incoming_msg:
            msg.body("hi im ruben lets go \n this is options \n \u2211 algebra \n option two \n option tree" )
            responded = True
        elif "algebra" in incoming_msg:
             answer = remember('algebra')
             msg.body(answer + "\n now  its cool , go the fuking ")
             print(request.form['Body'])
             responded = True
        elif "option two" in incoming_msg:
            msg.body("estamos trabajando en esta funcion")
            responded = True
        elif  "option tree" in incoming_msg:
            msg.body("estamos trabajando en esta funcion")
            responded = True
        else:
            responded = False
            msg.body("to start say hello ")
            
    except Exception as e:
        print(f'Error algo salio mal ')
        msg.body("wheit sombady is bad ")
    return str(resp)
if __name__ =='__main__':
    app.run()