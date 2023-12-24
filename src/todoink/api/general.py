from todoink.api import bp
from flask import current_app as app
from flask import request


@bp.after_request
def after(response):
    app.logger.info(response)
    return response


@bp.before_request
def before():
    app.logger.info(request)