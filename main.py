from flask import Flask, request, jsonify
import yt_dlp
import os
import json

app = Flask(__name__)
cookies = 'cookies.txt'
@app.route('/info', methods=['GET'])
def get_info():
    # Retrieve the URL from query parameters
    url = request.args.get('url')
    
    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Get the cookies from environment variables (Vercel setup)

    # If cookies exist, load and pass them to yt-dlp
    try:
        ydl_opts = {
            'quiet': True,  # Suppress the standard output
            'extract_flat': True,  # Only extract info, not download
            'forcejson': True,  # Get info in JSON format
            'cookies': cookies  # Pass cookies to yt-dlp
        }

        # Extract video info
        info_dict = yt_dlp.YoutubeDL(ydl_opts).extract_info(url, download=False)
        return jsonify(info_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
