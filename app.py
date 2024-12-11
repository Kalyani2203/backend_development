from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)

# Generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

# Route to shorten a URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('original_url')
    if not original_url:
        return jsonify({"error": "Missing 'original_url'"}), 400

    # Check if the URL is already shortened
    existing_url = URL.query.filter_by(original_url=original_url).first()
    if existing_url:
        return jsonify({"short_url": request.host_url + existing_url.short_url})

    # Create a new short URL
    short_url = generate_short_url()
    while URL.query.filter_by(short_url=short_url).first():
        short_url = generate_short_url()

    new_url = URL(original_url=original_url, short_url=short_url)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({"short_url": request.host_url + short_url})

# Route to redirect to the original URL
@app.route('/<short_url>')
def redirect_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)

if __name__ == '_main_':
    # Create the database
    with app.app_context():
        db.create_all()

from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)

# Generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

# Route to shorten a URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('original_url')
    if not original_url:
        return jsonify({"error": "Missing 'original_url'"}), 400

    # Check if the URL is already shortened
    existing_url = URL.query.filter_by(original_url=original_url).first()
    if existing_url:
        return jsonify({"short_url": request.host_url + existing_url.short_url})

    # Create a new short URL
    short_url = generate_short_url()
    while URL.query.filter_by(short_url=short_url).first():
        short_url = generate_short_url()

    new_url = URL(original_url=original_url, short_url=short_url)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({"short_url": request.host_url + short_url})

# Route to redirect to the original URL
@app.route('/<short_url>')
def redirect_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)

if __name__ == '_main_':
    # Create the database
    with app.app_context():
        db.create_all()

    app.run(debug=True)
