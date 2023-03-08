from flask import Flask, render_template, request
from PIL import Image
import io
import pytesseract


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/process_image', methods=['POST'])
def process_image():
    file = request.files['image']
    img = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(img)
    return render_template('result.html', text=text)



if __name__ == '__main__':
    app.run(debug=True)

