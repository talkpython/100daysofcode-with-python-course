from anvil import *
import anvil.server
import tables
from tables import app_tables
import utilities

class AllDocsForm (AllDocsFormTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.repeating_panel_docs.items = utilities.docs

  def text_box_filter_change (self, **event_args):
    self.repeating_panel_docs.items = self.filtered_docs()
    
  def doc_to_text(self, d):
    return "{} {} {}".format(d["name"], d["contents"], d["category"]["name"])
  
  def filtered_docs(self):
    txt = self.text_box_filter.text
    if not txt:
      return utilities.docs
    
    txt = txt.lower()
    
    return [
      d
      for d in utilities.docs
      if self.doc_to_text(d).lower().find(txt) >= 0
    ]

