from db_operations import add, delete, update


def add_data():
    add("1,John Doe,24")
    add("2,John Doe,24")
    add("3,John Doe,24")
    add("4,John Doe,24")
    add("5,John Doe,24")
    add("6,John Doe,24")


def main():
    print("Welcome to MiniDB")
    add_data()
    update("5", "5,Doe John,25")
    delete("1")


if __name__ == "__main__":
    main()
