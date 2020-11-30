import pytest
from  app.helpers import *
from werkzeug.security import generate_password_hash

# make and teardown rows/ tables
def addTestUser():
    username = "test"
    password = "test4$password"
    hash = generate_password_hash(password)
    db.session.execute("INSERT INTO users (username, hash, id, cash) VALUES (:username, :hash, :id, :cash)", {"username":username, "hash":hash, "id" : 10000000000, "cash" : 9999})
    db.session.commit()

def deleteTestUser():
    db.session.execute("DELETE FROM users WHERE id =:id", { "id" : 10000000000})
    db.session.commit()

def makeTestPortfolio():
    db.session.execute("CREATE TABLE IF NOT EXISTS testPortfolio ('id' integer, 'stock' text, 'number' integer, 'value' real, 'key' integer, PRIMARY KEY('key'))")

def addTestPortfolio():
    db.session.execute("INSERT INTO testPortfolio (id, stock, number, value, key) VALUES (:id, :stock, :number, :value, :key)", {"id" : 10000000000, "stock": "AMZN", "number":2, "value":1, "key" : 1})
    db.session.commit()

def deleteTestPortfolioRow():
    db.session.execute("DELETE FROM testPortfolio WHERE stock =:stock", { "stock" : "AMZN"})
    db.session.commit()

def deleteTestPortfolio():
    db.session.execute("DROP TABLE testPortfolio")
    db.session.commit()

# test individual functions

def testGet_cash(app):
    addTestUser()
    cash = get_cash(10000000000)
    deleteTestUser()
    assert cash == 9999

def testUpdate_Cash(app):
    addTestUser()
    old_cash = get_cash(10000000000)
    update_cash(10000000000, 1)
    cash = get_cash(10000000000)
    deleteTestUser()
    assert old_cash == 9999
    assert cash == 1

def testIndex_portfolio(app):
    makeTestPortfolio()
    deleteTestPortfolioRow()
    addTestPortfolio()
    portfoli = db.session.execute("SELECT stock, number, value FROM testPortfolio WHERE id= :id", { "id" : 10000000000})
    portfolio_db = SQLalchemy_query_pandas(portfoli)
    deleteTestPortfolioRow()
    deleteTestPortfolio()
    assert portfolio_db.to_dict('index') == {0: {'stock': 'AMZN', 'number': 2, 'value': 1.0}}

def test_isOwned(app):
    makeTestPortfolio()
    deleteTestPortfolioRow()
    addTestPortfolio()
    isOwned = db.session.execute("SELECT * FROM testPortfolio WHERE id= :id AND stock= :stock", { "id" : 10000000000, "stock" : "AMZN"})
    test_righcols = resultProxy_2_dict(isOwned)
    print(test_righcols)
    deleteTestPortfolioRow()
    deleteTestPortfolio()
    assert test_righcols == {'id': 10000000000, 'stock': 'AMZN', 'number': 2, 'value': 1.0, 'key': 1}

