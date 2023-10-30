from ._anvil_designer import UserTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class User(UserTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    open_form('landingmodule.New_loan')

  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    open_form('landingmodule.borrower_page_landing_form.Exiting_loan')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('landingmodule.borrower_page_landing_form')

 




