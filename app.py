from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


model = pickle.load(open('startup.pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods =['POST'])

def login():
   
   a = request.form["Time"]
   b = request.form["V1"]
   c = request.form["V2"]
   d = request.form["V3"]
   e = request.form["V4"]
   f = request.form["V5"]
   g = request.form["V6"]
   g1 = request.form["V7"]
   h = request.form["V8"]
   i = request.form["V9"]
   j = request.form["V10"]
   k = request.form["V11"]
   l = request.form["V12"]
   m = request.form["V13"]
   n = request.form["V14"]
   o = request.form["V15"]
   p = request.form["V16"]
   q = request.form["V17"]
   r = request.form["V18"]
   s = request.form["V19"]
   t = request.form["V20"]
   u = request.form["V21"]
   v = request.form["V22"]
   w = request.form["V23"]
   x = request.form["V24"]
   y = request.form["V25"]
   z = request.form["V26"]
   z1 = request.form["V27"]
   z2 = request.form["V28"]
   z3 = request.form["Amount"]



   

   t =  [[int(a),float(b),float(c),float(d),float(e),float(f),float(g),float(g1),float(h),float(i),float(j),float(k),float(l),float(m),float(n),float(o),float(p),float(q),float(r),float(s),float(t),float(u),float(v),float(w),float(x),float(y),float(z),float(z1),float(z2),float(z3)]]
   output =model.predict(t)
   
   if(output==1.0):
       output="The transaction is Fraudulent."
   elif(output==0.0):
       output="Great!!The transaction is Legitimate."

   return render_template("index.html", y = str((output)))
#    return render_template("front.html")

if __name__ == '__main__' :
    app.run(debug=True)
          





