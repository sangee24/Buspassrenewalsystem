from flask import Flask,redirect,url_for,render_template
from flask import request
from flask import flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kite@localhost/buspass'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

@app.route('/')
def login():
    return render_template('login.html')
   
@app.route('/login_reg',methods=['GET','POST'])
def login_reg():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form['name']
    password = request.form['password']
    register = registration.query.filter_by(name=user,password=password).first()  
    if register is None:
        return redirect(url_for('login'))
    return redirect(url_for('success',name=user))

@app.route('/success/<name>')
def success(name):
	return render_template('profile.html',registration=registration.query.filter_by(name='%s'%name))


@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/createpass')
def createpass():
	return render_template('createpass.html',registration=registration.query.order_by(registration.id.desc()).limit(1).all())
	
@app.route('/passdetails')
def passdetails():
	if request.method == 'GET':
		return render_template('pass.html')
	user = request.form['passid']
	return render_template('details',passid=user)
	
@app.route('/details/<int:passid>')
def details(passid):
	return render_template('details.html',createpass=createpass.query.filter_by(passid='%s'%passid))

@app.route('/renew')
def renew():
	return render_template('renew.html')	

class registration(db.Model):
	id = db.Column('register_id', db.Integer, primary_key = True )
	name=db.Column(db.String(50),unique=True)
	password=db.Column(db.String(50),unique=True)
	gender=db.Column(db.String(50))
	qualification=db.Column(db.String(50))
	address=db.Column(db.String(50),unique=True)
	email=db.Column(db.String(50),unique=True)
	city=db.Column(db.String(50))
	phone=db.Column(db.Integer,unique=True)	
	
	def __init__(self,name,password,gender,qualification,address,email,city,phone):
		self.name=name
		self.password=password
		self.gender=gender
		self.qualification=qualification
		self.address=address
		self.email=email
		self.city=city
		self.phone=phone 	
		

	@app.route('/register_page', methods = ['GET', 'POST'])
	def register_page():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['password'] or not request.form['gender'] or not request.form['qualification'] or not request.form['address'] or not request.form['email'] or not request.form['city'] or not request.form['phone'] :
				flash('Please enter all the fields', 'error')
			else:
				register = registration(request.form['name'],request.form['password'],request.form['gender'],request.form['qualification'],request.form['address'],request.form['email'],request.form['city'],request.form['phone']   )         
				db.session.add(register)
				db.session.commit()
				flash('Record was successfully added')
			return redirect(url_for('register'))
		return render_template('register.html') 
		
class createpass(db.Model):
	id = db.Column('create_id', db.Integer, primary_key = True )
	passid = db.Column(db.Integer,unique=True)
	busno = db.Column(db.String(50))
	start = db.Column(db.String(50))
	end=db.Column(db.String(50))
	bustype=db.Column(db.String(50))
	amount=db.Column(db.Integer)
	cardno=db.Column(db.Integer,unique=True)
	cvvno=db.Column(db.Integer,unique=True)	
	month=db.Column(db.Integer)
	year=db.Column(db.Integer)	
	
	def __init__(self,passid,busno,start,end,bustype,amount,cardno,cvvno,month,year):
		self.passid=passid
		self.busno=busno
		self.start=start
		self.end=end
		self.bustype=bustype
		self.amount=amount
		self.cardno=cardno
		self.cvvno=cvvno
		self.month=month
		self.year=year
		 	 	
	@app.route('/create_page', methods = ['GET', 'POST'])
	def create_page():
		if request.method == 'POST':
			if  not request.form['passid'] or not request.form['busno'] or not request.form['start'] or not request.form['end'] or not request.form['bustype'] or not request.form['amount'] or not request.form['cardno'] or not request.form['cvvno'] or not request.form['month'] or not request.form['year'] :
				flash('Please enter all the fields', 'error')
			else:
				create = createpass(request.form['passid'],request.form['busno'],request.form['start'],request.form['end'],request.form['bustype'],request.form['amount'],request.form['cardno'],request.form['cvvno'],request.form['month'],request.form['year']   )         
				db.session.add(create)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('createpass'))
			return render_template('createpass.html') 


if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)
			
