import unittest
import os

from nose.tools import *
from adventure.adventure import Adventure
from page.page import Page
from choice.choice import Choice

class AdventureTestCases(unittest.TestCase):
    def setup_class():
        print ("Setting Up")

    def teardown_class():
        print ("Tearing Down")

    def create_adventure(self):
        page1 = Page(text="Page1")
        choice1 = Choice(text="choice1")
        page2 = Page(text="Page2")
        choice2 = Choice(text="choice2")
        adventure = Adventure([page1, page2], [choice1, choice2], page1, 
                "test_save_file")
        return(adventure)
        

    def adventure_creation_test(self):
        """Test the creation of a adventure"""
        adventure = Adventure()

    def adventure_creation_with_pages_test(self):
        """Test Adventure creation with initial pages"""
        page1 = Page(text="Page1")
        adventure = Adventure([page1])
        assert_true(adventure._pages[0]._text == "Page1")

    def adventure_creation_with_initial_page_test(self):
        """Test Adventure creation with initial page"""
        page1 = Page(text="Page1")
        adventure = Adventure([page1], start_page=page1)
        assert_true(adventure._start_page._text == "Page1")

    def adventure_creation_with_choices_test(self):
        """Test Adventure creation with initial choices"""
        choice = Choice(text="choice1")
        adventure = Adventure(choices=[choice])
        assert_true(adventure._choices[0]._text == "choice1")

    def save_adventure_test(self):
        """docstring for save_adventure"""
        adventure = self.create_adventure()
        adventure.write()
        assert_true(os.path.exists("./test_save_file"))
        adventure.delete()

    def delete_adventure_test(self):
        """docstring for save_adventure"""
        adventure = self.create_adventure()
        adventure.write()
        adventure.delete()
        assert_true(not os.path.exists("./test_save_file"))
