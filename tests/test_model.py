from unittest import TestCase

from conform.model import Model


class TestModel(TestCase):
    def test_model_instance(self):
        class TestModel(Model):
            pass

        inst = TestModel()
        self.assertTrue(isinstance(inst, Model))
