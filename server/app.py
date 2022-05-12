# !!!!!!!!!!!!!  IMPORTANT  !!!!!!!!!!!!!!!!! #
#                                             #
#       Please, do not modify this file       #
#                                             #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

import pprint
from flask import Flask, request, Blueprint, jsonify

import generate_schedule_c.generate_schedule_c1
import generate_schedule_c.generate_schedule_c2
from generate_schedule_c import (
    generate_schedule_c1,
    generate_schedule_c2,
)

app = Flask(__name__)
api = Blueprint("api", __name__, url_prefix="/api")


@app.route("/")
def health():
    return {"status": "ok"}


@api.route("/generateScheduleC1", methods=["POST"])
def schedule_c1():
    """Call generate_schedule_c1 function."""
    request_data = request.get_json()
    result = generate_schedule_c1.generate_schedule_c1(
        request_data["multipliers"],
        request_data["transactions"],
    )
    return result


@api.route("/generateScheduleC2", methods=["POST"])
def schedule_c2():
    """Call generate_schedule_c2 function."""
    request_data = request.get_json()
    result = generate_schedule_c2.generate_schedule_c2(
        request_data["multipliers"],
        request_data["transactions"],
        request_data["jobs"],
    )
    return jsonify(result)


@app.errorhandler(404)
def not_found(error):
    return {"status": "not found"}, 404


@app.cli.command("generate-schedule-c1")
def cli_schedule_c1():
    result = generate_schedule_c.generate_schedule_c1.generate_schedule_c1(
        generate_schedule_c.generate_schedule_c1.MULTIPLIERS_1,
        generate_schedule_c.generate_schedule_c1.TRANSACTIONS_1,
    )
    pprint.pprint(result, indent=2)


@app.cli.command("generate-schedule-c2")
def cli_schedule_c1():
    result = generate_schedule_c.generate_schedule_c2.generate_schedule_c2(
        generate_schedule_c.generate_schedule_c2.MULTIPLIERS_2,
        generate_schedule_c.generate_schedule_c2.TRANSACTIONS_2,
        generate_schedule_c.generate_schedule_c2.JOBS_2,
    )
    pprint.pprint(result, indent=2)


app.register_blueprint(api)
