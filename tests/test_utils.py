import pytest
from utils import get_data, get_filtered, get_last_values, get_formatted_data, encode_bill_info


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert len(data) == 3


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x["date"] for x in data] == ['019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572', '2018-03-23T10:45:06.972075', '2019-04-04T23:20:05.206878']

def test_formatted_data(test_data):
    data = get_formatted_data(test_data)
    print(data)
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счёт **9589\n31957.58 руб', '03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счёт **5560\n8221.37 USD', '30.06.2018 Перевод организации\nСчет 7510 68** **** 6952 -> Счет **6702\n9824.07 USD', '23.03.2018  Открытие вклада\n -> Счет **2431\n48223.05 руб', '04.04.2019 Перевод со счета на счет\nСчет 1970 86** **** 8542 -> Счет **4188\n79114.93 USD']

@pytest.mark.parametrize("test_input,expected", [
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Platinum 1596837868705199", "Visa Platinum 1596 83** **** 5199")
])


def test_encode_bill_info(test_input, expected):
    assert encode_bill_info(test_input) == expected