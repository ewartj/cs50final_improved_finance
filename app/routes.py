from app.helpers import *
from flask import Flask, flash

## Should this go in init?

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors will need to make this a function?
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

#  import os

# #TEST ACCOUNT: test test
# # to do: appologise if you add text when buying/selling for amoutn
# # change to SQLalchemy

# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
# from flask_session import Session
# from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
# from werkzeug.security import check_password_hash, generate_password_hash
# from datetime import datetime
# import pandas as pd


# from passlib.apps import custom_app_context as pwd_context

# from app.helpers import *
# from app.models import portfolio, log, users, portfolioSchema

# #from app.models import log, portfolio, users
# from app import app, db

# # Homescreen
# @app.route("/")
# @app.route("/index")
# @login_required
# def index():
#     """Show portfolio of stocks"""
#     cash = float(get_cash(session["user_id"]))
#     print(cash)
#     print(session["user_id"])

#     # pull all transactions belonging to user
#     portfoli = getPortfolio(session["user_id"])

#     if not portfoli: # CHANGE THIS SO IT LOOKS FOR AN EMPRTY DICTIONARY
#         return apology("sorry you have no holdings")
#     # https://stackoverflow.com/questions/12047193/how-to-convert-sql-query-result-to-pandas-data-structure
#     # Turn this into a function 
#     portfolio_db = SQLalchemy_query_pandas(portfoli)
#     print("Pandas portfolio:")
#     print(portfolio_db)
#     full_port_db = index_portfolio(portfolio_db)
#     print(full_port_db)
#     # Get total value
#     portfolio_total = full_port_db['cur_total'].sum() + cash
#     return render_template("index.html", cash=usd(cash), grand_total=usd(portfolio_total))

# @login_required
# @app.route("/indexJSON")
# def indexJSON():
#     """Show portfolio of stocks"""
#     # pull all transactions belonging to user
#     portfolio = getPortfolio(session["user_id"])
#     if not portfolio: # CHANGE THIS SO IT LOOKS FOR AN EMPRTY DICTIONARY
#         return apology("sorry you have no holdings")
#     # https://stackoverflow.com/questions/12047193/how-to-convert-sql-query-result-to-pandas-data-structure
#     portfolio_db = SQLalchemy_query_pandas(portfolio)
#     #portfolioTEST = pd.read_sql("SELECT stock, number, value FROM portfolio WHERE id= :id", { "id" : session["user_id"]}, con=db.engine)
#     full_port_db = index_portfolio(portfolio_db)
#     print(full_port_db)
#     # Get total value
#     # jsonify the db so its easy to show as a table
#     full_port_db = full_port_db.to_json(orient='table',index=False)
#     print("JSOn format")
#     print(full_port_db)
#     return full_port_db


# #Manage portfolio
# @app.route("/buy", methods=["GET", "POST"])
# @login_required
# def buy():
#     """Buy shares of stock"""
#     #user selects buy and amount to but
#     if request.method == "POST":
#         print("Post")
#         # ensure a symbol and quantity were submited
#         check_request_okay(request)

#         name = request.form.get("symbol").upper()
#         print("name " + name)
#         amount = int(request.form.get("amount"))
#         print("amount " + str(amount))
#         user_id = session["user_id"]
#         print(user_id)

#         name_iex_info = lookup(name)
#         print(name_iex_info)
#         if not name_iex_info:
#             return apology("Symbol not found")

#         # calculate value of this
#         value = float(name_iex_info["price"]) * float(amount)
#         print("value")
#         print(value)

#         #check this is less than the cash the user has
#         cash = get_cash(session["user_id"])
#         print("can spend")
#         print(cash)

#         if cash < value:
#             return apology("Sorry cannot afford transaction") # THIS DID WORK UP TO HERE
#         else:
#             # update cash in databse
#             # https://www.programiz.com/python-programming/datetime/current-datetime
#             cash = cash - value
#             now = datetime.now()
#             dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#                 # update the portfolio database
#                 #https://www.sqlitetutorial.net/sqlite-update/
#             #db.session.execute("UPDATE users SET cash = :cash WHERE id = :id", {"cash" : cash, "id" : user_id})
#             update_cash(session["user_id"], cash)
#                 # check to see if already owned
#             is_owned = isOwned(session["user_id"], name_iex_info["symbol"])
#             print("is_owned!!!!!")
#             test_righcols = resultProxy_2_dict(is_owned)
#             # print(test_righcols) these only work if not empty
#             # print(test_righcols["stock"])
#                 # if owned there will be a result
#             if test_righcols: #len(is_owned) > 1: # this is wrong!!!!
#                 is_owned_name = test_righcols["stock"]
#             # get new amount
#                 new_amount = int(test_righcols["number"]) + int(amount)
#             # get new value
#                 new_value = float(test_righcols["value"]) + value
#             # get new values
#                 print("Update portfolio")
#                 db.session.execute("UPDATE portfolio SET number=:number, value=:value WHERE id=:id AND stock=:name",
#                 {"number" : new_amount, "value" : new_value,"id" : user_id, "name" : name})
#                 db.session.commit()
#                 db.session.execute("SELECT * FROM portfolio WHERE id= :id AND stock= :stock",{ "id" : session["user_id"], "stock" : name_iex_info["symbol"]})
#             # insert new stock to the db
#             else:
#                 print("Add to portfolio") # WORKED TO HERE. Its not updating the right column. Not inseting/updating
#                 inserted = db.session.execute("INSERT INTO portfolio (id, stock, number, value) VALUES(:id, :name, :number, :value)",
#                 {"id" : user_id , "number" : amount, "value" : value, "name" : name})
#                 db.session.commit()
#                 db.session.execute("SELECT * FROM portfolio WHERE id= :id AND stock= :stock",{ "id" : session["user_id"], "stock" : name_iex_info["symbol"]})
#                 is_owned3 = isOwned(session["user_id"], name_iex_info["symbol"])
#                 test_righcols = resultProxy_2_dict(is_owned3)
#                 print(is_owned3)
#                 print(test_righcols)
#             # add to log do I need a timestamp?
#             db.session.execute("INSERT INTO log (id, action, stock, amount, price_dealt, date) VALUES (:id, :action, :name, :amount, :price_dealt, :date)"
#             , {"id" : user_id ,"action" : "Buy", "amount" : amount, "price_dealt" : name_iex_info["price"], "name" : name, "date" : dt_string})
#             db.session.commit()
#             db.session.execute("SELECT * FROM log WHERE id=:id ORDER BY date DESC", { "id" : session["user_id"]})
#             # displaying everything to screen
#             portfolio = getPortfolio(session["user_id"])
#             portfolio_db = SQLalchemy_query_pandas(portfolio)
#             #portfolioTEST = pd.read_sql("SELECT stock, number, value FROM portfolio WHERE id= :id", { "id" : session["user_id"]}, con=db.engine)
#             full_port_db = index_portfolio(portfolio_db)
#             portfolio_total = full_port_db['total'].sum() + cash
#             print(full_port_db)
#             # Get total value
#             # jsonify the db so its easy to show as a table
#             full_port_db = full_port_db.to_json(orient='table',index=False)
#             print("JSOn format")
#             # Get total value
#             return render_template("index.html", portfolio=portfolio, cash=usd(cash), grand_total=usd(portfolio_total))
#     else:
#         print("ERROOOOR")
#         return render_template("buy.html") #cash=usd(cash), grand_total=usd(portfolio_total)

# @app.route("/sell", methods=["GET", "POST"])
# @login_required
# def sell():
#     """Sell shares of stock"""
#     #user selects buy and amount to but
#     if request.method == "POST":
#         check_request_okay(request)

#         name = request.form.get("symbol").upper()
#         name_iex_info = lookup(name)

#         if not name_iex_info:
#             return apology("Symbol not found")
#         # check if its owned
#         is_Owned = isOwned(session["user_id"], name_iex_info["symbol"])
#         print("is_owned!!!!!")
#         test_righcols = resultProxy_2_dict(is_Owned)
#         print(test_righcols)
#         print(test_righcols["stock"])
#         is_owned_name = test_righcols["stock"]
#                 # if owned there will be a result
#         if len(is_owned_name) > 1:
#             apology("Do not owned")

#         # check if there is suffient shares for the sale
#         amount = int(request.form.get("amount"))
#         sufficient_stock = int(test_righcols["number"]) - int(amount)
#         if sufficient_stock < 0:
#             apology("Insufficient stocks for this transactions")
#         else:
#             cash = get_cash(session["user_id"])
#             value = float(name_iex_info["price"]) * amount
#             new_amount = int(test_righcols["number"]) - int(amount)
#             new_value = float(test_righcols["value"]) - value
#             cash = cash + value
#             now = datetime.now()
#             dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#             if new_amount == 0:
#                 #db.session.execute("DELETE FROM portfolio WHERE id =:id AND stock=:name", { "id" : session["user_id"], "name" : name_iex_info["symbol"]})
#                 update_cash(session["user_id"], cash)
#                 db.session.commit()
#                 db.session.execute("SELECT stock, number, value FROM portfolio WHERE id= :id", { "id" : session["user_id"]})
#             # calculate value of this
#             else:
#             # update the portfolio database
#             #https://www.sqlitetutorial.net/sqlite-update/
#                 db.session.execute("UPDATE portfolio SET number=:number, value=:value WHERE id=:id AND stock=:name",
#             {"number" : new_amount, "value" : new_value, "id" : session["user_id"], "name" : name})
#                 #db.session.refresh(port)
#             db.session.execute("UPDATE users SET cash=:cash WHERE id=:id", {"cash" : cash,  "id" : session["user_id"]})
#             db.session.commit()
#             cash = get_cash(session["user_id"])
#             #db.session.refresh(usersUpdate)
#                 # check to see if already owned
#              # get new values
#             # add to log do I need a timestamp?
#             db.session.execute("INSERT INTO log (id, action, stock, amount, price_dealt, date) VALUES (:id, :action, :name, :amount, :price_dealt, :date)"
#             , { "id" : session["user_id"], "action" : "sell", "amount" : amount, "name" : name_iex_info["symbol"], "price_dealt" : name_iex_info["price"], "date" : dt_string})
#             db.session.commit()
#             portfolio = getPortfolio(session["user_id"])
#             portfolio_db = SQLalchemy_query_pandas(portfolio)
#             portfolio_total = 0.0
#             full_port_db = index_portfolio(portfolio_db)
#             print(full_port_db)
#             # Get total value
#             portfolio_total = full_port_db['total'].sum() + cash
#             return render_template("index.html", portfolio=portfolio, cash=usd(cash), grand_total=usd(portfolio_total))
#     return render_template("sell.html")



# @app.route("/history")
# @login_required
# def history():
#     """Show history of transactions"""
#     return render_template("history.html")

# @app.route("/historyJSON")
# @login_required
# def historyJSON():
#     """Show history of transactions"""
#     log = db.session.execute("SELECT * FROM log WHERE id=:id ORDER BY date DESC", { "id" : session["user_id"]})
#     log_df = SQLalchemy_query_pandas(log)
#     log_json = log_df.to_json(orient='table',index=False)
#     print(log_df)
#     return log_json 

# @app.route("/quote", methods=["GET", "POST"])
# @login_required
# def quote():
#     """Find a stock"""
#     if request.method == "POST":
#         #checking a stock exists and that the form was filled succesfuly
#         if not request.form.get("symbol"):
#             return render_template("quote.html")

#         symbol = lookup(request.form.get("symbol").upper())


#         if not symbol:
#             return apology("Cannot find {}".format(request.form.get("symbol")))

#         return render_template("quoted.html", symbol=symbol["symbol"], name=symbol["name"], price=symbol["price"])
#     else:
#         return render_template("quote.html")


# # login

# # login required
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     """Log user in"""
#     # this was modified for SQL-ALCHEMY
#     # https://stackoverflow.com/questions/17972020/how-to-execute-raw-sql-in-flask-sqlalchemy-app

#     # Forget any user_id
#     session.clear()

#     # User reached route via POST (as by submitting a form via POST)
#     if request.method == "POST":

#         # Ensure username was submitted
#         if not request.form.get("username"):
#             return apology("must provide username")

#         # Ensure password was submitted
#         elif not request.form.get("password"):
#             return apology("must provide password")
        
#         # Query database for username {'val': 5}
#         rows = db.session.execute("SELECT * FROM users WHERE username = :username",
#                           {"username" : request.form.get("username")})
#         print(rows)
#         d = resultProxy_2_dict(rows)

#         print(d["username"])
#         print(len(d))

#         # Ensure username exists and password is correct
#         if len(d["username"]) == request.form.get("username") or not check_password_hash(d["hash"], request.form.get("password")):
#             return apology("invalid username and/or password")

#         # Remember which user has logged in
#         session["user_id"] = d["id"]

#         # Redirect user to home page
#         return redirect(url_for("index"))

#     # User reached route via GET (as by clicking a link or via redirect)
#     else:
#         return render_template("login.html")


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         if not request.form.get("username"):
#             return apology("Please provide a username")
#         elif not request.form.get("password") or not request.form.get("password_confirm"):
#             return apology("Please provide a password")
#         elif not request.form.get("password") == request.form.get("password_confirm"):
#             return apology("Password must match confirmation")
#     # ensure that password contains letters numbers and symbols
#         elif len(request.form.get("password")) < 8:
#             return apology("Password must be over 8 characters")
#         elif not hasNumbers(request.form.get("password")):
#             return apology("Password must contain numbers")
#         elif hasSpecialCharecters(request.form.get("password")) == False:
#             return apology("Password must contain special characters")
#         # hash password
#         print(request.form.get("password"))
#         hash = generate_password_hash(request.form.get("password"))

#         # add user to database
#         result = db.session.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get("username"), hash=hash)
#         print(request.form.get("username"))
#         print(hash)
#         # ensure username is unique
#         if not result:
#             return apology("username is already registered")
#         # NEED TO ADD RUNTIME EXCEPTION FOR UNIQUE constraint failed: users.username
#         # remember which user has logged in
#         session["user_id"] = result

#         # redirect user to home page
#         return redirect(url_for("index"))

#     # else if user reached route via GET (as by clicking a link or via redirect)
#     else:
#         return render_template("register.html")

# @app.route("/logout")
# def logout():
#     """Log user out"""

#     # Forget any user_id
#     session.clear()

#     # Redirect user to login form
#     return redirect("/login")

# def errorhandler(e):
#     """Handle error"""
#     if not isinstance(e, HTTPException):
#         e = InternalServerError()
#     return apology(e.name, e.code)


# # Listen for errors
# for code in default_exceptions:
#     app.errorhandler(code)(errorhandler)