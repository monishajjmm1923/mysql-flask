from __future__ import print_function
from PIL import Image,ImageFilter

import os

from flask import Flask, request, render_template, send_from_directory


folder = os.path.join('static', 'images')

app = Flask(__name__ ,static_url_path='/static')
app.config['UPLOAD_FOLDER'] = folder


@app.route('/')

def show_index():

    img_source = Image.open("D:/Monisha/mysql-flask/flask/app/static/images/Lighthouse.jpg")
    box = (100, 100, 400, 400)
    img_source=img_source.crop(box)
    img_source.save("D:/Monisha/mysql-flask/flask/app/static/images/crop.jpg")
    img_crop= os.path.join(app.config['UPLOAD_FOLDER'], 'crop.jpg')
    return render_template("img_properties_pillow.html", img_crop=img_crop,img_source=img_source)


if __name__ == "__main__":
    app.run( debug=True)
