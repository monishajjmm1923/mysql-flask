from __future__ import print_function
from PIL import Image,ImageFilter

import os

from flask import Flask, request, render_template, send_from_directory


folder = os.path.join('static', 'images')

app = Flask(__name__ ,static_url_path='/static')
app.config['UPLOAD_FOLDER'] = folder


@app.route('/')

def show_index():

        #rgb
    b= Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Lighthouse.jpg")
   
    r, g, b = b.split()
    b= Image.merge("RGB", (b, g, r))
    b.save("D:/Monisha/mysql-flask/flask/app/static/images/rgb.jpg")
    img_rgb= os.path.join(app.config['UPLOAD_FOLDER'], 'rgb.jpg')
    return render_template("img_properties_pillow.html", img_rgb=img_rgb,b=b)


if __name__ == "__main__":
    app.run( debug=True)
