from anvil import *
import anvil.server
import tables
from tables import app_tables
import utilities

class HomeDetailsForm (HomeDetailsFormTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.repeating_panel_1.items = utilities.docs[:3]