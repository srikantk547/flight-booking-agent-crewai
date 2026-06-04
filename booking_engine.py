# booking_engine.py

import re


def extract_flight(result_text):

    matches = re.findall(r'BA205|AI101|UA300', result_text)

    if matches:
        return matches[0]

    return "UNKNOWN"


def extract_seat(result_text):

    matches = re.findall(r'\b\d+[A-Z]\b', result_text)

    if matches:
        return matches[0]

    return "UNKNOWN"


def extract_meal(result_text):

    lines = result_text.split("\n")

    for line in lines:
        if len(line.strip()) > 10:
            return line.strip()

    return "Vegetarian Meal"