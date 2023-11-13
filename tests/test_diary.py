from lib.diary import *
from lib.diary_entry import *
from lib.task import *
from lib.task_list import *
from lib.phone_number_finder import *
import pytest

"""
initially no entries
#read_diary_entries returns empty list
"""

def test_initially_no_entries():
    diary = Diary()
    result = diary.read_diary_entries()
    assert result == []

"""
given a diary entry
this is reflected in property of diary
"""

def test_add_diary_entry():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Hello, my name is dan. How are you?")
    diary.add_diary_entry(diary_entry_1)
    result = diary.diary_entries
    assert result == [diary_entry_1]

"""
given multiple diary entries
#read_diary_entries returns entries as list
"""

def test_read_diary_entry():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Hello, my name is dan. How are you?")
    diary_entry_2 = DiaryEntry("Hello, my name is Annabel. How are you?")
    diary_entry_3 = DiaryEntry("Hello, my name is Fiona. How are you?")
    diary.add_diary_entry(diary_entry_1)
    diary.add_diary_entry(diary_entry_2)
    diary.add_diary_entry(diary_entry_3)
    result = diary.read_diary_entries()
    assert result == [diary_entry_1, diary_entry_2, diary_entry_3]

"""
given multiple diary entries
given time and reading speed
#read_entries_based_on_time returns entry which is closest to max words
user can read given the time and reading speed
"""

def test_reading_entries_based_on_time_and_speed():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Hello, my name is dan. I am completing the golden square principal challanges")
    diary_entry_2 = DiaryEntry("Hello, my name is Annabel. I am ill at home sitting with the cats")
    diary_entry_3 = DiaryEntry("Hello, my name is Fiona. I am in nottingham probably reading a book. I will walk the dog later.")
    diary.add_diary_entry(diary_entry_1)
    diary.add_diary_entry(diary_entry_2)
    diary.add_diary_entry(diary_entry_3)
    result = diary.read_entries_based_on_time(2, 10)
    assert result == "Hello, my name is Fiona. I am in nottingham probably reading a book. I will walk the dog later."

"""
where all entries are too long to read given time and reading speed
#exception is raised
"""

def test_no_suitable_entries_based_on_length():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Hello, my name is dan. I am completing the golden square principal challanges")
    diary_entry_2 = DiaryEntry("Hello, my name is Annabel. I am ill at home sitting with the cats")
    diary_entry_3 = DiaryEntry("Hello, my name is Fiona. I am in nottingham probably reading a book. I will walk the dog later.")
    diary.add_diary_entry(diary_entry_1)
    diary.add_diary_entry(diary_entry_2)
    diary.add_diary_entry(diary_entry_3)
    with pytest.raises(Exception) as e:
        diary.read_entries_based_on_time(1, 10)
    assert str(e.value) == "No suitable entries based on time and reading speed"

