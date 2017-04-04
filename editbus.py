@app.route('/edit_page/<id>', methods = ['POST','GET'])
	def edit_page (id):
		addb = addbus.query.get(id)
		if request.method == 'POST':		
			addb.busnumber = request.form['busnumber']
			addb.startroute = request.form['startroute']
			addb.endroute = request.form['endroute']
			addb.stopa = request.form['stopa']
			addb.stopb = request.form['stopb']
			addb.stopc = request.form['stopc']
			addb.stopd = request.form['stopd']
			addb.stope = request.form['stope']
			addb.stopf = request.form['stopf']
			addb.stopg = request.form['stopg']
			addb.stoph = request.form['stoph']
			addb.stopi = request.form['stopi']
			addb.stopj = request.form['stopj']
			
			db.session.commit()
		return  redirect(url_for('addbus'))
		return render_template('edit.html',addb=addb)

			
