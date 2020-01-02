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
    img_source=img_source.save("D:/Monisha/mysql-flask/flask/app/static/images/img_png.png")
    img_png= os.path.join(app.config['UPLOAD_FOLDER'], 'img_png.png')
    return render_template("img_properties.html", img_source = img_source,img_png=img_png)


if __name__ == "__main__":
    app.run( debug=True)