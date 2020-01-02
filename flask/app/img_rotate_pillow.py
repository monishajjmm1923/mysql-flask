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
    img_source = img_source.rotate(180)
    img_source.save("D:/Monisha/mysql-flask/flask/app/static/images/rotate.jpg")
   
    img_rotate= os.path.join(app.config['UPLOAD_FOLDER'], 'rotate.jpg')
    return render_template("img_properties_pillow.html", img_rotate=img_rotate,img_source=img_source)


if __name__ == "__main__":
    app.run( debug=True)
