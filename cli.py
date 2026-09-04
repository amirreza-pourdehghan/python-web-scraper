"""This module provides a CLI for running the web scraper."""

import sys

from core.scraper import Scraper
from report.reporter import Reporter


def main():
    """Runs the scraper CLI and generates reports."""
    url = sys.argv[1]
    scraper = Scraper(url=url)
    report = Reporter(scraper=scraper)

    output = report.make_report()
    print(output)
    report.export_pdf("output")
    report.export_text("output")


if __name__ == "__main__":
    main()
