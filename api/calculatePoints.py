
from math import ceil, floor
from datetime import datetime


def calculate_points(receipt):
    name_points = get_name_points(receipt)
    round_dollar_points = get_round_dollar_points(receipt)
    multiple_25_points = get_multiple_25_points(receipt)
    number_of_items_points = get_number_of_items_points(receipt)
    desc_price_points = get_desc_price_points(receipt)
    time_points = get_purchase_time_points(receipt)
    date_points = get_purchase_date_points(receipt)

    total_points = (
        name_points +
        round_dollar_points +
        multiple_25_points +
        number_of_items_points +
        desc_price_points +
        time_points +
        date_points
    )

    return total_points


def get_name_points(receipt):
    retailer = receipt["retailer"].replace(" ", "")  # Remove white spaces
    retailer = ''.join(filter(str.isalnum, retailer))  # Remove non-alphanumeric chars
    return len(retailer)


def get_round_dollar_points(receipt):
    total=0
    for item in receipt["items"]:
        total+=float(item["price"])
    if total.is_integer():
        return 50 
    return 0



def get_multiple_25_points(receipt):
    total = float(receipt["total"])
    if total % 0.25 == 0:
        return 25 
    return 0


def get_number_of_items_points(receipt):
    items_count = len(receipt["items"])
    return (items_count // 2) * 5


def get_desc_price_points(receipt):
    desc_price_points = 0
    for item in receipt["items"]:
        short_desc_length = len(item["shortDescription"].strip())
        if short_desc_length % 3 == 0:
            desc_price_points += ceil(float(item["price"]) * 0.2)
    return desc_price_points


def get_purchase_time_points(receipt):
    time = int(receipt["purchaseTime"].replace(":", ""))
    if 1400 < time < 1600:
        return 10 
    return 0


def get_purchase_date_points(receipt):
    purchase_date = datetime.strptime(receipt["purchaseDate"], "%Y-%m-%d")
    if purchase_date.day % 2 != 0:
        return 6
    return 0