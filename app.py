from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

# Connect to MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/my_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Profile(db.Model):
    mobilenumber = db.Column(db.String(255), primary_key=True)
    username = db.Column(db.String(255), unique=False, nullable=False)
    datetime = db.Column(db.String(255), unique=False, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    punchinout = db.Column(db.String(255), nullable=False)  
    selfie = db.Column(db.String(255), nullable=False)  
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    mobilenumber = request.form.get('mobilenumber')
    username = request.form.get('username')
    datetime = request.form.get('datetime')
    location = request.form.get('location')
    punchinout = request.form.get('punchinout')
    selfie = request.form.get('selfie')

    # Create a new Profile object
    new_profile = Profile(mobilenumber=mobilenumber, username=username, datetime=datetime, location=location, punchinout=punchinout, selfie=selfie)

    # Add the new profile to the database session
    db.session.add(new_profile)

    # Commit the changes to the database
    db.session.commit()

    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
