"""This module is used for storing scraped data in JSON files."""

import json


class JSONStorage:
    """This is JSONStorage class and it will manage your data in JSON."""

    @staticmethod
    def save(data: list[dict], filename: str) -> None:
        """This function saves your data in a JSON file with your filename.
        filename should be without .json extension."""
        if filename.endswith(".json"):
            filename = filename.replace(".json", "")

        with open(f"{filename}.json", "w", encoding="utf-8") as file:
            json.dump(data, file)

    @staticmethod
    def load(filename: str) -> list[dict] | dict:
        """This function loads your data from JSON file that you give filename.
        filename should be without .json extension."""
        if filename.endswith(".json"):
            filename = filename.replace(".json", "")

        with open(f"{filename}.json", "r", encoding="utf-8") as file:
            return json.load(file)
