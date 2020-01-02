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
    img_source = Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Lighthouse.jpg")
    enhancer = ImageEnhance.Contrast(img_source)
    enhanced_im = enhancer.enhance(4.0)
    enhanced_im.save("D:/Monisha/mysql-flask/flask/app/static/images/contrast.jpg")
    img_text= os.path.join(app.config['UPLOAD_FOLDER'], 'contrast.jpg')
    return render_template("img_properties.html", img_source = img_source,img_text=img_text)

if __name__ == "__main__":
    app.run( debug=True)