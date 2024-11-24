from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    # Retrieve the URL from query parameters
    url = request.args.get('url')
    
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        ydl_opts = {
            'quiet': True,  # Suppress the standard output
            'extract_flat': True,  # Only extract info, not download
            'forcejson': True,  # Get info in JSON format
        }
        info_dict = yt_dlp.YoutubeDL(ydl_opts).extract_info(url, download=False)
        return jsonify(info_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)