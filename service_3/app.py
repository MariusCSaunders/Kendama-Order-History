from flask import Flask
import random

app = Flask(__name__)

accessories = ["Dama Holster", "T-Shirt", "String Pack", "Pin Badge", "5 Panel Hat", "Ken Care Kit"]

@app.route('/get/accessories')
def get_accessories():
    return random.choice(accessories)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)