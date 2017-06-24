from unittest import TestCase

from conform.types import TextType


class TestTypes(TestCase):
    def test_text_type_compile(self):
        txt = TextType(required=True)
        f = txt.compile_load()

        with self.assertRaises(Exception):
            f(None)

        f(1)
