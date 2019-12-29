#from flask import Flask ,render_template
from flask import* 
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello, this is our first flask website";  

@app.route("/test")  
def message():  
      return render_template('demo.html') 
  
if __name__ =='__main__':  
    app.run() 