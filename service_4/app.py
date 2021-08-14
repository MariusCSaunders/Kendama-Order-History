#Marius Saunders
#QA Project 2
#Kendama Order History

from flask import Flask, request, jsonify

app = Flask(__name__)

prices = {
    'damas': {
        'Krom Gas': 40.00,
        'SK Lomond': 36.99,
        'Sol Liam R Mod': 44.99,
        'Sweets Decade': 74.99,
        'GT Nic Stodd': 45.00,
        'Cereal WC Performer': 33.99
    },
    'accessories': {
        'Dama Holster': 4.99,
        'T-Shirt': 19.99,
        'String Pack': 4.99,
        'Pin Badge': 0.00,
        '5 Panel Hat': 24.99,
        'Ken Care Kit': 18.99
    }
}

@app.route('/post/order', methods=['POST'])
def post_order():
    dama = request.json['damas']
    accessory = request.json['accessories']

    price = prices['damas'][dama] + prices['accessories'][accessory]
    price = price + 3.50
    price = round(price, 2)

    return jsonify(5)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
    