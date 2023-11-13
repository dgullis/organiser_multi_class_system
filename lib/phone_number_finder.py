import re

class PhoneNumberFinder:
    
    #initialises class instance with specified diary.
    def __init__(self, diary):
        self.diary = diary
    
    # creates empty set to store found numbers.
    # fetches diary entries and extracts contents.
    # finds phone numbers in diary entrs contents and adds to the set.
    # returns a set of unique phone numbers.
    def see_phone_numbers(self):
        phone_numbers = set()
        diary_entries = self.diary.read_diary_entries()
        diary_contents = [entry.contents for entry in diary_entries]
        found_phone_numbers = re.findall(r'07\d{9}\b', str(diary_contents))
        phone_numbers.update(found_phone_numbers)
        return phone_numbers