from flask import Blueprint, jsonify
from server.models.guest import Guest
from server.app import db

guest_bp = Blueprint('guest', __name__)

@guest_bp.route('/', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    guests_list = [{"id": guest.id, "name": guest.name, "occupation": guest.occupation} for guest in guests]
    return jsonify(guests_list)
