from __future__ import print_function
from PIL import Image,ImageFilter,ImageDraw,ImageFont
from PIL import ImageEnhance

import os

from flask import Flask, request, render_template, send_from_directory


folder = os.path.join('static', 'images')

app = Flask(__name__ ,static_url_path='/static')
app.config['UPLOAD_FOLDER'] = folder


@app.route('/')

def show_index():
    #source image
    img = os.path.join(app.config['UPLOAD_FOLDER'], 'Tulips.jpg')

        #properties
    img_source = Image.open("D:/Monisha/mysql-flask/pillow/app/static/images/Tulips.jpg")
    img_format = img_source.format
    img_size=img_source.size
    img_mode=img_source.mode

    return render_template("flask_pillow.html", user_image = img,img_format = img_format,img_size=img_size,img_mode=img_mode,img_source=img_source,
    )



if __name__ == "__main__":
    app.run( debug=True)