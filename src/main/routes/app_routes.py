import os
from flask import Blueprint, jsonify, send_from_directory

app_routes_bp = Blueprint('app_routes', __name__)

@app_routes_bp.route('/info', methods=['GET'])
def info():
    # Customize the info the way you want, if you want to put the info as home and the documentation as docs, feel free.
    return jsonify({
        "status": True,
        "message": "Welcome to the Structure Flask API!",
        "version": "1.0v",
        "endpoints": {
            "docs": "/",
            "info": "/info",
        },
        "documentation": "/",
        "contact": {
            "email_personal": "pedro.henrique.martins404@gmail.com",
            "email_academic": "pedro.borges@alu.unibalsas.edu.br",
            "github": "piedro404",
            "linkedin": "pedrohenrique404"
        }
    }), 200