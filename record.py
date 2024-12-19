class Record:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, record_str):
        id, name, age = record_str.strip().split(",")
        return cls(id, name, age)

    def __str__(self):
        return f"{self.id},{self.name},{self.age}"

    def is_valid(self):
        return (
            self.id.isdigit()
            and self.name.replace(" ", "").isalpha()
            and self.age.isdigit()
        )
