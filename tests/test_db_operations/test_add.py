import unittest
from db_operations import add, update, delete, search
from record import Record
from constants import DB_NAME
import os


class TestAddOperation(unittest.TestCase):

    def setUp(cls):
        if os.path.exists(DB_NAME):
            os.remove(DB_NAME)

    def test_add_valid_record(self):
        record = Record.from_string("1,John Doe,25")
        result = add(record)
        self.assertTrue(result)

    def test_add_duplicate_id(self):
        record1 = Record.from_string("1,John Doe,25")
        record2 = Record.from_string("1,Doe John,25")

        add(record1)
        result = add(record2)
        self.assertFalse(result)

    def test_add_invalid_id_format(self):
        record = Record.from_string("a,John Doe,25")
        result = add(record)
        self.assertFalse(result)

    def test_add_invalid_name_format(self):
        record = Record.from_string("1,John123 Doe,25")
        result = add(record)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
