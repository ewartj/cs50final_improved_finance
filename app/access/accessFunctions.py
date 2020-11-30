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

def hasNumbers(inputString):
    """
    From:
    https://stackoverflow.com/questions/31083503/how-do-i-check-if-a-string-contains-any-numbers
    """
    if any(str.isdigit(c) for c in inputString) == True:
        return True
    else:
        return False

def hasSpecialCharecters(inputString):
    if set(inputString).difference(ascii_letters + digits):
        return True
    else:
        return False
