from ._anvil_designer import lendor_landing_page_formTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import landingmoduleg

class lendor_landing_page_form(lendor_landing_page_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_of_user.text = "Welcome " + landingmoduleg.name
    # Any code you write here will run before the form opens.

  def link_1_copy_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.openform')

  def link_1_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.Home')

  def link_1_copy_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.About')

  def link_1_copy_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.Services')

  def link_1_copy_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.Products')

  def link_1_copy_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.Home_direct')

  def button_2_click(self, **event_args):
    open_form('landingmodule.Home.regesterform')

  def button_1_click(self, **event_args):
    open_form('landingmodule.Home.regesterform')
