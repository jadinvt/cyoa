import unittest

from nose.tools import *
from page.page import Page
from choice.choice import Choice

class BasicPageTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print ("Setting Up")
    def teardown_class():
        print ("Tearing Down")
    def page_creation_test(self):
        """Test the creation of a page"""
        page = Page()
    def page_creation_with_text_test(self):
        """Test creation with initial text"""
        page = Page(text="A page with initial text")
        assert_true(page._text == "A page with initial text")
    def page_creation_with_choices(self):
        """Test creation with initial text"""
        choice = Choice("choice text")
        page = Page(text="A page with initial text", choices=[choice])
        assert_true(page._choices[0]._text == "choice text")
    def set_page_text_test(self):
        """Test text set method"""
        page = Page()
        page.set_text("A page with initial text")
        assert_true(page._text == "A page with initial text")
    def set_page_text_overwrite(self):
        """Test text set/overwrite method"""
        page = Page(text="A page with initial text")
        page.set_text("This text overwrites the initial text")
        assert_true(page._text == "This text overwrites the initial text")
    def get_page_text_test(self):
        """Test creation with initial text"""
        page = Page(text="A page with initial text")
        assert_true(page.get_text() == "A page with initial text")
    def set_page_choice_test(self):
        page = Page(text="A page with initial text")
        choice = Choice("choice1")
        page.set_choices([choice])
        assert_true(page._choices[0]._text == "choice1")


