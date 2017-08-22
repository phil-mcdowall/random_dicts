import weighteddict
import pytest

class TestClass(object):
    def test_keyerror(self):
        """raise key error if key not in dict"""
        x = weighteddict.WeightedDict()
        with pytest.raises(KeyError):
         x[1]

    def test_set(self):
        """check total of weights after addition"""
        x = weighteddict.WeightedDict()
        x[1] = "value 1",1
        x[2] = "value 2",2
        assert x._total == 3
        assert len(x._data) == len(x._weights)

    def test_set_no_weight(self):
        """raise TypeError if no weight specified"""
        x = weighteddict.WeightedDict()
        with pytest.raises(TypeError):
            x[1] = "value 1"

    def test_del(self):
        """check total of weights after deletion"""
        x = weighteddict.WeightedDict()
        x[1] = "value 1", 1
        x[2] = "value 2", 2
        del x[2]
        assert x._total == 1
        assert len(x._data) == len(x._weights)

    def test_modify(self):
        """check total after changing key/value/weight"""
        x = weighteddict.WeightedDict()
        x[1] = "value 1", 1
        x[2] = "value 2", 2
        x[2] = "value 2", 1
        assert x._total == 2
        assert len(x._data) == len(x._weights)

    def test_pop(self):
        """check total"""
        x = weighteddict.WeightedDict()
        x[1] = "value 1", 1
        x[2] = "value 2", 2
        y = x.pop(1)
        assert y == "value 1"
        assert len(x._data) == len(x._weights)
        assert 1 not in x
        assert x._total == 2

    def test_random(self):

        x = weighteddict.WeightedDict()
        x[1] = "value 1", 1
        x[2] = "value 2", 0
        y = x.random(1)
        assert y == ["value 1"]
