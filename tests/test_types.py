import six

from unittest import TestCase

from conform.types import TextType


class TestTypes(TestCase):
    def test_text_type_compile(self):
        txt = TextType(required=True)
        f = txt.compile_load()

        with self.assertRaises(Exception):
            f(None)

        self.assertEqual(f(1), 1)

        txt = TextType(required=False)
        f = txt.compile_load()

        self.assertEqual(f(None), None)

        if six.PY2:
            self.assertTrue(isinstance(f('test'), unicode))
        else:
            self.assertTrue(isinstance(f('test'), str))

        self.assertEqual(f('test'), 'test')
