from flask import Flask, render_template, request, redirect, url_for
from application import models

app = Flask(__name__)
app.debug=True
# change this to your own value
app.secret_key = 'cC1YCIWOj9GgWspgNEo2'
@app.route('/')
@app.route('/sberbank_op.html')
def sberbank_op():
	return render_template('sberbank_op.html')
@app.route('/sberbank_reg.html')
def sberbank_reg():
	return render_template('sberbank_reg.html')
@app.route('/sberbank_doc.html',method=['POST'])
def sberbank_doc():
    
    inn = request.form['inn']
    
    #post = Data(inn = inn)
    
    return '<h1> INN{}</>'.format(inn)
if __name__ == '__main__':
	app.run(host='0.0.0.0')
