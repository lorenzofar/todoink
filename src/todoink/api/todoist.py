from flask import jsonify

from todoink.api import bp
from todoink.api.errors import error_response_from_exception
from todoink.controller import ControllerFactory

from dataclasses import asdict

@bp.route('/todoist/projects')
def get_todoist_projects():
    td_ctrl = ControllerFactory.todoist_ctrl()
    try:
        projects = td_ctrl.get_projects()
        return jsonify({"projects": [asdict(project) for project in projects]})
    except Exception as e:
        # Handle the exception here
        return error_response_from_exception(e)
