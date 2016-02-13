import unittest
from app import blog

class mockPosts():
    def __init__(self):
        self.posts = [
            {
                'tags': ['tag1', 'tag2', 'tag3']
            },
            {
                'tags': ['tag2']
            },
            {
                'tags': ['tag1', 'tag2', 'tag4']
            }
        ]


class blogTest(unittest.TestCase):
    def get_pages_test(self):
        self.assertEqual(len(blog.get_pages([None])), 1)
        self.assertEqual(len(blog.get_pages([None] * 3)), 1)
        self.assertEqual(len(blog.get_pages([None] * 5)), 1)
        self.assertEqual(len(blog.get_pages([None] * 6)), 2)
        self.assertEqual(len(blog.get_pages([None] * 10)), 2)
        self.assertEqual(len(blog.get_pages([None] * 15)), 3)

    def gen_tags_test(self):
        mock_posts = mockPosts()
        tags = blog.gen_tags(mock_posts.posts)
        self.assertEqual(len(tags), 4)
        self.assertEqual(tags[0]['count'], 3)
        self.assertEqual(tags[1]['tag'], 'tag1')


