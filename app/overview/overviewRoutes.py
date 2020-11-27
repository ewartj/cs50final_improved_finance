import os

#TEST ACCOUNT: test test
# to do: appologise if you add text when buying/selling for amoutn
# change to SQLalchemy

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
import pandas as pd


from passlib.apps import custom_app_context as pwd_context

from app.helpers import *
# from app.models import portfolio, log, users, portfolioSchema

#from app.models import log, portfolio, users
from app.overview import bp

@bp.route("/")
@bp.route("/index")
@login_required
def index():
    """Show portfolio of stocks"""
    cash = float(get_cash(session["user_id"]))
    print(cash)
    print(session["user_id"])

    # pull all transactions belonging to user
    portfoli = getPortfolio(session["user_id"])

    if not portfoli: # CHANGE THIS SO IT LOOKS FOR AN EMPRTY DICTIONARY
        return apology("sorry you have no holdings")
    # https://stackoverflow.com/questions/12047193/how-to-convert-sql-query-result-to-pandas-data-structure
    # Turn this into a function 
    portfolio_db = SQLalchemy_query_pandas(portfoli)
    print("Pandas portfolio:")
    print(portfolio_db)
    full_port_db = index_portfolio(portfolio_db)
    print(full_port_db)
    # Get total value
    portfolio_total = full_port_db['cur_total'].sum() + cash
    return render_template("index.html", cash=usd(cash), grand_total=usd(portfolio_total))

@login_required
@bp.route("/indexJSON")
def indexJSON():
    """Show portfolio of stocks"""
    # pull all transactions belonging to user
    portfolio = getPortfolio(session["user_id"])
    if not portfolio: # CHANGE THIS SO IT LOOKS FOR AN EMPRTY DICTIONARY
        return apology("sorry you have no holdings")
    # https://stackoverflow.com/questions/12047193/how-to-convert-sql-query-result-to-pandas-data-structure
    portfolio_db = SQLalchemy_query_pandas(portfolio)
    #portfolioTEST = pd.read_sql("SELECT stock, number, value FROM portfolio WHERE id= :id", { "id" : session["user_id"]}, con=db.engine)
    full_port_db = index_portfolio(portfolio_db)
    print(full_port_db)
    # Get total value
    # jsonify the db so its easy to show as a table
    full_port_db = full_port_db.to_json(orient='table',index=False)
    print("JSOn format")
    print(full_port_db)
    return full_port_db

@bp.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return render_template("history.html")

@bp.route("/historyJSON")
@login_required
def historyJSON():
    """Show history of transactions"""
    log = db.session.execute("SELECT * FROM log WHERE id=:id ORDER BY date DESC", { "id" : session["user_id"]})
    log_df = SQLalchemy_query_pandas(log)
    log_json = log_df.to_json(orient='table',index=False)
    print(log_df)
    return log_json

for code in default_exceptions:
    bp.errorhandler(code)(errorhandler)