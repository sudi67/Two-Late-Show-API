from flask import Blueprint, jsonify
from models.guest import Guest
from flask import Blueprint, jsonify

guest_bp = Blueprint('guest', __name__)

@guest_bp.route('/guests', methods=['GET'])
def list_guests():
    guests = Guest.query.all()
    result = []
    for guest in guests:
        result.append({
            'id': guest.id,
            'name': guest.name,
            'occupation': guest.occupation
        })
    return jsonify(result), 200
