# health check route to check if the app is running
from flask import Blueprint, jsonify
from database import get_connection

expenses_bp = Blueprint('expenses', __name__)


@expenses_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200