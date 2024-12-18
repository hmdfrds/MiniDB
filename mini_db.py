from db_operations import add, delete


def add_data():
    add("1,John Doe,24")
    add("2,John Doe,24")
    add("3,John Doe,24")
    add("4,John Doe,24")
    add("5,John Doe,24")
    add("6,John Doe,24")


def main():
    print("Welcome to MiniDB")
    delete("3")


if __name__ == "__main__":
    main()
