class DiaryEntry:

    # initialises task with specified contents.
    def __init__(self, contents):
        self.contents = contents
    
    # returns number of words when entry split by whitespace
    # returns length of lsit of words.
    # returns exception message if diary entry is empty string.
    def count_words(self):
        if not self.contents:
            raise Exception("Empty diary entry")
        else:
            number_of_words_in_entry = len(self.contents.split())
            return number_of_words_in_entry
    