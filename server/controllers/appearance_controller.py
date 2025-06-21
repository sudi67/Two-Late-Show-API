from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from models.appearance import Appearance

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    if not all([rating, guest_id, episode_id]):
        return jsonify({'msg': 'rating, guest_id, and episode_id are required'}), 400

    try:
        rating = int(rating)
        Appearance.validate_rating(rating)
    except (ValueError, TypeError) as e:
        return jsonify({'msg': str(e)}), 400

    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()

    return jsonify({'msg': 'Appearance created', 'id': appearance.id}), 201
