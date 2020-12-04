import os

from flask_sqlalchemy import SQLAlchemy
from flask import current_app, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from passlib.apps import custom_app_context as pwd_context

from app.helpers import *
from app.access.accessFunctions import *
from app.access import bp
#from app.models import log, portfolio, users

# login

# login required
@bp.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # this was modified for SQL-ALCHEMY
    # https://stackoverflow.com/questions/17972020/how-to-execute-raw-sql-in-flask-sqlalchemy-app

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")
        
        # Query database for username {'val': 5}
        rows = db.session.execute("SELECT * FROM users WHERE username = :username",
                          {"username" : request.form.get("username")})
        print(rows)
        d = resultProxy_2_dict(rows)

        print(d["username"])
        print(len(d))

        # Ensure username exists and password is correct
        if len(d["username"]) == request.form.get("username") or not check_password_hash(d["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = d["id"]

        # Redirect user to home page
        return redirect(url_for("overview.ind"))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("Please provide a username")
        elif not request.form.get("password") or not request.form.get("password_confirm"):
            return apology("Please provide a password")
        elif not request.form.get("password") == request.form.get("password_confirm"):
            return apology("Password must match confirmation")
    # ensure that password contains letters numbers and symbols
        elif len(request.form.get("password")) < 8:
            return apology("Password must be over 8 characters")
        elif not hasNumbers(request.form.get("password")):
            return apology("Password must contain numbers")
        elif hasSpecialCharecters(request.form.get("password")) == False:
            return apology("Password must contain special characters")
        # hash password
        print(request.form.get("password"))
        hash = generate_password_hash(request.form.get("password"))

        # add user to database
        result = db.session.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get("username"), hash=hash)
        print(request.form.get("username"))
        print(hash)
        # ensure username is unique
        if not result:
            return apology("username is already registered")
        # NEED TO ADD RUNTIME EXCEPTION FOR UNIQUE constraint failed: users.username
        # remember which user has logged in
        session["user_id"] = result

        # redirect user to home page
        return redirect(url_for("overview.ind"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@bp.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")

for code in default_exceptions:
    bp.errorhandler(code)(errorhandler)
