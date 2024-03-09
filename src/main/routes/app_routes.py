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
    
@app_routes_bp.route('/favicon.ico')
def favicon():
    # To change the site icon, simply change your .ico to favicon.ico in the Static folder. Remembering to rename it in the process to favicon.ico
    return send_from_directory(os.path.join(app_routes_bp.root_path, '../../static'),
                          'favicon.ico')

@app_routes_bp.route('/')
def swagger_ui():
    # Swagger Documentation Renderer
    return send_from_directory(os.path.join(app_routes_bp.root_path, '../../templates'),
                          'docs.html')

@app_routes_bp.route('/openapi.json')
def swagger_file():
    # Develop your swagger for this project in the Swagger Editor and convert it to JSON
    return send_from_directory(os.path.join(app_routes_bp.root_path, '../../templates/documentation'),
                          'openapi.json')