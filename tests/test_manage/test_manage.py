# test check_requests_okay
import pytest
import flask
from app.manage.manageFunctions import *

def test_check_request_okay(mocker):
    # test what happens when symbol is empty:
    empty_symbol = ""
    request_mock = mocker.patch.object(flask, "request")
    request_mock.headers.get.return_value =  empty_symbol
    test = check_request_okay(request_mock)
    print(test)


