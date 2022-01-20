from flask import Blueprint

app = Blueprint("api", "api", url_prefix="/api/v1")

@app.route("/")
def index_():
    return jsonify(
                {
                    "status":[200, "working"]
                }
            )
