# Delegatable


# Summary

Delegable is a simple Python alternative to Ruby on Rails' delegate module, which makes delegation easy. It enables any class to delegate its functions to an instance of another one. Here's an example:

```python
@delegable
class Que:
    def __init__(self):
        self.q = []
        self.delegate('append', 'pop', to='q')

que = Que()
que.append(1)
que.pop()
# => 1
```


### Features:

- Inheritance Safe
- No dependent libraries
- Available for py35, py36, py37, py38


# Install
```sh
pip install delegable
```

# Getting Started

#### Basic Usage

Place @delegable.delegator on the top of a class in which you want to enable delegation.

```python
import delegable

@delegable.delegator
class Que:
    def __init__(self, name='default_queue'):
        self._name = name
        self.q = []
        self.delegate('append', 'pop', to='q')

    @property
    def all(self):
        return self.q


que = Que('')
que.append(1)
que.append(2)
que.pop(0)
assert que.all == [2]
```


#### Inheritance Safe

It works well with classes inheriting its parent which uses `@delegable.delegtor` without any problem.

```python
class Que2(Que):
    def __init__(self, name='default_queue'):
        super().__init__(name)

que1 = Que('')
que2 = Que2('')
que1.delegate('append', 'pop', to='q')
que2.delegate('append', 'pop', to='q')
que1.append(1)
que2.append(2)
assert que1.all == [1]
assert que2.all == [2]
```


#### delegates

The decorator offers a property, `delegates` to define delegates all at once. Note it overwrites whole delegates but doesn't merge delegates.

```python
@delegable.delegator
class Que:
    def __init__(self, name='default_queue'):
        self._name = name
        self.q = []
        self.delegate('append', 'pop', to='q')
        self.delegates = {'s': 'join'}

assert que.join('ab') == 'a,b'

que.append(1)
# => AttributeError("'Que' object has no attribute 'append'")
```


# How to Test

This project uses [tox](https://tox.readthedocs.io/) to test it against different versions of Python, with underlying pyenv.


### Set up

You have to have pyenv installed to run tox in this project.


### Test

To test with all versions:
```sh
tox
```

To test with a certain version:
```sh
tox -e py37
```

or

```sh
pyenv shell 3.7.7
pytest
```
