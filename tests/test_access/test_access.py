#Test hasNumber:Charecter
#Test hasSpecial
#   check its a number
#   checks its not a letter
#   check its a special charecter
import pytest
from app.access.accessFunctions import *

def test_hasNumber():
    number = hasNumbers("2")
    letter = hasNumbers("test")
    special = hasNumbers("$")
    assert number == True
    assert letter == False
    assert special == False

def test_hasSpecial():
    number = hasSpecialCharecters("2")
    letter = hasSpecialCharecters("test")
    special = hasSpecialCharecters("$")
    assert number == False
    assert letter == False
    assert special == True
