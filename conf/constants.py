import os
from dotenv import load_dotenv

load_dotenv()

SQL_HOST = os.environ.get("SQL_HOST", None)
SQL_HOSTNAME = os.environ.get("SQL_HOSTNAME", None)
SQL_USERNAME = os.environ.get("SQL_USERNAME", None)
SQL_PASSWORD = os.environ.get("SQL_PASSWORD", None)
SQL_DATABASE = os.environ.get("SQL_DATABASE", None)
SQL_PORT = os.environ.get("SQL_PORT", None)

SSH_HOST = os.environ.get("SSH_HOST", None)
SSH_USER = os.environ.get("SSH_USER", None)
SSH_PORT = os.environ.get("SSH_PORT", None)
KEY_FILE = os.environ.get("KEY_FILE", None)

MAGENTO_URL = os.environ.get("MAGENTO_URL", None)
AUTH = os.environ.get("AUTH", None)
API_URL = 'rest/V1/products/attributes/{}/options'.format(os.environ.get("ATTRIBUTE_CODE", None))
PATH_FILE = os.environ.get("PATH_FILE", None)
BODY = '{"option": {"label": "{value}","value": "{value}","sort_order": 0,"is_default": false}}'
