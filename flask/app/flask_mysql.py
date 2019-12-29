from flask import Flask,request,render_template
from flaskext.mysql import MySQL
mysql=MySQL()
 
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='test'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

@app.route('/')   
def my_form():
    return render_template('forms.html')  

@app.route('/',methods=['POST'])    
def Authenticate():
    username=request.form['u']
    password=request.form['p']
    cursor=mysql.connect().cursor()
    cursor.execute("SELECT * from user where username= '"+ username +"' and password='"+ password +"'")
    data=cursor.fetchone()
    if data is None:
        return "username password wrong"
    else:
        return "login successfull"

if __name__ =='__main__':  
    app.run() 