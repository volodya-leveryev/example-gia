from flask import render_template, request

from app import models


def index_page():
    query = models.db.select(models.Product).order_by(models.Product.model)
    brand = request.args.get('brand', None)
    if brand:
        query = query.filter_by(brand_id=int(brand))
    products = models.db.session.execute(query).scalars()

    query = models.db.select(models.Brand).order_by(models.Brand.name)
    brands = models.db.session.execute(query).scalars()

    return render_template('index.html', brands=brands, products=products)


def product_page(product_id):
    product = models.db.get_or_404(models.Product, product_id)
    return render_template('product.html', product=product)
