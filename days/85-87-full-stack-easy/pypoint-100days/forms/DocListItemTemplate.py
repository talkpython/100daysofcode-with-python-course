from anvil import *
import anvil.server
import tables
from tables import app_tables
import utilities

class DocListItemTemplate (DocListItemTemplateTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def form_show (self, **event_args):
    # This method is called when the column panel is shown on the screen
    self.label_created.text = self.item["created"].strftime("%B %d, %Y")

  def link_details_click (self, **event_args):
    # This method is called when the link is clicked
    utilities.go_details(self.item)


