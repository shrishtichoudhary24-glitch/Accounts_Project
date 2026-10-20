"""Flask app initialisation with security headers and CORS"""
import logging
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from service import config

app = Flask(__name__)
app.config.from_object(config)

# Security headers (Talisman) and CORS policy
talisman = Talisman(app)
CORS(app)

# pylint: disable=wrong-import-position
from service import routes, models  # noqa: F401,E402
from service.common import error_handlers  # noqa: F401,E402

models.init_db(app)
app.logger.setLevel(logging.INFO)
app.logger.info("Accounts service initialised")
