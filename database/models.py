"""This module contains the database models."""

# pylint: disable=too-few-public-methods

from typing import Optional

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    """Base class for declarative models."""


class ScrapedData(Base):
    """Model for storing scraped data."""

    __tablename__ = "scraped_data"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tag: Mapped[str]
    text: Mapped[str]
    href: Mapped[Optional[str]] = mapped_column(nullable=True)
