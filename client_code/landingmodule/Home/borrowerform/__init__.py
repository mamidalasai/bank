from ._anvil_designer import borrowerformTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import landingmoduleg


class borrowerform(borrowerformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def home_btn_click(self, **event_args):
    open_form('landingmodule.Home')

  def submitbtt_click(self, **event_args):
    open_form('landingmodule.borrower_page_landing_form')

  def clear_click(self, **event_args):
    print("this button need to done")
    

    

    





