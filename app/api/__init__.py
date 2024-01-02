from flask import Blueprint
from flask import current_app as cdp_app


health_check_bp = Blueprint('health_check_bp', __name__)


@health_check_bp.route("/check")
def check_health():
    """ Health ApI"""
    cdp_app.logger.info("Health check API was called.")
    return {"success": True, "data": "Server is running!"}
