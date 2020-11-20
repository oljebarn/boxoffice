from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):
    """
    Features: 
    budget, popularity, runtime, actionOrAdventure, lan_cat, isSpielberg, isTop8dir, top5actor, isCollection
    """


    budget = IntegerField('How much money (USD) do you wish to spend on this movie?', validators=[DataRequired()])

    popularity = FloatField('How much hype is it around the movie? (scale from 0 to 300)', validators=[NumberRange(min=0, max=300)])

    runtime = FloatField('How long is the movie? (minutes)', validators=[DataRequired()])

    actOrAdv = IntegerField('Is it a adventure og action movie? (1 = yes, 0 = no)', validators=[NumberRange(min = 0, max= 1)])

    language = IntegerField('Do they speak English in this movie? (1 = yes, 0 = no)', validators=[NumberRange(min = 0, max= 1)])

    spielberg = IntegerField('Do you want the great Spielberg to direct it? (1 = yes, 0 = no)', validators=[NumberRange(min = 0, max= 1)])

    top8dir = IntegerField('Or do you want Bay, Russo, Jackson, Howard, Zemeckis, Nolan or Cameron? (1 = yes, 0 = no)', validators=[NumberRange(min = 0, max= 1)])

    top5actor = IntegerField('Does Samuel L. Jakson, Robert Downey Jr, Scarlett Johannsson, Harrison Ford or Tom Hanks act in the lead role? (1 = yes, 0 = no)', validators=[NumberRange(min = 0, max= 1)])

    collection = IntegerField('Is this movie a part of a collection? (1 = yes, 0 = no)', validators=[NumberRange(min = 0, max= 1)]) 
    
    submit = SubmitField('Submit')
