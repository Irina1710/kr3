from datetime import datetime

from src.utils import get_filtered_data, get_last_values, get_formatted_data, encode_bill_info


def test_get_filtered_data(test_data):
    filtered_data = get_filtered_data(test_data)
    for item in filtered_data:
        assert item["state"] == "EXECUTED"


def test_get_last_values(test_data):
    count_last_values = 3
    last_values = get_last_values(test_data, count_last_values)
    assert len(last_values) == count_last_values
    dates = [datetime.fromisoformat(item["date"]) for item in last_values]
    assert dates == sorted(dates, reverse=True)


def test_encode_bill_info():
    bill_info = "Maestro 1596837868705199"
    encoded_info = encode_bill_info(bill_info)
    assert encoded_info == "Maestro 1596 83** **** 5199"

    bill_info = "Счет 75106830613657916952"
    encoded_info = encode_bill_info(bill_info)
    assert encoded_info == "Счет **6952"


def test_get_formatted_data(test_data):
    formatted_data = get_formatted_data(test_data)
    assert isinstance(formatted_data, list)
    assert len(formatted_data) == len(test_data)