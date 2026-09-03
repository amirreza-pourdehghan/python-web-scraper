"""This module is used for cleaning scraped data."""


class DataCleaner:
    """This is DataCleaner class and it will clean your data."""

    @staticmethod
    def text_cleaner(text: str) -> str:
        """This function cleans a text by removing extra spaces."""
        return " ".join(text.split())

    @staticmethod
    def remove_empty(items: list) -> list:
        """This function removes empty items from the list."""

        return [item for item in items if item.strip()]
