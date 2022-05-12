from pprint import pprint


def generate_schedule_c1(multipliers, transactions):
    """Base Schedule C calculation."""
    return {
        "meal": 0,
        "car": 0,
        "payment": 0,
    }


MULTIPLIERS_1 = {
    "meal": 0.5,
    "car": 0.4,
}

TRANSACTIONS_1 = [
    {
        "id": "t1",
        "category": "meal",
        "amount": 32.5,
    },
    {
        "id": "t2",
        "category": "meal",
        "amount": 51.33,
    },
    {
        "id": "t3",
        "category": "car",
        "amount": 300.02,
    },
    {
        "id": "t4",
        "category": "car",
        "amount": 350.61,
    },
    {
        "id": "t5",
        "category": "meal",
        "amount": 49.68,
    },
    {
        "id": "t6",
        "category": "payment",
        "amount": 45.0,
    },
]


if __name__ == "__main__":
    pprint(generate_schedule_c1(MULTIPLIERS_1, TRANSACTIONS_1), indent=2)
