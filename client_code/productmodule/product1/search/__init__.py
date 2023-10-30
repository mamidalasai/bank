from ._anvil_designer import searchTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class search(searchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.repeating_panel_products.items=app_tables.products.search()

  def edit_products(self):
    productid = self.tb_productid.text
    productname = self.tb_productname.text
    membership = self.dd_membership.selected_value
    interest = self.dd_interest.selected_value
    max = self.dd_max.selected_value
    min = self.dd_min.selected_value
    tenure = self.dd_tenure.selected_value
    process = self.tb_process.text
    extension = self.tb_extension.text
    defaulter = self.tb_defaulter.text
    extallowed = self.dd_extensions.text
    part = self.tb_part.text
    foreclosure = self.foreclosure.text
    
    
    
    anvil.server.call(
      'edit_products',
      self.item,
      productid = self.tb_productid.text,
      productname = self.tb_productname.text,
      membership = self.dd_membership.selected_value,
      interest = self.dd_interest.selected_value,
      max = self.dd_max.selected_value,
      min = self.dd_min.selected_value,
      tenure = self.dd_tenure.selected_value,
      process = self.tb_process.text,
      extension = self.tb_extension.text,
      defaulter = self.tb_defaulter.text,
      extallowed = self.dd_extensions.text,
      part = self.tb_part.text,
      foreclosure = self.foreclosure.text,
      
    )

    app_tables.products.add_row(product_id=productid, product_name=productname, membership=membership)
    
    self.repeating_panel_products.items=app_tables.products.search()

    self.tb_productid.text = ""
    self.tb_productname.text = ""
    self.dd_membership.selected_value = self.dd_membership.items[0]
    self.dd_interest.selected_value = self.dd_interest.items[0]
    self.dd_max.selected_value = self.dd_max.items[0]
    self.dd_min.selected_value = self.dd_min.items[0]
    self.dd_tenure.selected_value = self.dd_tenure.items[0]
    self.tb_process.text = ""
    self.tb_extension.text = ""
    self.tb_defaulter.text = ""
    self.dd_extensions.selected_value = self.dd_extensions.items[0]
    self.dd_part.selected_value = self.dd_part.items[0]
    self.tb_foreclosure.text = ""
    
    

  

 


  def search(self, **event_args):
    self.repeating_panel_products.items = anvil.server.call(
      'search_products',
      self.text_box_search.text
    )

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('productmodule.product1')



 



  
  


  


  
 