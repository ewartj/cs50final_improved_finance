import os
from tempfile import mkdtemp

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SESSION_FILE_DIR = mkdtemp()
    # SESSION_PERMANENT = False
    # SESSION_TYPE = "filesystem"
    # PREFERRED_URL_SCHEME = 'https'
    # DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'finance.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_KEY = "pk_75bffab4799745718863931100e83a62"
    #    # NB: THIS ISN'T WORKING NEEDED TO DO MANUALY, WILL NEED TO TEST FOR THIS
    #  export API_KEY=pk_75bffab4799745718863931100e83a62
