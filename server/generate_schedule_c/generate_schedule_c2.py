from pprint import pprint


def generate_schedule_c2(multipliers, transactions, jobs):
    """Schedule C calculation for multiple jobs with additional categories."""
    return [
        {
            "meal": 0,
            "car": 0,
            "payment": 0,
            "home": 0,
            "phone": 0,
        },
        {
            "meal": 0,
            "car": 0,
            "payment": 0,
            "home": 0,
            "phone": 0,
        },
    ]


MULTIPLIERS_2 = {
    "meal": 0.5,
    "car": 0.4,
    "home": 0.1,
    "phone": 0.5,
}
TRANSACTIONS_2 = [
    {
        "id": "t1",
        "category": "meal",
        "amount": 32.5,
        "jobId": "j1",
    },
    {
        "id": "t2",
        "category": "meal",
        "amount": 51.33,
        "jobId": "j2",
    },
    {
        "id": "t3",
        "category": "car",
        "amount": 300.02,
        "jobId": "j2",
    },
    {
        "id": "t4",
        "category": "car",
        "amount": 350.61,
        "jobId": "j2",
    },
    {
        "id": "t5",
        "category": "meal",
        "amount": 49.68,
        "jobId": "j1",
    },
    {
        "id": "t6",
        "category": "payment",
        "amount": 45.0,
        "jobId": "j1",
    },
    {
        "id": "t7",
        "category": "home",
        "amount": 550.0,
        "jobId": "j1",
    },
    {
        "id": "t8",
        "category": "phone",
        "amount": 81.98,
        "jobId": "j2",
    },
    {
        "id": "t9",
        "category": "phone",
        "amount": 81.98,
        "jobId": "j2",
    },
]

JOBS_2 = [
    {
        "id": "j1",
    },
    {
        "id": "j2",
    },
]


if __name__ == "__main__":
    pprint(generate_schedule_c2(MULTIPLIERS_2, TRANSACTIONS_2, JOBS_2), indent=2)
