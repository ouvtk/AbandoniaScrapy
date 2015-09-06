Abandonia.com scraper
===============
## Goal
Make a local copy of Abandonia.com games list to search and access easily.

## Prerequisites
 - Python 2.7 (https://www.python.org/downloads/)
 - Scrapy 1.0 (http://scrapy.org/download/)

## Usage
To download only text info and links to 'items.json' file:
	```scrapy crawl abandonia -o items.json```
	
To download title and screen-shot images:
	```scrapy crawl abandonia_images -o items.json```
	
You can even run both to do it in two steps — Scrapy will ignore to save already fetched data.
You can configure path where images will be saved at 'settings.py':
	```FILES_STORE  = 'abandonia/screens/'```
	
#### If you like what Abandonia.com do — donate at their web site.