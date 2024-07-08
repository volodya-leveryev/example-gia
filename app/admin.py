from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import models


class ProductModelView(ModelView):
    column_list = ['brand', 'model', 'description', 'photo_small', 'photo_large']


admin = Admin()
admin.add_view(ModelView(models.Brand, models.db.session))
admin.add_view(ProductModelView(models.Product, models.db.session))
