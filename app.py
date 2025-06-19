from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/indir', methods=['GET', 'POST'])  # ÖNEMLİ: GET ve POST ikisi birden açık
def indir():
    url = request.args.get('url') or request.form.get('url')  # Hem GET hem POST desteği

    if not url:
        return jsonify({"error": "TikTok bağlantısı eksik!"}), 400

    api_url = f"https://tikwm.com/api/?url={url}"

    try:
        response = requests.get(api_url)
        data = response.json()

    from flask import send_from_directory

@app.route('/googlea9723dd352217b44.html')
def dogrulama_dosyasi():
    return send_from_directory('.', 'googlea9723dd352217b44.html')

    except Exception as e:
        return jsonify({"error": f"API isteği başarısız: {str(e)}"}), 500

    if "data" in data and data["data"]:
        video_data = data["data"]
        result = {
            "kullanici_adi": video_data.get("author", {}).get("unique_id", ""),
            "aciklama": video_data.get("title", ""),
            "profil_resmi": video_data.get("author", {}).get("avatar", ""),
            "video": video_data.get("play", ""),
            "filigranli": video_data.get("wmplay", ""),
            "mp3": video_data.get("music", "")
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Video bilgileri alınamadı!"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

