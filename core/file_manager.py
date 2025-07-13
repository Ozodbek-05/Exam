import csv
import os


def writerows(filename: str, data: list[list]) -> None:
    """
    write given list of data to csv
    :param filename: file name
    :param data: list of data
    :return: None
    """
    path = f"core/data/{filename}.csv"
    with open(file=path, mode="w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def read(filename: str) -> list:
    path = f"core/data/{filename}.csv"
    if os.path.exists(path):
        with open(path, mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            return list(reader)
    return []


def append(filename: str, data: list) -> None:
    """
    write given list of data to csv
    :param filename: file name
    :param data: list of data
    :return: None
    """
    path = f"core/data/{filename}.csv"
    with open(file=path, mode="a", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
