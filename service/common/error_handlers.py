"""JSON error handlers"""
from flask import jsonify
from service import app
from service.models import DataValidationError
from service.common import status


@app.errorhandler(DataValidationError)
def request_validation_error(error):
    """Handle validation errors"""
    return jsonify(status=400, error="Bad Request", message=str(error)), status.HTTP_400_BAD_REQUEST


@app.errorhandler(404)
def not_found(error):
    """Handle 404"""
    return jsonify(status=404, error="Not Found", message=str(error)), status.HTTP_404_NOT_FOUND


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405"""
    return jsonify(status=405, error="Method not Allowed", message=str(error)), status.HTTP_405_METHOD_NOT_ALLOWED


@app.errorhandler(500)
def internal_error(error):
    """Handle 500"""
    return jsonify(status=500, error="Internal Server Error", message=str(error)), status.HTTP_500_INTERNAL_SERVER_ERROR
