from lib.diary_entry import *
import pytest

"""
given entry
contents property is correctly set
"""
def test_properties_set():
    diary_entry = DiaryEntry("hello, my name is dan, how are you?")
    result = diary_entry.contents 
    assert result == "hello, my name is dan, how are you?"

"""
given one entry
count_words returns correct value
"""

def test_count_words():
    diary_entry = DiaryEntry("hello, my name is dan, how are you?")
    result = diary_entry.count_words()
    assert result == 8

"""
given empty string
retuns error message
"""

def test_count_words_empty_string():
    diary_entry = DiaryEntry("")
    with pytest.raises(Exception) as e:
        diary_entry.count_words()
    assert str(e.value) == "Empty diary entry"

