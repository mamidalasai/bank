from ._anvil_designer import LoanTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Loan(LoanTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('cancel')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    loan_extension=self.text_box_1.text
    loan_id=self.text_box_2.text
    loan_amount=self.text_box_3.text
    loan_availed_date=self.text_box_10.text
    tenure=self.text_box_5.text
    intrest=self.text_box_4.text
    processing_fee=self.text_box_6.text
    loan_repayment_amount=self.text_box_8.text
    loan_due_amount=self.text_box_9.text
    select=self.drop_down_1.selected_value
    anvil.server.call('add_loan',loan_extension,loan_id,loan_amount,loan_availed_date,tenure,intrest,processing_fee,loan_repayment_amount,loan_due_amount,select)
    alert('sumitted')

   