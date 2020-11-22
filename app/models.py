from app import db, ma

class log(db.Model):
    __tablename__ = 'log'
    __table_args__ = { 'extend_existing': True }
    key = db.Column("key", db.Integer, primary_key=True) # add this column
    id = db.Column("id", db.Integer)
    action = db.Column("action", db.Text)  
    stock = db.Column("stock", db.Text)
    amount = db.Column("amount", db.Integer)
    price_dealt = db.Column("price_dealt", db.Float)#is this right?
    date = db.Column("date", db.DateTime)

class portfolio(db.Model):
    __tablename__ = "portfolio"
    __table_args__ = { 'extend_existing': True }
    key = db.Column("key", db.Integer, primary_key=True) # add this column
    id = db.Column("id", db.Integer)
    stock = db.Column("stock", db.Text)
    number = db.Column("number", db.Integer)
    value = db.Column("value", db.Float)
    #action = db.Column("action", db.Text)  

class portfolioSchema(ma.ModelSchema):
    class Meta:
        model = portfolio

class users(db.Model):
    __tablename__ = "users"
    __table_args__ = { 'extend_existing': True }
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.Text)
    hash = db.Column("hash", db.Text)  
    cash = db.Column("cash", db.Float)

    def __repr__(self):
        return '<User {}>'.format(self.username)  
