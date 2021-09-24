from django.core.management.base import BaseCommand
import pandas as pd
from ProductsDetail.models import Product, Review


class Command(BaseCommand):

    def handle(self, *args, **options):
        comments_file = pd.read_excel('dataset.xlsx', header=1)
        # pid = comments_file.iloc[:, 0]
        # pset = pid.unique()
        # for id in pset:
        #     p = Product(product_id=str(id))
        #     p.save()
        for index, row in comments_file.iterrows():
            p, _ = Product.objects.get_or_create(product_id=row[0])
            r = Review(
                product_id=p,
                reviews=str(row[1]),
                polarity=str(row[2]),
                score=int(row[3])
            )
            r.save()
