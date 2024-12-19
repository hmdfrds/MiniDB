from constants import DB_NAME
import os
from record import Record
import logging
from file_handler import FileHandler


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
file_handler = FileHandler(DB_NAME)


def validate_id(func):
    def wrapper(id, *args, **kwargs):
        if not id.isdigit():
            print(f"ID must be a digit")
            return False
        return func(id, *args, **kwargs)

    return wrapper


# Add into file
# Id must be unique and a digit
# Return True if success add
def add(record):
    try:

        if not record.is_valid():
            print(f"Record {record} is not valid, no addition were made.")
            return False

        if not is_id_unique(record.id):
            print(f"Id {record.id} already exist, no addition were made.")
            return False

        file_handler.append_lines(str(record) + "\n")

    except Exception as e:
        logging.error(f"Error while writing to file: {e}")
        return False
    return True


# Search by ID or name
# Return data line if exist, None if not
def search(input):
    try:
        lines = file_handler.read_lines()
        for line in lines:
            record = Record.from_string(line)
            if is_id_equal(record.id, input) or is_name_equal(record.name, input):
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

        file_handler.write_lines(new_lines)
    except Exception as e:
        logging.error(f"Error while deleting record: {e}")
        return False
    return True


@validate_id
def update(id, record):
    try:
        if not record.is_valid():
            print(f"Record {record} is not valid, no updates were made.")
            return False
        lines = file_handler.read_lines()
        found = False
        new_lines = []
        for line in lines:
            if is_id_equal(line.split(",")[0], id):
                new_lines.append(str(record) + "\n")
                found = True
            else:
                new_lines.append(line)
        if not found:
            print(f"Id {id} not found, no updates were made.")
            return False

        if lines == new_lines:
            print(f"No changes in data, no updates were made.")
            return False
        file_handler.write_lines(new_lines)
    except Exception as e:
        logging.error(f"Error while updating record: {e}")
        return False
    return True


def is_id_unique(id):
    return search(id) == None


def is_id_equal(id, input):
    return input.isdigit() and id == input


def is_name_equal(name, input):
    return input.replace(" ", "").isalpha() and name == input
