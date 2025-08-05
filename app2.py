from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    MaSV = request.args.get("MaSV")
    sv = None
    error = None
    if MaSV:
        try:
            response = requests.get(f"http://192.168.1.6:8000/sinhvien/{MaSV}")

            response.raise_for_status()
            sv = response.json()
        except requests.exceptions.RequestException:
            error = "Không tìm thấy sinh viên có mã đã nhập hoặc API không phản hồi."
    return render_template("sinhvien.html", sv=sv, error=error, MaSV=MaSV)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

