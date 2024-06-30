from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException


def error_response(message: str, status_code: int):
    return jsonify({"error": message}), status_code


def register_error_handlers(app: Flask):
    @app.errorhandler(400)
    def bad_request(e):
        if isinstance(e, HTTPException):
            return error_response(e.description, e.code)
        return error_response("Bad request", 400)

    @app.errorhandler(404)
    def not_found(e):
        return error_response("Not found", 404)

    @app.errorhandler(405)
    def method_not_allowed(e):
        return error_response("Method not allowed", 405)

    @app.errorhandler(415)
    def unsupported_media_type(e):
        return error_response("Content-Type must be application/json", 415)

    @app.errorhandler(500)
    def internal_server_error(e):
        return error_response("An internal server error occurred", 500)

    @app.errorhandler(Exception)
    def unhandled_exception(e):
        app.logger.error(f"An unhandled exception occurred: {str(e)}")
        return internal_server_error(e)
