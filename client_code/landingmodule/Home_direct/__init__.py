from ._anvil_designer import Home_directTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Home_direct(Home_directTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def sign_in(self, **event_args):
    open_form('landingmodule.openform')
    """This method is called when the link is clicked"""

  def login(self, **event_args):
    open_form('landingmodule.Login')
    """This method is called when the link is clicked"""

  def link_1_copy_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('productmodule.product1')

  def link_1_click(self, **event_args):
   open_form('landingmodule.CreateMem')

  def link_2_click(self, **event_args):
   open_form('ROI.Manage_ROI')



    

  

