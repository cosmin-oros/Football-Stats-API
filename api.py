from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Stats(db.Model):
    # create columns for the db
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    matches = db.Column(db.Integer, nullable=False)
    matches_started = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    yellow_cards = db.Column(db.Integer, nullable=False)
    red_cards = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"{self.name} {self.matches_started}/{self.matches} matches started/played " \
               f"{self.goals} goals {self.assists} assists {self.yellow_cards} yellow cards " \
               f"{self.red_cards} red cards {self.rating} rating"


@app.route('/')
def index():
    return "Stats Main Page"


@app.route('/stats')
def get_stats():
    stats = Stats.query.all()
    output = []

    for stat in stats:
        stat_data = {'name': stat.name,
                     'matches': stat.matches,
                     'matches_started': stat.matches_started,
                     'goals': stat.goals,
                     'assists': stat.assists,
                     'yellow_cards': stat.yellow_cards,
                     'red_cards': stat.red_cards,
                     'rating': stat.rating
                     }
        output.append(stat_data)

    return {"stats": output}


app.run(host="0.0.0.0", port=80)
