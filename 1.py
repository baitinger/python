class Data:

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def to_number(cls, date):
        my_list = [el for el in list(date) if el.isdigit()]
        return ''.join(my_list)

    @staticmethod
    def validate(date):
        date = date.split("-")
        if int(date[1]) in [1, 3, 5, 7, 8, 10, 12]:
            return "Date is OK" if 1 <= int(date[0]) <= 31 else "Date isn't okay"
        elif int(date[1]) in [4, 6, 9, 11]:
            return "Date is OK" if 1 <= int(date[0]) <= 30 else "Date isn't okay"
        else:
            return "Date is OK" if 1 <= int(date[0]) <= 28 and 1 <= int(date[1]) <= 12 else "Date isn't okay"


new_data = Data("08-11-1994")
print(new_data.date)
print(Data.to_number("08-11-1994"))
print(Data.validate("29-02-1994"))
