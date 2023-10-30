from ._anvil_designer import Manage_ROITemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Manage_ROI(Manage_ROITemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('landingmodule.Home')

  def calculate_click(self, **event_args):
    #initial_investment = float(self.tb_initial.text)
    #tenure = float(self.tb_tenure.text)
   # membership_type = str(self.tb_member.text)
   # interest_rate = float(self.tb_interest_rate.text)
    initial_investment = self.tb_initial.text
    tenure = self.tb_tenure.text
    membership_type = self.tb_member.text
    interest_rate = self.tb_interest_rate.text
    
    

    anvil.server.call('add_return_on_investment',initial_investment,tenure,membership_type,interest_rate)
    initial_investment = float(self.tb_initial.text)
    tenure = float(self.tb_tenure.text)
    membership_type = str(self.tb_member.text)
    interest_rate = float(self.tb_interest_rate.text)

    
    future_value = int(initial_investment*(1+interest_rate/100))*int(tenure/12)
    ROI = [(future_value-initial_investment)/initial_investment]*100

    #final_value = int(initial_investment * (1 + (interest_rate / 100)) * int(tenure / 12))
    #ROI = ((final_value - initial_investment) / initial_investment) * 100
    #FROI = ROI*int(initial_investment)/100
    
  
  


    #output
    self.output_tb.text = f"Your ROI is {ROI[0]}%"
    self.output_tb1.text = f"Your Future value is {future_value}"
    #self.output_tb.text = f"Your FROI is {FROI[0]}"

    

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('ROI.Form1')



 








  




