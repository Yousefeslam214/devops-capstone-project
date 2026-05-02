"""
Accounts service package.
Includes CORS policies and Talisman security headers configuration.
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)

# Security headers (Talisman) and CORS policies
Talisman(app, force_https=False, content_security_policy=None)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    """Service root endpoint."""
    return (
        jsonify(
            {
                "name": "accounts",
                "version": "1.0.0",
                "message": "Accounts service running",
            }
        ),
        200,
    )
