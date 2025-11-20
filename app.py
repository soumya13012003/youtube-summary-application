
from flask import Flask, request, jsonify, render_template, send_from_directory
import os
from summarize import process_video_url

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    video_url = data.get('video_url')
    summary = process_video_url(video_url)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
