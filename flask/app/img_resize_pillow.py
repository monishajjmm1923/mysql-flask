from __future__ import print_function
from PIL import Image,ImageFilter

import os

from flask import Flask, request, render_template, send_from_directory


folder = os.path.join('static', 'images')

app = Flask(__name__ ,static_url_path='/static')
app.config['UPLOAD_FOLDER'] = folder


@app.route('/')

def show_index():

        
    c= Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Lighthouse.jpg")
    c=c.resize((2000, 1000))
    c.save("D:/Monisha/mysql-flask/flask/app/static/images/resize.jpg")
    img_resize= os.path.join(app.config['UPLOAD_FOLDER'], 'resize.jpg')
    return render_template("img_properties_pillow.html", img_resize=img_resize,c=c)


if __name__ == "__main__":
    app.run( debug=True)
