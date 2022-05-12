"""Basic tests."""

from pydantic import ValidationError

from tests.schemas import ScheduleC1Schema, ScheduleC2Schema


def test_post_generate_schedule_c1(client, multipliers_1, transactions_1):
    result = client.post(
        "/api/generateScheduleC1",
        json={"multipliers": multipliers_1, "transactions": transactions_1},
    )
    assert result.status_code == 200
    result_json = result.get_json(silent=True)
    assert result_json
    try:
        ScheduleC1Schema.parse_obj(result_json)
    except ValidationError as e:
        raise AssertionError(e)


def test_post_generate_schedule_c2(client, multipliers_2, transactions_2, jobs_2):
    result = client.post(
        "/api/generateScheduleC2",
        json={
            "multipliers": multipliers_2,
            "transactions": transactions_2,
            "jobs": jobs_2,
        },
    )
    assert result.status_code == 200
    result_json = result.get_json(silent=True)
    assert result_json
    try:
        ScheduleC2Schema.parse_obj(result_json)
    except ValidationError as e:
        raise AssertionError(e)
