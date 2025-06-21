from flask import Blueprint, jsonify, request
from server.app import db
from server.models.episode import Episode
from server.models.appearance import Appearance

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    episodes_list = [{"id": ep.id, "date": ep.date.isoformat(), "number": ep.number} for ep in episodes]
    return jsonify(episodes_list)

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=id).all()
    appearances_list = [{"id": app.id, "rating": app.rating, "guest_id": app.guest_id} for app in appearances]
    return jsonify({
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": appearances_list
    })

@episode_bp.route('/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    Appearance.query.filter_by(episode_id=id).delete()
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"msg": "Episode and appearances deleted"}), 200
