from flask import Flask, request, jsonify
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/extract_audio', methods=['POST'])
def extract_audio():
    data = request.get_json()
    video_url = data.get('video_url')
    
    if not video_url:
        return jsonify({'error': 'No video URL provided'}), 400

    try:
        # Initialize YouTube object
        yt = YouTube(video_url)
        # Get the audio stream URL
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream:
            audio_url = audio_stream.url
            return jsonify({'audio_url': audio_url})
        else:
            return jsonify({'error': 'No audio stream found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))  # Default to 10000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
    
