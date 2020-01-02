from __future__ import print_function
from PIL import Image,ImageFilter

import os

from flask import Flask, request, render_template, send_from_directory


folder = os.path.join('static', 'images')

app = Flask(__name__ ,static_url_path='/static')
app.config['UPLOAD_FOLDER'] = folder


@app.route('/')

def show_index():
    source_img = os.path.join(app.config['UPLOAD_FOLDER'], 'Lighthouse.jpg')
    return render_template("img_properties_pillow.html", source_img=source_img
    )


if __name__ == "__main__":
    app.run( debug=True)