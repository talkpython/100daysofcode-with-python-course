from anvil import *
import anvil.server
import tables
from tables import app_tables
from AddDocForm import AddDocForm
from DocDetailsForm import DocDetailsForm
from AllDocsForm import AllDocsForm
from HomeDetailsForm import HomeDetailsForm
import utilities

class HomeForm (HomeFormTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    utilities.refresh_data()
    self.link_home_click()
    utilities.home_form = self
    

  def link_home_click (self, **event_args):
    self.label_title.text = "PyPoint: Home"
    self.content_panel.clear()
    self.content_panel.add_component(HomeDetailsForm())

  def link_all_docs_click (self, **event_args):
    self.label_title.text = "PyPoint: All Documents"
    self.content_panel.clear()
    self.content_panel.add_component(AllDocsForm())

  def link_add_doc_click (self, **event_args):
    self.label_title.text = "PyPoint: Add a document"
    self.content_panel.clear()
    self.content_panel.add_component(AddDocForm())

  def go_details(self, doc):
    self.label_title.text = "PyPoint: Details"
    self.content_panel.clear()
    self.content_panel.add_component(DocDetailsForm(item=doc))


