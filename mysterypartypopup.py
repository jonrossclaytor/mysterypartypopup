from flask import Flask
from flask import render_template
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route('/')
def home():

	app.config['MAIL_SERVER']='smtp.gmail.com'
	app.config['MAIL_PORT'] = 465
	app.config['MAIL_USERNAME'] = 'mysterypopup@gmail.com'
	app.config['MAIL_PASSWORD'] = 'mystery!'
	app.config['MAIL_USE_TLS'] = False
	app.config['MAIL_USE_SSL'] = True
	mail = Mail(app)
	
	msg = Message("Hello",
                  sender=("Mystery Party Popup","mysterypopup@gmail.com"),
                  recipients=["johnrossclaytor@gmail.com"])
	msg.body = "testing"
	msg.html = "<b>testing</b>"

	mail.send(msg)
	

	return render_template('index.html')

if __name__ == '__main__':
	app.run(port=5000, debug=True)