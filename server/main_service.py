import os,cv2,pytesseract
from flask import Flask, render_template, request,jsonify
from PIL import Image
from OCR_handler import handler
import json

pytesseract.pytesseract.tesseract_cmd = r".\libs\Tesseract\tesseract.exe"

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('.')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/ocr', methods=['POST','GET'])
def upload_file():
    user_name = request.form['user_name']
    password = request.form['password']
    check = False

    if request.method == "GET":
        return "This is the api BLah blah"

    elif request.method == "POST":
        with open(r'.\libs\accounts.json') as f:
            data = json.load(f)
        for k, v in data.items():
            if user_name == v['user_name'] and password == v['password']:
                check = True

        result = ''
        if check:

            for i in request.files:
                file = request.files[i]
                f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(f)
                image = cv2.imread(UPLOAD_FOLDER+"/"+file.filename)
                os.remove(UPLOAD_FOLDER+"/"+file.filename)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                filename = "{}.png".format(file.filename)
                cv2.imwrite(filename, gray)
                text = handler(filename)
                result = result + (i+'\n'+text)
                os.remove(filename)
        else:
            result = "denied"
        return jsonify({"text" : result})

app.run("0.0.0.0",5000,threaded=True,debug=True)


