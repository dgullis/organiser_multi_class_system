from lib.diary import *
from lib.diary_entry import *
from lib.task import *
from lib.task_list import *
from lib.phone_number_finder import *
import pytest

"""
given diary entry with phone number in
#see_phone_numbers returns phone number
"""

def test_see_phone_number_one_entry_one_number():
    diary = Diary()
    phone_number_finder = PhoneNumberFinder(diary)
    diary_entry1 = DiaryEntry("hello, my name is dan my number is 07590395227")
    diary.add_diary_entry(diary_entry1)
    result = phone_number_finder.see_phone_numbers()
    assert result == {"07590395227"}

"""
given one entry with multiple phone numbers
#see_phone_numbers returns list of phone numbers
"""

def test_see_phone_number_one_number():
    diary = Diary()
    phone_number_finder = PhoneNumberFinder(diary)
    diary_entry1 = DiaryEntry("hello, my name is dan my number is 07590395227. hello my name is annabel my number is 07590395117")
    diary.add_diary_entry(diary_entry1)
    result = phone_number_finder.see_phone_numbers()
    assert result == {"07590395227", "07590395117"}

"""
given multiple entries, multiple phone numbers
#see_phone_numbers returns list of unique phone numbers
"""

def test_see_phone_number_multiple_entries_multiple_numbers():
    diary = Diary()
    phone_number_finder = PhoneNumberFinder(diary)
    diary_entry1 = DiaryEntry("hello, my name is dan my number is 07590395227")
    diary_entry2 = DiaryEntry("hello, my name is dan my number is 07590395337")
    diary_entry3 = DiaryEntry("hello, my name is dan my number is 07590395337")
    diary.add_diary_entry(diary_entry1)
    diary.add_diary_entry(diary_entry2)
    diary.add_diary_entry(diary_entry3)
    result = phone_number_finder.see_phone_numbers()
    assert result == {"07590395227", "07590395337"}