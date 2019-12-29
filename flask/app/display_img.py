import os

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload1.html")

@app.route("/upload1", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
   
    print(target)
   
    for upload in request.files.getlist("file"):
         
        filename = upload.filename
        destination = "/".join([target, filename])
      
        upload.save(destination)

 
    return render_template("complete1.html", image_name=filename)

@app.route('/upload1/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('D:/Monisha/flask/app/images')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)

if __name__ == "__main__":
    app.run( debug=True)
