DEBUG = True

USERNAME = "root"
PASSWORD = "1008981904"
SERVER = "34.122.3.198"
DB = "smart_condominium"

SQLALCHEMY_DATABASE_URI = f"mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
