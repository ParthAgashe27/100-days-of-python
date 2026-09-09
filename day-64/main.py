from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


YOUR_GAME_DB_API_KEY = "your_api_key_here"  # Replace with your actual API key from The Game Database (TGDb)
GAME_DB_SEARCH_URL = "https://api.thegamesdb.net/v1.1/Games/ByGameName"



app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with your
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-games-collection.db"
db.init_app(app)


# CREATE TABLE
class Game(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f'<Game {self.title}>'


with app.app_context():
    db.create_all()

# New Find Movie Form
class FindMovieForm(FlaskForm):
    title = StringField("Game Title", validators=[DataRequired()])
    submit = SubmitField("Add Game")


@app.route("/")
def home():
    result = db.session.execute(db.select(Game).order_by(Game.ranking))
    games = result.scalars().all()
    return render_template("index.html", games=games)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        game_title = form.title.data
        search_url = f"{GAME_DB_SEARCH_URL}"
        response = requests.get(GAME_DB_SEARCH_URL, params={"apikey": YOUR_GAME_DB_API_KEY, "name": game_title})
        data = response.json()
        games_found = data["data"]["games"]  
        if data["data"]["games"]:
            game_data = games_found[0]  # Get the first result
            game_id_api = game_data["id"]
            img_response = requests.get(
                "https://api.thegamesdb.net/v1/Games/Images",
                params={"apikey": YOUR_GAME_DB_API_KEY, "games_id": game_id_api}
            )
            img_data = img_response.json()
            game_count = db.session.execute(db.select(Game)).scalars().all()
            next_ranking = len(game_count) + 1

            base_url = img_data["data"]["base_url"]["original"]
            images_list = img_data["data"]["images"].get(str(game_id_api), [])
            img_filename = images_list[0]["filename"] if images_list else ""
            img_url_final = base_url + img_filename if img_filename else ""
            new_game = Game(
                title=game_data["game_title"],
                year=game_data["release_date"].split("-")[0],
                img_url=img_url_final,
                description="",  # TheGamesDB search doesn't return this],
                rating=0.0,  # Default rating
                ranking=next_ranking,   # Default ranking
                review=""    # Default review
            )
            db.session.add(new_game)
            db.session.commit()
            return redirect(url_for("edit", id=new_game.id))
    return render_template("add.html", form=form)

@app.route("/edit", methods=["GET", "POST"])
def edit():

    game_id = request.args.get('id')
    game_selected = db.get_or_404(Game, game_id)
    if request.method == "POST":
        game_selected.rating = float(request.form["rating"])
        game_selected.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", game=game_selected)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    game_id = request.args.get('id')
    game_to_delete = db.get_or_404(Game, game_id)
    db.session.delete(game_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
