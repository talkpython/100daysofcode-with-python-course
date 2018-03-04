from anvil import *
import anvil.server
import tables
from tables import app_tables
import utilities

class AddDocForm (AddDocFormTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.drop_down_categories.items = [('select a category', None)] +  [(c, c) for c in utilities.categories]
    self.label_errors.text = ""

  def button_save_click (self, **event_args):
    errors = self.validate()
    if errors:
      self.label_errors.text = "\n".join(errors)
      return
    
    name = self.text_box_doc_name.text.strip()
    category = self.drop_down_categories.selected_value
    contents = self.text_area_contents.text.strip()
    
    utilities.create_doc(name, category, contents)
    utilities.go_home()
    
  
  def validate(self):
    self.label_errors.text = ""
    errors = []
    if not self.text_box_doc_name.text or not self.text_box_doc_name.text.strip():
      errors.append('Document name is required')
    
    if not self.drop_down_categories.selected_value:
      errors.append('Document category is required')
    
    if not self.text_area_contents.text or not self.text_area_contents.text.strip():
      errors.append('Cannot create empty documents')
      
    return errors


