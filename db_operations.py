from constants import DB_NAME, ID_INDEX, NAME_INDEX
import os
import logging
from file_handler import FileHandler


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
file_handler = FileHandler(DB_NAME)


def validate_id(func):
    def wrapper(id, *args, **kwargs):
        id = id.strip()
        if not id.isdigit():
            print(f"ID must be a digit")
            return False
        return func(id, *args, **kwargs)

    return wrapper


# Add into file
# Id must be unique and a digit
# Return True if success add
def add(data):
    try:
        id = data.split(",")[ID_INDEX].strip()
        if not id.isdigit() or not is_id_unique(id):
            return False
        file_handler.append_lines(data + "\n")
    except Exception as e:
        logging.error(f"Error while writing to file: {e}")
        return False
    return True


# Search by ID or name
# Return data line if exist, None if not
def search(input):
    try:
        input = input.strip()
        lines = file_handler.read_lines()
        for line in lines:
            data = line.split(",")
            if is_id_equal(data[ID_INDEX], input) or is_name_equal(
                data[NAME_INDEX], input
            ):
                return line
    except Exception as e:
        logging.error(f"Error while searching record: {e}")
    return None


# Return True if success delete
@validate_id
def delete(id):
    try:
        lines = file_handler.read_lines()
        new_lines = [line for line in lines if not is_id_equal(line.split(",")[0], id)]

        if len(lines) == len(new_lines):
            print(f"Id {id} not found, no delete were made.")
            return False

        file_handler.write_lines(lines)
    except Exception as e:
        logging.error(f"Error while deleting record: {e}")
        return False
    return True


@validate_id
def update(id, data):
    try:
        lines = file_handler.read_lines()

        new_lines = [
            id + "," + data + "\n" if is_id_equal(line.split(",")[0], id) else line
            for line in lines
        ]

        if lines == new_lines:
            print(f"Id {id} not found, no updates were made.")
            return False

        file_handler.write_lines(new_lines)
    except Exception as e:
        logging.error(f"Error while updating record: {e}")
        return False
    return True


def is_id_unique(id):
    if search(id) == None:
        return True
    else:
        print(f"id {id} already exist")
        return False


def is_id_equal(id, input):
    return input.isdigit() and id == input


def is_name_equal(name, input):
    return input.isalpha() and name.strip() == input.strip()
