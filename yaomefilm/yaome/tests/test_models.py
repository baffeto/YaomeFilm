from unittest import TestCase
from yaome.models import *


class ModelsTestCase(TestCase):
    def test_category(self):
        category = Category.objects.create(name='Мистика')
        category.save()

        saved_categories = Category.objects.all()
        self.assertEqual(saved_categories.count(), 3)

        category_check = saved_categories[0]
        self.assertEqual(category_check.name, 'Триллеры')
        
    def test_actor(self):
        actor = Actor.objects.create(name='Игорь', surname='Сазонов')
        actor.save()

        count_actors = Actor.objects.all().count()

        saved_actors = Actor.objects.all()
        self.assertEqual(saved_actors.count(), count_actors)

        actors_check = saved_actors[0]
        self.assertEqual(actors_check.name, 'Иван')
    
    def test_director(self):
        director = Director.objects.create(name='Игорь', surname='Наставник')
        director.save()

        count_director = Director.objects.all().count()

        saved_director = Director.objects.all()
        self.assertEqual(saved_director.count(), count_director)

        director_check = saved_director[0]
        self.assertEqual(director_check.name, 'Kevin')

