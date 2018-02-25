#!python3
#pull_xml.py uses the requests module to pull down the feed xml file for use in the xml parser script.
#This will result in just one call/request to the Steam webserver hosting this XML file.

import requests

URL = "http://store.steampowered.com/feeds/newreleases.xml"

if __name__ == "__main__":
	r = requests.get(URL)
	with open('newreleases.xml', 'wb') as f:
		f.write(r.content)
