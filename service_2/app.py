#Marius Saunders
#QA Project 2
#Kendama Order History

from flask import Flask
import random

app = Flask(__name__)

damas = ["Krom Gas", "SK Lomond", "Sol Liam R Mod", "Sweets Decade", "GT Nic Stodd", "Cereal WC Performer"]

@app.route('/get/dama')
def get_dama():
    return random.choice(damas)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
