from ._anvil_designer import CreateMemTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class CreateMem(CreateMemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.repeating_panel_lendor.items=app_tables.lendor.search()
  def edit_membership(self):
    membership = self.tb_membrship.text
    anvil.server.call(
      'edit_membership',
      self.item,
      membership = self.tb_membrship.text,
      tenure = self.tb_tenure.text,
    )
    # Any code you write here will run before the form opens.
    app_tables.lendor.add_row(membership=membership,tenure=tenure)
    
    self.repeating_panel_lendor.items=app_tables.lendor.search()

    self.tb_membrship.text = ""
    self.tb_tenure.text = ""
    
    

  def button_1_click(self, **event_args):
    open_form('landingmodule.Home')

    
    
    
  
    






