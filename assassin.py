from flask import Flask, request
from face_compare import compare


app = Flask(__name__)

mainfrm = "<form action='compare' method='GET'>\
            Video URL:<br>\
            <input type='text' name='source_face' value='sample/source.jpg'/>\
            <input type='text' name='target_face' value='sample/target.jpg'/>\
            <input type='submit' value='Submit'>\
        </form>"


@app.route('/')
def index():
    return mainfrm

@app.route('/compare', methods = ['GET'])
def processVideo():
    # read source and target image from GET and set default Value 
    sourceURL = request.args.get('source_face', 'sample/source.jpg')
    targetURL = request.args.get('target_face', 'sample/target.jpg')
    result = compare(sourceURL, targetURL)
    return mainfrm + "<br>" + "Src = " + str(sourceURL) + "<br>Tgt = " + str(targetURL) + "<br> RESULT = " + str(result)


if __name__ == '__main__':
#    app.run(debug=True)
    app.run(host='0.0.0.0', threaded=True)