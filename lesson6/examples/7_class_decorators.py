from datetime import datetime, timedelta


class Example:
    __counter = 1
    __hidden_attribute = "I'm hidden"

    # def __init__(self):
    #     if self.__up_counter() > 4:
    #         raise Exception("Too many classes created!")

    @property
    def hidden(self):
        if self.__counter < 2:
            return self.__hidden_attribute + ", but accessible!"
        else:
            raise AssertionError('wrong condition')

    @staticmethod
    def static():
        return datetime.today().strftime('%d:%m:%Y %H:%m:%s')
        # print("Call this method without instance, its ok!")

    @staticmethod
    def get_current_datetime():
        return datetime.now()

    @classmethod
    def add_date(cls, days):
        current_date = cls.get_current_datetime()
        return str(current_date + timedelta(days=days))


# staticmethod
# print(Example.static())

# property
# ex = Example()
# print(ex.hidden)

# classmethod
print(Example.add_date(5))
