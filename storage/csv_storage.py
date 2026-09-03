"""This Module is used for storing scraped data in CSV file."""

import csv


class CSVStorage:
    """This is CsvStorage class and it will manage your data in CSV."""

    @staticmethod
    def save(data: list[dict], filename: str) -> None:
        """This function saves your data in a CSV file with your filename.
        filename should be without .csv extension."""
        if filename.endswith(".csv"):
            filename = filename.replace(".csv", "")

        with open(f"{filename}.csv", "w", newline="", encoding="utf-8") as file:
            if data[0].get("Tag") == "a":
                fieldnames = ["Tag", "Text", "Href"]
            else:
                fieldnames = ["Tag", "Text"]

            csv_writer = csv.DictWriter(file, delimiter="|", fieldnames=fieldnames)

            csv_writer.writeheader()

            csv_writer.writerows(data)

    @staticmethod
    def load(filename: str) -> list[dict]:
        """This function loads your data from CSV file that you give filename.
        filename should be without .csv extension."""
        if filename.endswith(".csv"):
            filename = filename.replace(".csv", "")

        with open(f"{filename}.csv", "r", encoding="utf-8", newline="") as file:
            csv_reader = csv.DictReader(file, delimiter="|")

        return list(csv_reader)
