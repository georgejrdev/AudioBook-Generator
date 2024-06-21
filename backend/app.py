from src import *
from flask import Flask, send_file, request, jsonify
from flask_cors import cross_origin,CORS

app = Flask(__name__)
CORS(app)


@cross_origin
@app.route('/generateAudio', methods=['POST'])
def generate_audio():
    if 'pdf' not in request.files:
        print("Entrou aqui")
        return jsonify({'error': 'No file part'}), 400

    file = request.files['pdf']

    if file.filename == '':
        print("Entrou aqui não")
        return jsonify({'error': 'No selected file'}), 400
    

    if file:
        print("Aqui sim hehe")
        pdf = file.read()
        print("Lido")
        text = optimize_pdf(pdf)
        print("Quase la")
        audio = generate_voice(text)
        print("No final")
        return send_file(audio, as_attachment=True, download_name='audio.mp3', mimetype='audio/mpeg')


app.run("localhost",port=3030)