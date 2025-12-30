from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from api.routes import search_courses, recommend_courses, user_clicked_course
import os

app = Flask(__name__)
CORS(app)

USER_ID = 1


# ---------------- FRONTEND ----------------
@app.route("/")
def home():
    return send_from_directory("../frontend", "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("../frontend", path)


# ---------------- BACKEND APIs ----------------
@app.route("/search")
def search():
    query = request.args.get("q", "")
    search_results, recommendations = search_courses(query)

    return jsonify({
        "search_results": search_results,
        "recommendations": recommendations
    })



@app.route("/click", methods=["POST"])
def click():
    course_id = request.json.get("course_id")
    return jsonify(user_clicked_course(USER_ID, course_id))


if __name__ == "__main__":
    app.run(debug=True)
