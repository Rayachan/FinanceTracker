from flask import Flask
from database import init_db
from routes import expenses_bp

app = Flask(__name__)

with app.app_context():
    init_db()

app.register_blueprint(expenses_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    #need 0.0.0.0 to work in docker so that it can connect with the outside