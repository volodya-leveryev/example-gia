from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class Brand(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    products: Mapped[List['Product']] = relationship(back_populates='brand')

    def __str__(self):
        return self.name


class Product(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    brand_id: Mapped[int] = mapped_column(Integer, ForeignKey('brand.id', name='brand'))
    brand: Mapped['Brand'] = relationship(back_populates='products')
    model: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(Text)
    photo_small: Mapped[str] = mapped_column(String(255))
    photo_large: Mapped[str] = mapped_column(String(255))
