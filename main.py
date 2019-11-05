from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about():
    user_name = request.cookies.get("username")
    return render_template("about.html", name=user_name)


@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    response = make_response(render_template("success.html"))
    response.set_cookie("username", contact_name)
    print(contact_name)

    return response


if __name__ == '__main__':
    app.run()