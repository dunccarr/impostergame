import json

__all__ = ["Modal"]

class Modal:
    def __init__(self, path):
        self.path = path
        with open(path, "r") as f:
            self.modal = json.load(f)

    def render(self):
        print()
        print(self.modal["title"])
        option_id = 1
        for option in self.modal["options"]:
            print(f"{option_id}. {option}")
            option_id += 1

        return self.__checkinput__()

    def __checkinput__(self):
        while True:
            try:
                choice = int(input("Enter your choice...\t"))
                if 1 <= choice <= len(self.modal["options"]):
                    return choice
                raise IndexError()
            except ValueError:
                print("Invalid input. Please enter a number.")
            except IndexError:
                print("Choice out of range. Please correct your input.")
