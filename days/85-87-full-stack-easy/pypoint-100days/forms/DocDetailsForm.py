from anvil import *
import anvil.server
import tables
from tables import app_tables

class DocDetailsForm (DocDetailsFormTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    doc = self.item
    self.label_category.text = doc['category']['name']
    self.label_date.text = doc["created"].strftime("%B %d, %Y")