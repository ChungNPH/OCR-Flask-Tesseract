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

        if check:
            file = request.files['image']
            f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(f)
            # print(file.filename)
            image = cv2.imread(UPLOAD_FOLDER+"/"+file.filename)
            os.remove(UPLOAD_FOLDER+"/"+file.filename)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            filename = "{}.png".format(os.getpid())
            cv2.imwrite(filename, gray)
            text = handler(filename)
            os.remove(filename)
        else:
            text = "denied"
        return jsonify({"text" : text})

app.run("0.0.0.0",5000,threaded=True,debug=True)


