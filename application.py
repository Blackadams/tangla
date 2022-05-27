
from flask import Flask, render_template



application = Flask(__name__)



@application.route("/about")
def about():
    return render_template("tangla/about.html")


# @application.route("/hello")
# def index():

#     return "Hello World."


@application.route("/home",methods=['GET', 'POST'])
def home():

    return render_template('tangla/home.html')


@application.route("/poultry")
def poultry():
    return render_template('tangla/poultry.html')




@application.route("/herbs")
def herbs():
    return render_template('tangla/herbs.html')


@application.route("/dairy-farming/")
def dairy():
    return render_template('tangla/dairy.html')




@application.route("/ornamental-birds/")
def ornament():
    return render_template('tangla/ornament.html')


@application.route("/gallery/")
def gallery():
    return render_template('tangla/gallery.html')


@application.route("/")
@application.route("/home_page/")
def land():
    return render_template('tangla/landing.html')


if __name__ == "__main__":
    application.debug=True
    application.run()
