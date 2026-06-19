from datetime import datetime


def generate_ticket_number(
    count: int
):
    year = datetime.now().year

    return (
        f"EVT-{year}-"
        f"{str(count + 1).zfill(6)}"
    )