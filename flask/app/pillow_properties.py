from __future__ import print_function
from PIL import Image,ImageFilter

import os

from flask import Flask, request, render_template, send_from_directory


folder = os.path.join('static', 'images')

app = Flask(__name__ ,static_url_path='/static')
app.config['UPLOAD_FOLDER'] = folder

@app.route('/')

def show_index():
    #source image
  
    
    #properties
    img_source = Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Lighthouse.jpg")
    img_format = img_source.format
    img_size=img_source.size
    img_mode=img_source.mode
    return render_template("img_properties_pillow.html", img_source=img_source,img_format=img_format,img_size=img_size,img_mode=img_mode
    )


if __name__ == "__main__":
    app.run( debug=True)