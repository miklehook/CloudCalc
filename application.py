from flask import Flask, render_template, request, redirect, url_for
#from application import db
#from application.models import Data


app = Flask(__name__)
app.debug=True
# change this to your own value
app.secret_key = 'cC1YCIWOj9GgWspgNEo2'

@app.route('/')
@app.route('/sberbank_op.html')
def sberbank_op():
	return render_template('sberbank_op.html')
@app.route('/sberbank_reg.html',methods=['POST'])
def sberbank_reg():
    return render_template('sberbank_reg.html')
@app.route('/sberbank_doc.html')
def sberbank_doc():
    return render_template('sberbank_doc.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
