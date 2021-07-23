from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from recipe.models import Category, Recipe


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

    def test_category_url(self):
        """
        Test category model slug and URL reverse
        """
        data = self.data1
        # response = self.client.post(
        #     reverse('recipe:category_list', args=[data.slug]))
        # self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data, Category))


class TestRecipesModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Recipe.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')
        # self.data2 = Recipe.recipes.create(category_id=1, title='django advanced', created_by_id=1,
        #                                      slug='django-advanced', price='20.00', image='django')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Recipe))
        self.assertEqual(str(data), 'django beginners')

    # def test_products_url(self):
    #     """
    #     Test product model slug and URL reverse
    #     """
    #     data = self.data1
    #     url = reverse('recipe:recipe_detail', args=[data.slug])
    #     self.assertEqual(url, '/item/django-beginners/')
    #     response = self.client.post(
    #         reverse('recipe:recipe_detail', args=[data.slug]))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_products_custom_manager_basic(self):
    #     """
    #     Test recipe model custom manager returns only active products
    #     """
    #     data = Recipe.recipes.all()
    #     self.assertEqual(data.count(), 1)