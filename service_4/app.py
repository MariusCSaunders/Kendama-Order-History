from flask import Flask, request
from . import app

@app.route('/post/order', methods=['POST'])
def post_order():
    damas = request.json['damas']
    accessories = request.json['accessories']


