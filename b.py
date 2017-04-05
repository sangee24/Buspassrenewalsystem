from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'soundaryaquit@gmail.com'
app.config['MAIL_PASSWORD'] = 'Angry birds'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/a")
def index():
   msg = Message('Hello', sender = 'soundaryaquit@gmail.com', recipients = ['lenin.nkl@gmail.com'])
   msg.body = "Your pass is renewed"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)


