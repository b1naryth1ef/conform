import six


class ModelMeta(type):
    def __new__(mcs, name, parent, dct):
        return super(ModelMeta, mcs).__new__(mcs, name, parent, dct)


class Model(six.with_metaclass(ModelMeta)):
    pass


"""
class TestModel(Model):
    a = TextField()
    b = IntegerField()
    c = FloatField()


TestModel.load_into(TestModel(), {'a': 'test', 'b': 1, 'c': 3.3})
"""
