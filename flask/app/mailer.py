from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'monijjmm@gmail.com'
app.config['MAIL_PASSWORD'] = 'monijeni1923'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'monijjmm@gmail.com', recipients = ['monishawlts@gmail.com'])
   msg.body = "Welcome to Flask"
   mail.send(msg)
   return "Mail sent successfully"

if __name__ == '__main__':
   app.run(debug = True)