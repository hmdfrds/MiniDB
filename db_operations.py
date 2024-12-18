from constants import DB_NAME, ID_INDEX, NAME_INDEX

import os


# Add into file
# Id must be unique and a digit
# Return True if success add
def add(data):
    id = data.split(",")[ID_INDEX].strip()
    if not is_id_valid(id):
        return False
    try:
        with open(DB_NAME, "a") as file:
            file.write(data + "\n")
    except Exception as e:
        print(f"Error while writing to file: {e}")
        return False
    return True


# Search by ID or name
# Return data line if exist, None if not
def search(input):
    input = input.strip()
    if os.path.exists(DB_NAME):
        with open(DB_NAME) as file:
            for line in file:
                data = line.split(",")
                if is_id_equal(data[ID_INDEX], input) or is_name_equal(
                    data[NAME_INDEX], input
                ):
                    return line
    return None


# Return True if success delete
def delete(id):
    id = id.strip()
    if not id.isdigit():
        print(f"Invalid Id: {id}")
        return False

    if os.path.exists(DB_NAME):
        with open(DB_NAME, "r+") as file:
            new_data = []
            id_found = False

            for line in file:
                if not is_id_equal(line.split(",")[0], id):
                    new_data.append(line)
                else:
                    id_found = True

            if not id_found:
                print(f"Id {id} not found")
                return False
            file.seek(0)
            file.truncate()
            for line in new_data:
                file.write(line)

    return True


def is_id_valid(id):
    if not id.isdigit():
        print(f"ID must be a digit")
        return False
    return is_id_unique(id)


def is_id_unique(id):
    if search(id) == None:
        return True
    else:
        print(f"id {id} already exist")
        return False


def is_id_equal(id, input):
    return input.isdigit() and id == input


def is_name_equal(name, input):
    return input.isalpha() and name == input
