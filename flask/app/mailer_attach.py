from flask import *  
from flask_mail import *  
  
app = Flask(__name__)  
  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465  
app.config["MAIL_USERNAME"] = 'monijjmm@gmail.com'  
app.config['MAIL_PASSWORD'] = 'monijeni1923'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
mail = Mail(app)  
 
@app.route("/")  
def index():  
    msg = Message(subject = "hello", body = "hello", sender = "monijeni@gmail.com", recipients = ["monishawlts@gmail.com"])  
    with app.open_resource("C:/Users/Public/Pictures/Sample Pictures/Hydrangeas.jpg") as fp:  
        msg.attach("Hydrangeas.jpg","image/png",fp.read())  
        mail.send(msg)  
    return "sent"  
  
if __name__ == "__main__":  
    app.run(debug = True)  