from flask import Flask
from flask import render_template
from flask import request
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/submit')
def submit():
	try:
		# configure mail server
		app.config['MAIL_SERVER']='smtp.gmail.com'
		app.config['MAIL_PORT'] = 465
		app.config['MAIL_USERNAME'] = 'mysterypopup@gmail.com'
		app.config['MAIL_PASSWORD'] = 'mystery!'
		app.config['MAIL_USE_TLS'] = False
		app.config['MAIL_USE_SSL'] = True
		mail = Mail(app)


		# collect input
		contactName = request.args.get('contactName')
		contactEmail = request.args.get('contactEmail')
		contactSubject = request.args.get('contactSubject')
		contactMessage = request.args.get('contactMessage')

		msg = Message(contactSubject,
	                  sender=("Info Request","mysterypopup@gmail.com"),
	                  recipients=["mysterypopup@gmail.com"])
		msg.html = """
				  <b>Name:</b> """ + contactName + """<br>
				  <b>Email:</b> """ + contactEmail + """<br>
				  <b>Subject:</b> """ + contactSubject + """<br><br>
				  <b>Message:</b> """ + contactMessage + """<br>
				   """

		mail.send(msg)
		
		return 'OK'

	except:
		return 'Error occurred.'
		

@app.route('/test')
def test():
	return render_template('test.html')

if __name__ == '__main__':
	app.run(port=5000, debug=True)