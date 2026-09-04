"""This module is used for creating reports from scraped data."""

from fpdf import FPDF

from core.scraper import Scraper


class Reporter:
    """This is Reporter class and it will return a report of scraped data."""

    def __init__(self, scraper: Scraper):
        self.scraper = scraper

    def make_report(self) -> str:
        """This function makes report of scraped data."""
        url = self.scraper.url
        self.scraper.fetch()
        titles = self.scraper.get_titles()
        titles_num = len(titles)
        links = self.scraper.get_links()
        links_num = len(links)

        output = (
            "Scraping Report"
            "\n=================="
            f"\n\n- URL: {url}"
            f"\n- Total Titles: {titles_num}\n"
            f"- Total Links: {links_num}\n"
            "\n\nTop Titles:\n"
        )

        for title in titles:
            output += f"- {title['Text']}\n"

        output += "\n\n\nTop Links:\n"

        for link in links:
            output += f"- {link['Text']} ({link['Href']})\n"

        return output

    def export_text(self, filename: str) -> None:
        """This function writes the report in a txt file."""
        if filename.endswith(".txt"):
            filename = filename.replace(".txt", "")

        report = self.make_report()

        with open(f"{filename}.txt", "w", encoding="utf-8") as file:
            file.write(report)

    def export_pdf(self, filename: str) -> None:
        """This function writes the report in a PDF file."""
        if filename.endswith(".pdf"):
            filename = filename.replace(".pdf", "")

        report = self.make_report()

        pdf = FPDF()
        pdf.add_page()
        pdf.add_font("IranYekan", "", "./assets/fonts/IranYekan.ttf", uni=True)
        pdf.set_font("IranYekan", size=12)
        pdf.multi_cell(0, 10, report)
        pdf.output(f"{filename}.pdf")
