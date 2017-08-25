[![Build Status](https://travis-ci.org/phil-mcdowall/weighted_dicts.svg?branch=master)](https://travis-ci.org/phil-mcdowall/weighted_dicts)

Weighted dictionaries for python 3.6. In development. 0.01dev

Installation:
```bash
apt-get install python3.6-dev
git clone https://github.com/phil-mcdowall/random_dicts.git
python3 setup.py build_ext
```
Usage: 
```python
from weighted_dict import WeightedDict
# initialise weighted dictionary
w_d = WeightedDict()
# Set key/value pairs, where value is a tuple (data,weight)
w_d['key 1'] = 'value 1', 1
w_d['key_2'] = 'value 2', 2
# Weighted random choice (size 1) from dictionary
w_d.random(k=1)
```

