import os
import requests
import urllib.parse
from flask_sqlalchemy import SQLAlchemy
from string import ascii_letters, digits
from app import db
import pandas as pd

from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from flask import redirect, render_template, request, session
from functools import wraps
from app.helpers import *

def check_request_okay(request):
    if not request.form.get("symbol") or not request.form.get("amount"):
        return apology("Please provide all details")
    if request.form.get("amount").isnumeric() == False:
        return apology("Please provide a numerical value for amount")
    amount = int(request.form.get("amount"))
    if amount < 1:
        return apology("Please provide an amount greater than 1")
