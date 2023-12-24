import logging
import traceback

from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

LOGGER = logging.getLogger()


def bad_request(message):
    return error_response(400, message=message)


def unauthorized(message):
    return error_response(401, message=message)


def not_found(message):
    return error_response(404, message=message)


def server_error(message):
    return error_response(500, message=message)


def not_implemented(message):
    return error_response(501, message=message)


def error_response(status_code, error_type='TECHNICAL', message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unkown error'), 'errorType': error_type}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def error_response_from_exception(exception: Exception):
    LOGGER.error(f"Error while processing request: {exception}")
    LOGGER.error(traceback.format_exc())
    # Get error code from exception, if present, otherwise use default 500
    error_code = 500
    if hasattr(exception, "error_code"):
        error_code = exception.error_code
    return error_response(status_code=error_code, message=str(exception))
