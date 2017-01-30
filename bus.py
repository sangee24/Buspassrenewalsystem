from flask import Flask,redirect,url_for,render_template
from flask import request
from flask import flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kite@localhost/buspass'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')
	
@app.route('/create')
def create():
	return render_template('create.html')
	
class registration(db.Model):
	id = db.Column('register_id', db.Integer, primary_key = True )
	name=db.Column(db.String(50),unique=True)
	password=db.Column(db.String(50),unique=True)
	dob=db.Column(db.Integer)
	gender=db.Column(db.String(50))
	qualification=db.Column(db.String(50))
	address=db.Column(db.String(50),unique=True)
	email=db.Column(db.String(50),unique=True)
	city=db.Column(db.String(50))
	phone=db.Column(db.Integer,unique=True)	
	
	def __init__(self,name,password,dob,gender,qualification,address,email,city,phone):
		self.name=name
		self.password=password
		self.dob=dob
		self.gender=gender
		self.qualification=qualification
		self.address=address
		self.email=email
		self.city=city
		self.phone=phone 	
		
	@app.route('/register_page', methods = ['GET', 'POST'])
	def register_page():
		if request.method == 'POST':
			if not request.form['id'] or not request.form['name'] or not request.form['password']or not request.form['dob'] or not request.form['gender'] or not request.form['qualification'] or not request.form['address'] or not request.form['email'] or not request.form['city'] or not request.form['phone'] :
				flash('Please enter all the fields', 'error')
			else:
				register = registration(request.form['id'],request.form['name'],request.form['password'],request.form['dob'],request.form['gender'],request.form['qualification'],request.form['address'],request.form['email'],request.form['city'],request.form['Phone']   )         
				db.session.add(register)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('home_register'))
			return render_template('register.html') 

class createpass(db.Model):
	id = db.Column('create_id', db.Integer, primary_key = True )
	userid=db.Column(db.Integer,unique=True)
	passid=db.Column(db.Integer,unique=True)
	busno=db.Column(db.String(50),unique=True)
	from=db.Column(db.String(50))
	to=db.Column(db.String(50))
	passtype=db.Column(db.String(50))
	date=db.Column(db.Integer)
	amount=db.Column(db.Integer)
	cardno=db.Column(db.Integer,unique=True)
	cvvno=db.Column(db.Integer,unique=True)	
	
	def __init__(self,,userid,passid,busno,from,to,passtype,date,amount,cardno,cvvno):
	
		self.userid=userid
		self.passid=passid
		self.busno=busno
		self.from=from
		self.to=to
		self.passtype=passtype
		self.date=date
		self.amount=amount
		self.cardno=cardno
		self.cvvno=cvvno
		 	
		
	@app.route('/create_page', methods = ['GET', 'POST'])
	def create_page():
		if request.method == 'POST':
			if not request.form['id'] or not request.form['userid'] or not request.form['passid']or not request.form['busno'] or not request.form['from'] or not request.form['to'] or not request.form['passtype'] or not request.form['date'] or not request.form['amount'] or not request.form['cardno'] or not request.form['cvvno'] :
				flash('Please enter all the fields', 'error')
			else:
				create = createpass(request.form['id'],request.form['userid'],request.form['passid'],request.form['busno'],request.form['from'],request.form['to'],request.form['passtype'],request.form['date'],request.form['amount'],request.form['cardno'],request.form['cvvno']   )         
				db.session.add(register)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('home_create'))
			return render_template('create.html') 



if __name__ == '__main__':
	db.create_all()
	app.run(debug = True)
