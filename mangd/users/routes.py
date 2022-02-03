import os
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


# import local modules:
from mangd import db, oauth, mail
from mangd.database import user
from mangd.extras import login_required

# imports for flask-mail
from flask_mail import Message
users = Blueprint('users', __name__)

# register function
@users.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        error = None
        _username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # check if the user provided a username, assign an error messsage
        if not _username:
            error = "Username is required."

        # Check if user provided email:
        elif not email:
            error = "Must provide an email"

        # if username already exists, return error message
        elif user.query.filter_by(username=_username).first():
            error = "Username already exists"

        # Check if the email has already been regustered for another user:
        elif user.query.filter_by(email=email).first():
            error = "Email is already in use."

        # if the lenght of username is less than 6 characcters, return error message
        elif len(_username) < 6:
            error = "Username must be at least 6 characters long"

        # check if user provided a password.
        elif not password:
            error = "Password is required."

        # check if the password provided matches with the confirmation input
        elif password != request.form["confirmation"]:
            error = "Passwords don't match."

        # check if the lenth of password if at least 6 characters long
        elif len(password) < 6:
            error = "Password must be at least 6 characters long"

        # if there are no errors, add user to database and commit
        if error is None:
            usr = user(_username, generate_password_hash(password), email)
            db.session.add(usr)
            db.session.commit()

            # let the user know they've been succesfully registered and redirect them to the login page
            flash("You Have Been Registered Successfully!", "success")
            return redirect(url_for("users.login"))

        # if there was an error during registration, flask error message
        flash(error, "danger")
    return render_template("register.html")


# login fucntion
@users.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":

        error = None
        _username = request.form["username"]
        password = request.form["password"]

        # Ensure username was submitted
        if not _username:
            error = "must provide username"

        # Ensure password was submitted
        elif not password:
            error = "must provide password"

        # Query database for username
        usr = user.query.filter_by(username=_username).first()

        if not usr:
            usr = user.query.filter_by(email=_username).first()

        # check if user exists
        if not usr:
            error = "invalid user or email."

        # Ensure username exists and password is correct
        elif not check_password_hash(usr.password, password):
            error = "invalid password"

        # if there are no errors, clear any previous sessions,
        # and initiate a new session for user
        if error is None:
            session.clear()
            session["user_id"] = usr._id
            return redirect(url_for("todos.todos"))

        # let the user name what went wrong using the flash function
        flash(error, "danger")

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("login.html")



@users.route("/forgot_password", methods=("GET", "POST"))
def forgot_password():
    if request.method == "POST":
        email = request.form["email"]
        if not user.query.filter_by(email=email).first():
            flash(" There is not an account registered under that email.", "danger")
        else:
            _user = user.query.filter_by(email=email).first()
            _token = _user.get_reset_token()

            # send email using gmail:
            msg = Message(
                "Password Reset", sender="criscodesnyc@gmail.com", recipients=[email]
            )
            msg.body = f"""To reset your password, please visit: 
            {url_for('users.reset_password', token=_token, _external=True)}"""
            mail.send(msg)
            flash(
                "An email has been sent to you account with the link to reset your password",
                "success",
            )
            return redirect(url_for("users.login"))
    return render_template("forgotpassword.html")


@users.route("/reset_password/<token>", methods=("GET", "POST"))
def reset_password(token):
    if request.method == "POST":
        _user = user.verify_reset_token(token)
        if not _user:
            flash("That is an invalid or expired token", "danger")
            return redirect(url_for("forgot_password"))
        else:
            error = None
            _password = request.form["password"]

            # check if user provided a password
            if not _password:
                error = "Password is required."

            # check if the password provided matches with the confirmation input
            elif _password != request.form["confirmation"]:
                error = "Passwords don't match."

            # check if the lenth of password if at least 6 characters long
            elif len(_password) < 6:
                error = "Password must be at least 6 characters long."
            # if no errors ocured, commit new password for the user to the database, provide success mesage to user
            elif error is None:
                _user.password = generate_password_hash(_password)
                db.session.commit()
                flash("Your password has been reset successfully", "success")
                return redirect("users.login")
        flash(error, "danger")
    return render_template("resetpassword.html")

# user logout
@users.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for("users.login"))




