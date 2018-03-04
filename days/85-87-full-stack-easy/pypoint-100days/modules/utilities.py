import anvil.server
import tables
from tables import app_tables

home_form = None

docs = []
categories = []

def refresh_data():
  global docs, categories
  
  raw_cats = anvil.server.call('all_categories')
  categories = [c["name"] for c in raw_cats]
  docs = anvil.server.call('all_docs')
  

def go_home():
  home_form.link_home_click()
  

def go_details(doc):
  home_form.go_details(doc)
    

def create_doc(name, category, contents):
  anvil.server.call('add_doc', name, category, contents, 0)
  refresh_data()