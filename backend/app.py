from flask import Flask,request,jsonify
from flask_cors import CORS
import os
import uuid
from Resume import run_scorer

app=Flask(__name__)
CORS(app) 

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_DOMAINS = [
    "Cybersecurity", "Software Engineering",
    "Machine Learning", "Data Science", "Blockchain"
]

@app.route("/upload",methods=["POST"])
def score():
    if "pdf" not in request.files:
        return jsonify({"error": "No PDF file provided"}), 400
    pdf = request.files["pdf"]
    if not pdf.filename.endswith(".pdf"):
        return jsonify({"error": "Invalid file type"}), 400
    domain = request.form.get("domain")
    if not domain or domain not in ALLOWED_DOMAINS:
        return jsonify({"error": "Invalid domain"}), 400
    

    filename = f"{uuid.uuid4().hex}.pdf"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    pdf.save(filepath)

    try:
        result = run_scorer(filepath, domain)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        os.remove(filepath)


if __name__ == "__main__":
    app.run(debug=True, port=5000)