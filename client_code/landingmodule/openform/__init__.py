from ._anvil_designer import openformTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import landingmoduleg


class openform(openformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  
  def submitbtt_click(self, **event_args):
    # Get the input values
    first_name = self.firstname.text
    last_name = self.lastname.text
    email_id = self.email.text
    mobile = self.mobile.text
    pincode = self.pincode.text
    password=self.pincode.text+self.mobile.text
    user_id = self.mobile.text+self.pincode.text
    
    # Check if any of the fields are empty
    if not first_name or not last_name or not email_id or not mobile or not pincode:
        Notification('Please fill in all fields').show()
    else:
      name = first_name + last_name
      anvil.server.call('add_user', name, email_id, mobile, pincode, user_id, password)
      Notification('Your details were submitted ' + name).show()
      landingmoduleg.email_id=email_id
      landingmoduleg.name=name
      landingmoduleg.password=password
      landingmoduleg.user_id=user_id
      open_form('landingmodule.Home')
      
      

  def loginbtt_click(self, **event_args):
   
    open_form('landingmodule.Login')

  # def homebtt(self, **event_args):
  #   open_form('landingmodule.Home_direct')

  #clear buton
  def clear_click(self, **event_args):
    self.firstname.text=None
    self.email.text=None
    self.mobile.text=None
    self.pincode.text=None
    self.lastname.text=None
    
  def home_btn(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('landingmodule.Home_direct')
    
    



    
  
  # def submitbtt_click(self, **event_args):
  #   # Get the input values
  #   first_name = self.firstname.text
  #   last_name = self.lastname.text
  #   email_id = self.email.text
  #   mobile = self.mobile.text
  #   pincode = self.pincode.text
    
  #   # Check if any of the fields are empty
  #   if not first_name or not last_name or not email_id or not mobile or not pincode:
  #       Notification('Please fill in all fields').show()
  #   else:
  #     name = first_name + last_name
  #     anvil.server.call('add_user', name, email_id, mobile, pincode)
  #     Notification('Your details were submitted ' + name).show()
  #     landingmoduleg.email_id=email_id
  #     open_form('landingmodule.Home')

  # def loginbtt_click(self, **event_args):
   
  #   open_form('landingmodule.Login')

  # def homebtt(self, **event_args):
  #   open_form('landingmodule.Home')



  
  # def submitbtt_click(self, **event_args):
  #   first_name = self.firstname.text
  #   last_name = self.lastname.text
  #   email_id = self.email.text
  #   mobile = self.mobile.text
  #   pincode = self.pincode.text

  #   # Check if any of the fields are empty
  #   if not first_name or not last_name or not email_id or not mobile or not pincode:
  #     Notification('Please fill in all fields').show()
  #   else:
  #     name = first_name + last_name
  #     if user_exists(name, email_id):
  #       Notification('User already exists in the database').show()
  #     else:
  #       anvil.server.call('add_user', name, email_id, mobile, pincode)
  #       Notification('Your details were submitted ' + name).show()
  #       open_form('Home')
  
# def user_exists(name, email_id):
#     # Check if a user with the given name and email_id already exists in the database
#     existing_user = app_tables.users.search(
#         q.and_(q.app_users.name == name, q.app_users.mail_id == email_id)
#     )
#     return len(existing_user) > 0

  # def submitbtt_click(self, **event_args):
  #   # Get the input values
  #   first_name = self.firstname.text
  #   last_name = self.lastname.text
  #   email_id = self.email.text
  #   mobile = self.mobile.text
  #   pincode = self.pincode.text
  #   password=self.pincode.text+self.mobile.text
  #   user_id = self.mobile.text+self.pincode.text
    
  #   # Check if any of the fields are empty
  #   if not first_name or not last_name or not email_id or not mobile or not pincode:
  #       Notification('Please fill in all fields').show()
  #   else:
  #     name = first_name + last_name
  #     anvil.server.call('add_user', name, email_id, mobile, pincode, user_id, password)
  #     Notification('Your details were submitted ' + name).show()
      
  #     open_form('landingmodule.Home')

  # def loginbtt_click(self, **event_args):
   
  #   open_form('landingmodule.Login')

  # def homebtt(self, **event_args):
  #   open_form('landingmodule.Home') 

  # #clear buton
  # def clear_click(self, **event_args):
  #   self.firstname.text=None
  #   self.email.text=None
  #   self.mobile.text=None
  #   self.pincode.text=None
  #   self.lastname.text=None

  def firstname_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass


  

    
    

    





