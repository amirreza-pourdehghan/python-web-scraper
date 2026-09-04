"""This module provides a DatabaseManager for handling scraped data."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from database.models import Base, ScrapedData


class DatabaseManager:
    """This DatabaseManager class manages the database for scraped data."""

    def __init__(self):
        self.engine = create_engine("sqlite:///scraper.db")
        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)

    def save(self, data: list[dict]) -> None:
        """Saves a list of scraped data dictionaries to the database."""
        for data_dict in data:
            scrapeddata = ScrapedData(
                tag=data_dict["Tag"],
                text=data_dict["Text"],
                href=data_dict.get("Href"),
            )
            self.session.add(scrapeddata)
            self.session.commit()

    def load_all(self) -> list[dict]:
        """Loads all scraped data records from the database."""
        items = self.session.query(ScrapedData).all()
        return [
            {"tag": item.tag, "text": item.text, "href": item.href} for item in items
        ]
