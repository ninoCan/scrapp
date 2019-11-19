#Python webscraper ScrApp

## Setting the virtual environment
[**Source**](https://realpython.com/python-virtual-environments-a-primer )
This is similar to the npm init, but python has a little bit more complication.

Let's initailaize the virtual environment with:

      $ python3 -m venv env

So to create an isolated dependency for the project we need to activate it through:

   $ source env/bin/activate

This could be later deactivated simply by running `$ deactivate`.

## Installing the dependencies
[**Source**](https://realpython.com/python-web-scraping-practical-introduction )
We are going to use the `request` and `BeautifulSoup` packages which we can now install inside the venv with:

   $ pip install requests BeautifulSoup4

Following the [BeatifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#id16 ), the best way to use it is through the use of a third party parser: [lxml](https://lxml.de ). Let us install it, as well:

   $ pip install lxml


##The scraper

Touched the `scrApp.py`, most of the comment are in-file.