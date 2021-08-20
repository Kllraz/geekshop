from django.test import TestCase
from mainapp.models import Product, ProductCategory


class ProductsTestCase(TestCase):
    def setUp(self):
        self.product_category_1 = ProductCategory.objects.create(name='Кровати 1')
        self.product_category_2 = ProductCategory.objects.create(name='Кровати 2', description='топ кровать')
        self.product_category_3 = ProductCategory.objects.create(name='Кровати 3', is_delete=True)
        self.product_1 = Product.objects.create(name="кровать 1", category=self.product_category_1, price=1999.5,
                                                quantity=150)
        self.product_2 = Product.objects.create(name="кровать 2", category=self.product_category_1, price=2998.1,
                                                quantity=125,
                                                is_deleted=True)
        self.product_3 = Product.objects.create(name="кровать 3", category=self.product_category_1, price=998.1,
                                                quantity=115)

    def test_product_get(self):
        product_1 = Product.objects.get(name="кровать 1")
        product_2 = Product.objects.get(name="кровать 2")
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = Product.objects.get(name="кровать 1")
        product_2 = Product.objects.get(name="кровать 2")
        self.assertEqual(str(product_1), 'кровать 1 | Кровати 1')
        self.assertEqual(str(product_2), 'кровать 2 | Кровати 1')

    def test_product_get_items(self):
        product_1 = Product.objects.get(name="кровать 1")
        product_3 = Product.objects.get(name="кровать 3")
        products = product_1.get_items()

        self.assertEqual(list(products), [product_1, product_3])

    def test_product_category_get(self):
        product_category_1 = ProductCategory.objects.get(name="Кровати 1")
        product_category_2 = ProductCategory.objects.get(name="Кровати 2")
        self.assertEqual(product_category_1, self.product_category_1)
        self.assertEqual(product_category_2, self.product_category_2)

    def test_product_category_print(self):
        product_category_1 = ProductCategory.objects.get(name="Кровати 1")
        product_category_2 = ProductCategory.objects.get(name="Кровати 2")
        self.assertEqual(str(product_category_1), 'Кровати 1')
        self.assertEqual(str(product_category_2), 'Кровати 2')

    def test_product_category_get_items(self):
        product_category_1 = ProductCategory.objects.get(name="Кровати 1")
        product_category_2 = ProductCategory.objects.get(name="Кровати 2")
        products_categories = product_category_1.get_items()

        self.assertEqual(list(products_categories), [product_category_1, product_category_2])
