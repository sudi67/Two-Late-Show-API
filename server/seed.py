from app import create_app, db

app = create_app()
app.app_context().push()

from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance

def seed_data():
    # Add users
    user1 = User(username='admin')
    user1.set_password('password')
    db.session.add(user1)

    # Add guests
    guest1 = Guest(name='John Doe', occupation='Comedian')
    guest2 = Guest(name='Jane Smith', occupation='Actor')
    db.session.add_all([guest1, guest2])

    # Add episodes
    episode1 = Episode(date='2023-01-01', number=1)
    episode2 = Episode(date='2023-01-08', number=2)
    db.session.add_all([episode1, episode2])

    # Add appearances
    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode2)
    db.session.add_all([appearance1, appearance2])

    db.session.commit()

if __name__ == '__main__':
    seed_data()
