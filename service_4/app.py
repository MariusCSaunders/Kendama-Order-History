#Marius Saunders
#QA Project 2
#Kendama Order History

from flask import Flask, request, jsonify

app = Flask(__name__)

prices = {
    'damas': {
        'Krom Beans': 45.99,
        'SK Mor': 26.99,
        'Sol Alex M': 44.99,
        'Sweets Splice': 74.99,
        'GT TF': 105.00,
        'Cereal 1.5 SK': 35.99
    },
    'accessories': {
        'Go Pro': 234.99,
        'Tripod': 19.99,
        'Adobe Premiere Pro': 139.99,
        'Editing Computer': 1499.99,
        'RED DSMC2': 14499.99,
        'Power Bank': 37.99
    }
}

@app.route('/post/order', methods=['POST'])
def post_order():
    dama = request.json['damas']
    accessory = request.json['accessories']

    price = prices['damas'][dama] + prices['accessories'][accessory]
    price = price + 3.50
    price = round(price, 2)

    return jsonify(price)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')