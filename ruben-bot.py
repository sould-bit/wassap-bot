from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

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
    print(request.form['Body'])
    msg.body("\u26A1")
    try:

        if "hello" in incoming_msg:
            msg.body("hi im ruben lets go this is options\n"" algebra \n " )
            responded = True
        elif "algebra" in incoming_msg:
            msg.body('cool go for the fucking \n 2 * 2 =')
            responded = True
        if responded == False:
            msg.body("im sorry , i've not this option")
    
            
    except Exception as e:
        print(f'Error algo salio mal ')
        msg.body("wheit sombady is bad ")
    return str(resp)
if __name__ =='__main__':
    app.run()