from flask import Blueprint, jsonify, request
from server.app import db
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')

    if not rating or not guest_id or not episode_id:
        return jsonify({'msg': 'rating, guest_id and episode_id are required'}), 400

    if not (1 <= rating <= 5):
        return jsonify({'msg': 'rating must be between 1 and 5'}), 400

    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()

    return jsonify({'msg': 'Appearance created', 'id': appearance.id}), 201

@appearance_bp.route('/episode/<int:episode_id>', methods=['GET'])
def get_appearances_by_episode(episode_id):
    appearances = Appearance.query.filter_by(episode_id=episode_id).all()
    result = []
    for app in appearances:
        guest = Guest.query.get(app.guest_id)
        result.append({
            'id': app.id,
            'rating': app.rating,
            'guest_id': app.guest_id,
            'guest_name': guest.name if guest else None
        })
    return jsonify(result)
