import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def add_user(name, mobile, mail, pincode, userid, passcode):
  app_tables.users.add_row(name=name,Date_of_signup=datetime.now(),mobile_no=mobile,mail_id=mail,pincode=pincode, user_id=userid, passward=passcode)



#ProductId,ProductName,MemebershipType,ProcessingFee,ExtensionFee,DefaulterFee,InterestType,MaxAmount,MinAmount,Tenure,ExtensionsAllowed,PartPayments,ForeClosure
@anvil.server.callable
def add_products(productid, productname, membership, process, extension, defaulter, interest, max, min, tenure, extensionsallowed, part, foreclosure):
   app_tables.products.add_row(product_id=productid, product_name=productname, membership=membership, process=process, extension=extension, defaulter=defaulter, interest=interest, max=max, min=min, tenure=tenure, ext_allowed=extensionsallowed, part=part, foreclosure=foreclosure)
@anvil.server.callable
def add_membership(membershiptype,tenure):
  app_tables.membership.add_row(membershiptype=membershiptype,tenure=tenure)

@anvil.server.callable
def add_loan(loan_extension,loan_id,loan_amount,loan_availed_date,tenure,intrest,processing_fee,loan_repayment_amount,loan_due_amount,select):
  app_tables.loan.add_row(loan_extension=loan_extension,loan_id=loan_id,loan_amount=loan_amount,loan_availed_date=loan_availed_date,tenure=tenure,intrest=intrest,processing_fee=processing_fee,loan_repayment_amount=loan_repayment_amount,loan_due_amount=loan_due_amount,select=select)

@anvil.server.callable
def get_products():
  return app_tables.products.search()

@anvil.server.callable
def search_products(query):
  result = app_tables.products.search()
  if query:
    result = [
      x for x in result
      if query in x['product_id']
      or query in x['product_name']
      or query in x['membership']
      or query in x['process']
      
    ]
  return result

@anvil.server.callable
def add_return_on_investment(initial_investment,tenure,membership_type,interest_rate):
  app_tables.return_on_investment.add_row(initial_investment=initial_investment,membership_type=membership_type,tenure=tenure,interest_rate=interest_rate)
  


  