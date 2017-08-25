import randomdict

class WeightedDict:
    def __init__(self, **kwargs):
        self._data = dict()
        self._weights = dict()
        self._total = 0
        if all(k in kwargs for k in ['weights','data']):
            self._data = kwargs['data']
            self._weights = kwargs['weights']
            self._total = self._calculate_total()

    def _calculate_total(self):
        return sum(self._weights.values())

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, value):
        if len(value) != 2:
            raise TypeError("Expected (value, weight) tuple")
        if value[1] < 0:
            raise ValueError("Weights must be positive")
        if key in self._data:
            self._total -= self._weights[key]
            self._total += value[1]
            self._weights[key] = value[1]
        else:
            self._total += value[1]
        return self._data.__setitem__(key, value[0]), self._weights.__setitem__(key, value[1])

    def __delitem__(self, key):
        self._data.__delitem__(key)
        self._total -= self._weights.pop(key)

    def get(self, key, default=None):
        return self._data.get(key, default)

    def pop(self, key):
        self._total -= self._weights.pop(key)
        return self._data.pop(key)

    def __contains__(self, key):
        return self._data.__contains__(key)

    def copy(self):
        return type(self)(**{'data':self._data,'weights':self._weights})

    def __repr__(self):
        return '{0}({{data:{1},weights:{2}}})'.format(type(self).__name__,self._data.__repr__(), self._weights.__repr__())

    def random(self, k):
        return [self._data[i] for i in randomdict.random(k, self._weights, self._total)]
