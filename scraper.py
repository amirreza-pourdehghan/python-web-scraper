"""This Module is used for scraping and fetching web page HTML."""

import requests
from bs4 import BeautifulSoup


class Scraper:
    """This is Scraper class and it will Scrape your URL."""

    def __init__(self, url: str):
        self.url = url
        self.soup = None

    def fetch(self) -> "Scraper":
        """This function Fetches the url HTML and parses with BeautifulSoup."""
        response = requests.get(self.url, timeout=10)
        response_txt = response.text

        self.soup = BeautifulSoup(response_txt, "html.parser")

        return self

    def get_titles(self) -> list:
        """This function gets titles of the url HTML and returns a list of titles."""
        if self.soup is None:
            raise ValueError("Please call fetch function first")

        titles_list = []

        titles = self.soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

        for title in titles:
            titles_list.append(
                {
                    "Tag": title.name,
                    "Text": title.text.strip(),
                }
            )

        return titles_list

    def get_links(self) -> list:
        """This function gets links of the url HTML
        and return a list included of dictionaries with text_key and href_key."""
        if self.soup is None:
            raise ValueError("Please call fetch function first")

        links_list = []

        links = self.soup.find_all("a")

        for link in links:
            links_list.append(
                {"Tag": "a", "Text": link.text.strip(), "Href": link.get("href")}
            )

        return links_list

    def get_elements(self, element_tag: str) -> list:
        """This function gets element tag and finds it in page HTML and return list of them."""
        if self.soup is None:
            raise ValueError("Please call fetch function first")

        element_tag_list = []

        elements = self.soup.find_all(element_tag)

        for element in elements:
            element_tag_list.append({"Tag": element_tag, "Text": element.text.strip()})

        return element_tag_list
