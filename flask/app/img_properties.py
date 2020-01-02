from __future__ import print_function
from PIL import Image,ImageFilter

import os

from flask import Flask, request, render_template, send_from_directory


folder = os.path.join('static', 'images')

app = Flask(__name__ ,static_url_path='/static')
app.config['UPLOAD_FOLDER'] = folder


@app.route('/')

def show_index():
    img = os.path.join(app.config['UPLOAD_FOLDER'], 'Lighthouse.jpg')
    
    
    a = Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Lighthouse.jpg")
    print(a.format)
    print(a.size)
    print(a.mode)

       
    a = a.rotate(180)
    a.save("D:/Monisha/mysql-flask/flask/app/static/images/rotate.jpg")
   
    img2= os.path.join(app.config['UPLOAD_FOLDER'], 'rotate.jpg')

    #size = (128, 128)
    #a=a.thumbnail(size)
    #a.save("D:/Monisha/mysql-flask/flask/app/static/images/e.jpg", "PNG")
    #img4= os.path.join(app.config['UPLOAD_FOLDER'], 'f.png')
    
    box = (100, 100, 400, 400)
    a=a.crop(box)
    a.save("D:/Monisha/mysql-flask/flask/app/static/images/crop.jpg")
    img3= os.path.join(app.config['UPLOAD_FOLDER'], 'crop.jpg')
    
    
    b= Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Lighthouse.jpg")
   
    r, g, b = b.split()
    b= Image.merge("RGB", (b, g, r))
    b.save("D:/Monisha/mysql-flask/flask/app/static/images/rgb.jpg")
    img4= os.path.join(app.config['UPLOAD_FOLDER'], 'rgb.jpg')


    c= Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Lighthouse.jpg")
    c=c.resize((2000, 1000))
    c.save("D:/Monisha/mysql-flask/flask/app/static/images/resize.jpg")
    img6= os.path.join(app.config['UPLOAD_FOLDER'], 'resize.jpg')

    d= Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Lighthouse.jpg")

    d = d.transpose(Image.FLIP_TOP_BOTTOM)
    d.save("D:/Monisha/mysql-flask/flask/app/static/images/rotate_top.jpg")
    img7= os.path.join(app.config['UPLOAD_FOLDER'], 'rotate_top.jpg')

    f= Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Lighthouse.jpg")
    f = f.convert("L")
    f.save("D:/Monisha/mysql-flask/flask/app/static/images/gray.jpg")
    img8= os.path.join(app.config['UPLOAD_FOLDER'], 'gray.jpg')
    
    g= Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Lighthouse.jpg")

    g = g.filter(ImageFilter.DETAIL)
    g.save("D:/Monisha/mysql-flask/flask/app/static/images/filter.jpg")
    img9= os.path.join(app.config['UPLOAD_FOLDER'], 'filter.jpg')
    
    return render_template("img_properties.html", user_image = img,use_image = img2,a=a,user=img3,use=img4,us=img6,u=img7,i=img8,im=img9)





#@app.route('/')
#def rotate():
     
        #Relative Path 
    #img = Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Hydrangeas.jpg")  
          
        #Angle given 
    #img = img.rotate(180)  
          
    #img.save("D:/Monisha/mysql-flask/flask/app/static/images/c.jpg")

    #img2= os.path.join(app.config['UPLOAD_FOLDER'], 'c.jpg')

    #return render_template("img_properties.html", use_image = img2)
    

    #return render_template("img_properties.html", use_image = img2)
     








if __name__ == "__main__":
    app.run( debug=True)