import re

class Diary():

    #constructes empty list to store diary entries.
    def __init__(self):
        self.diary_entries = []
    
    # adds diary entry to list of entries.
    def add_diary_entry(self, diary_entry):
        self.diary_entries.append(diary_entry)
    
    # returns list of diary entries.
    def read_diary_entries(self):
        return self.diary_entries
    
    # calculates max amount of words that can be read based on parameters.
    # returns diary entry whose word count is closest to mac amount.
    # returns exception message if all entries too long.
    def read_entries_based_on_time(self, time, reading_speed):
        max_words_can_read = time * reading_speed
        entries_under_max_words = [entry for entry in self.diary_entries if entry.count_words() <= max_words_can_read]
        if not entries_under_max_words:
            raise Exception("No suitable entries based on time and reading speed")
        else:
            sorted_entries = sorted([[entry, entry.count_words()] for entry in entries_under_max_words] , key=lambda elem: elem[1], reverse=True)
        return sorted_entries[0][0].contents


