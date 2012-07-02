import unittest

from nose.tools import *
from choice.choice import Choice

class ChoiceTestCases(unittest.TestCase):
    def setup_class():
        print ("Setting Up")
    def teardown_class():
        print ("Tearing Down")
    def choice_creation_test(self):
        """Test the creation of a choice"""
        choice = Choice()
    def choice_creation_with_text_test(self):
        """Test creation with initial text"""
        choice = Choice(text="A choice with initial text")
        assert_true(choice._text == "A choice with initial text")
    def set_choice_text_test(self):
        """Test text set method"""
        choice = Choice()
        choice.set_text("A choice with text set later")
        assert_true(choice._text == "A choice with text set later")
    def set_choice_text_overwrite(self):
        """Test text set/overwrite method"""
        choice = Choice(text="A choice with initial text")
        choice.set_text("This text overwrites the initial text")
        assert_true(choice._text == "This text overwrites the initial text")
    def get_choice_text_test(self):
        """Test creation with initial text"""
        choice = Choice(text="A choice with initial text")
        assert_true(choice.get_text() == "A choice with initial text")


