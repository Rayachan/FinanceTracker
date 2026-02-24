from flask import Flask
from app.database import init_db

app = Flask(__name__)

with app.app_context():
    init_db()

from app.routes import expenses_bp

app.register_blueprint(expenses_bp)
app.register_blueprint(expenses_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    #need 0.0.0.0 to work in docker so that it can connect with the outside