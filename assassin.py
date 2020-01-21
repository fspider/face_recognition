from flask import Flask, request, redirect, render_template
from face_compare import compare
import os

app = Flask(__name__)




@app.route('/')
def index():
    return render_template("main.html", result = "")

@app.route('/compare', methods = ['GET', 'POST'])
def processVideo():
    if request.method == "GET":
        return render_template("main.html", result = "")
    if not request.files:
        return render_template("main.html", result = "No input!")

    try:
        image1 = request.files["image1"]
        image1_path = os.path.join(app.config["IMAGE_UPLOADS"], image1.filename)
        image1.save(image1_path)
        print("Image1 saved", image1_path)

        image2 = request.files["image2"]
        image2_path = os.path.join(app.config["IMAGE_UPLOADS"], image2.filename)
        image2.save(image2_path)
        print("Image2 saved", image2_path)


        # # read source and target image from GET and set default Value 
        # sourceURL = request.args.get('source_face', 'sample/source.jpg')
        # targetURL = request.args.get('target_face', 'sample/target.jpg')
        # return mainfrm + "<br>" + "Src = " + str(sourceURL) + "<br>Tgt = " + str(targetURL) + "<br> RESULT = " + str(result)

        result = compare(image1_path, image2_path)
        return render_template("main.html", result = result)
    except Exception as e:
        print(e)
        return render_template("main.html", result = "ERROR")


if __name__ == '__main__':
#    app.run()
    app.config["IMAGE_UPLOADS"] = "sample"
    app.run(host='192.168.0.114', threaded=True)