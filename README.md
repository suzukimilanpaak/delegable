# Delegatable


# Summary

Delegatable is a simple Python alternative to Ruby on Rails' delegate module.


# Install
```sh
pip install delegatable
```

# Getting Started

#### Basic Usage

Place @delegatable on the top of a class you want to make delegatable.

```python
from delegatable import delegatable

@delegatable
class DecoQueue:
    def __init__(self, name='default_queue'):
        self._name = name
        self.q = []
        self.delegate('append', 'pop', to='q')

    @property
    def all(self):
        return self.q


que = DecoQueue('')
que.append(1)
que.append(2)
que.pop(0)
assert que.all == [2]
```


#### Inheritance Safe

It works with classes inheriting its parent with @delegatable defined without any problem.
```
class DecoQueue2(DecoQueue):
    def __init__(self, name='default_queue'):
        super().__init__(name)

que1 = DecoQueue('')
que2 = DecoQueue2('')
que1.delegate('append', 'pop', to='q')
que2.delegate('append', 'pop', to='q')
que1.append(1)
que2.append(2)
assert que1.all == [1]
assert que2.all == [2]
```


#### delegates

The decorator offers a property, `delegates` to define delegates all at once. Note it overwrites whole delegates but doesn't merge delegates.


```
class DecoQueue:
    def __init__(self, name='default_queue'):
        self._name = name
        self.q = []
        self.delegate('append', 'pop', to='q')
        self.delegates = {'s': 'join'}

assert que.join('ab') == 'a,b'

que.append(1)
# => AttributeError("'DecoQueue' object has no attribute 'append'")
```
