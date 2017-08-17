Python 3.6 introduced `random.choices` which allows weighted random choices from a list. This can be used to 
take weighted samples from a dictionary
```python
import random
d = {'a':0.5,'b':0.25,'c':0.25}
choice = random.choices(list(d.keys),list(d.values()),k=1)
```
However this requires creating a new list of the values in the dictionary. For a large dictionary this could use a lot of 
memory. This method can be recreated in pure python without needing to unpack all of the values into a new list, but its 
slower than `random.choices`.

`randomdict` is a c extension for c python (3.*) which allows weighted random samples from a dictionary without additional
memory overhead and around 3-4x faster than using `random.choices`.

```python
import randomdict
choice = randomdict.choices(d,k=1)
```
