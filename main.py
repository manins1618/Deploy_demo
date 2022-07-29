# install flask ---> pip install flask

# import
from flask import Flask, render_template, request
import joblib

# load the model
model = joblib.load('predict_79.pkl')

# initialise the app
app = Flask(__name__)  #__name__ variable of main file

# write code here

@app.route('/')
def homepage():
    return render_template('home.html')    

@app.route('/details')
def details():
    return render_template('details.html')   

@app.route('/form1')
def form1():
    return render_template('form1.html')

@app.route('/predict', methods=['post'])
def predict():
    preg = int(request.form.get('preg'))
    plas= int(request.form.get('plas'))
    pres = int(request.form.get('pres'))
    skin = int(request.form.get('skin'))
    test = int(request.form.get('test'))
    mass = float(request.form.get('mass'))
    pedi = float(request.form.get('pedi'))
    age = int(request.form.get('age'))


    data = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])

    if data[0] == 0:
        resp  = 'Not Diabetic'
    else:
        resp = 'Diabetic'

    return render_template('form1.html', data = resp)


# last line of code
app.run(host='0.0.0.0'  , debug = True) # debug = True let us update this code on live server. 



# http: - hypertext transfer protocol 
# 127.0.0.1 - ip address  - local address
# 5000 - port 
# / - route