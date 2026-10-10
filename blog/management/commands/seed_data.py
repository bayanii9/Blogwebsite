from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from blog.models import Category, Comment, Post


class Command(BaseCommand):
    help = 'Add sample users, categories, posts, and comments.'

    def handle(self, *args, **options):
        User = get_user_model()

        usernames = [
            'johnsmith',
            'emilyjones',
            'davidwilson',
            'sarahbrown',
            'michaelscott',
            'lisajohnson',
            'alexturner',
            'jessicabaker',
            'matthewwright',
            'oliviawalker',
        ]

        users = []
        for username in usernames:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'email': f'{username}@example.com'},
            )
            if created:
                user.set_unusable_password()
                user.save(update_fields=['password'])
            users.append(user)

        category_names = [
            'Programming',
            'Productivity',
            'Travel',
            'Art',
            'Technology',
            'Health',
            'Books',
            'Design',
            'Wellness',
            'Self-Improvement',
        ]

        categories = []
        for name in category_names:
            category, _ = Category.objects.get_or_create(name=name)
            categories.append(category)

        titles = [
            'Introduction to Django',
            'Tips for Effective Time Management',
            'Exploring the Wonders of Nature',
            'The Art of Photography',
            'Understanding Machine Learning',
            'Healthy Eating Habits',
            'Exploring the World of Literature',
            'Basics of Graphic Design',
            'Benefits of Yoga and Meditation',
            'The Power of Positive Thinking',
        ]

        contents = [
            'Django is a Python framework for building websites. This post introduces projects, apps, models, and views.',
            'Set priorities, divide large tasks into smaller steps, and make time for focused work.',
            'Nature offers beautiful landscapes, fascinating wildlife, and new places to explore.',
            'Photography uses light, composition, and timing to capture memorable moments.',
            'Machine learning helps computers find patterns in data and make useful predictions.',
            'Balanced meals and healthy routines can support energy and overall wellbeing.',
            'Reading different genres introduces us to new ideas, places, and points of view.',
            'Graphic design combines typography, color, and layout to communicate clearly.',
            'Yoga and meditation can help build flexibility, focus, and calm.',
            'Positive thinking can help us approach everyday challenges with patience and confidence.',
        ]

        posts = []
        for index, title in enumerate(titles):
            post, _ = Post.objects.get_or_create(
                slug=slugify(title),
                defaults={
                    'title': title,
                    'content': contents[index],
                    'author': users[index],
                    'category': categories[index],
                },
            )
            posts.append(post)

        sample_comments = [
            (0, 1, 'Great introduction to Django!'),
            (0, 4, 'This article was very informative.'),
            (1, 2, 'These time management tips are helpful.'),
            (2, 6, 'I love exploring nature.'),
            (3, 3, 'A lovely article about photography.'),
            (5, 7, 'Healthy eating is important.'),
            (6, 8, 'I enjoy reading different genres.'),
            (7, 9, 'Graphic design is a creative field.'),
            (8, 5, 'Yoga and meditation are helpful habits.'),
            (9, 0, 'Positive thinking makes a difference.'),
        ]

        for post_index, user_index, text in sample_comments:
            Comment.objects.get_or_create(
                post=posts[post_index],
                user=users[user_index],
                content=text,
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Sample data added: 10 users, 10 categories, 10 posts, and 10 comments.'
            )
        )