from lib.diary import *
from lib.diary_entry import *
from lib.task import *
from lib.task_list import *
from lib.phone_number_finder import *
import pytest

"""
given entry
contents property is set
comepleted status is set to false
"""

def test_correct_properties_set():
    task = Task("walk the dog")
    assert task.contents == "walk the dog"
    assert task.completed == False

"""
given task
#see_tasks returns that taks
"""

def test_added_task_seen_in_list():
    task_list = TaskList()
    task_1 = Task("walk the cat")
    task_list.add_task(task_1)
    result = task_list.see_incomplete_tasks()
    assert result == ["walk the cat"]

def test_see_tasks():
    task_list = TaskList()
    task_1 = Task("walk the cat")
    task_list.add_task(task_1)
    result = task_list.see_incomplete_tasks()
    assert result == ["walk the cat"]

"""
given multiple tasks
#see_tasks returns lsit of incomplete tasks
"""

def test_see_tasks_returns_multiple_tasks():
    task_list = TaskList()
    task_1 = Task("walk the cat")
    task_2 = Task("walk the dog")
    task_3 = Task("water the plants")
    task_list.add_task(task_1)
    task_list.add_task(task_2)
    task_list.add_task(task_3)
    result = task_list.see_incomplete_tasks()
    assert result == ["walk the cat", "walk the dog", "water the plants"]


"""
given multiple tasks
given one task marked complete
#mark_task_complete returns list of incomplete tasks
"""
def test_multiple_tasks_one_marked_complete_return_incomplete_tasks():
    task_list = TaskList()
    task_1 = Task("walk the cat")
    task_2 = Task("walk the dog")
    task_3 = Task("water the plants")
    task_list.add_task(task_1)
    task_list.add_task(task_2)
    task_list.add_task(task_3)
    task_2.mark_task_complete()
    result = task_list.see_incomplete_tasks()
    assert result == ["walk the cat", "water the plants"]

