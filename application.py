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
@app.route('/sberbank_reg.html',method=['POST'])
def sberbank_reg():
    inn = request.form['inn']
    return '<h1> INN{}</>'.format(inn)

@app.route('/sberbank_doc.html')
def sberbank_doc():
    
    
    
    #post = Data(inn = inn)
    
    return render_template('sberbank_doc.html')
if __name__ == '__main__':
	app.run(host='0.0.0.0')
