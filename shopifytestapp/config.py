#the config that is not inside instance
class Config(object):
    DATABASE_URI="some random parameters "
    MERCHANT_ID="SAMPLE"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://root@127.0.0.1/shopifytest"
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    MERCHANT_ID="oh*76&%^Gj"

    

class Test_config(Config):
    DATABASE_URL="Test Connection parameters"