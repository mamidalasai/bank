from ._anvil_designer import product1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class product1(product1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def link_1_click(self, **event_args):
    open_form('landingmodule.Home')

  
 
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    
  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    
  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    
  def radio_button_3_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    

  def button_1_click(self, **event_args):
    productid=self.text_box_1.text
    productname=self.text_box_2.text
    membership=self.drop_down_1.selected_value
    intrest=self.drop_down_5.selected_value
    max=self.drop_down_6.selected_value
    min=self.drop_down_7.selected_value
    tenure=self.drop_down_2.selected_value
    process=self.text_box_3.text
    extension=self.text_box_4.text
    defaulter=self.text_box_5.text
    extensionsallowed=self.drop_down_3.selected_value
    part=self.drop_down_4.selected_value
    foreclosure=self.text_box_6.text
    anvil.server.call('add_products', productid, productname, membership, process, extension, defaulter, intrest, max, min, tenure, extensionsallowed, part, foreclosure)
    Notification("submitted successfully").show()
       

  def button_2_click(self, **event_args):
    open_form('productmodule.product1.search')
    """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('landingmodule.Home')


  
  


  
    



    
    