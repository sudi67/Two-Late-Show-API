from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import db
from models.episode import Episode
from models.appearance import Appearance

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    result = []
    for ep in episodes:
        result.append({
            'id': ep.id,
            'date': ep.date.isoformat(),
            'number': ep.number
        })
    return jsonify(result), 200

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    ep = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=id).all()
    appearances_list = []
    for app in appearances:
        appearances_list.append({
            'id': app.id,
            'rating': app.rating,
            'guest_id': app.guest_id
        })
    return jsonify({
        'id': ep.id,
        'date': ep.date.isoformat(),
        'number': ep.number,
        'appearances': appearances_list
    }), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    ep = Episode.query.get_or_404(id)
    db.session.delete(ep)
    db.session.commit()
    return jsonify({'msg': 'Episode and related appearances deleted'}), 200
