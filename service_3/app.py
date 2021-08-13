#Marius Saunders
#QA Project 2
#Kendama Order History

from flask import Flask
import random

app = Flask(__name__)

accessories = ["Go Pro", "Tripod", "Adobe Premiere Pro", "Editing Computer", "RED DSMC2", "24000 Power Bank"]

@app.route('/get/accessories')
def get_accessories():
    return random.choice(accessories)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)