import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get(
        'BLOB_ACCOUNT') or 'cloudappstoragedemo'
    BLOB_STORAGE_KEY = os.environ.get(
        'BLOB_STORAGE_KEY') or '/wPzSFcHW+P4Vh83IzPROHafbdS8/pnplZOWRG5RU3r20sO4pRxVSTnO3NDC5IBviNhqP1X1/RCh+ASte2xyCg=='
    BLOB_CONTAINER = os.environ.get(
        'BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get(
        'SQL_SERVER') or 'cloud-app.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'app-db'
    SQL_USER_NAME = os.environ.get(
        'SQL_USER_NAME') or 'sqladmin'
    SQL_PASSWORD = os.environ.get(
        'SQL_PASSWORD') or 'sql@dmin123'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + \
        SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + \
        SQL_DATABASE + '?driver=ODBC+Driver+18+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "slo8Q~U96P.YDRTt1nQaI.xHIsMcydQ4A2z1SbiM"
    if not CLIENT_SECRET:
        raise ValueError("Need to define CLIENT_SECRET environment variable")

    # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/common"
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "7717a4c1-78e3-411d-8bb4-efef504b4fb0"

    # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    REDIRECT_PATH = "/getAToken"

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]  # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
