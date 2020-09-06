fncore
=======
A collection of functional programming for Python.

#### Quickstart
```
$ pip install fncore
$ python3

>>> from fncore import *
>>> xs = [1,2,3]
>>> reduce(fn.operator.add, xs)
6
```

## Background

`fncore` was written to make the tools necessary for functional programming in Python easier to acces. By design, these tools are scattered across other modules: the built-ins `functools`, `itertools` and `operator` and the community-managed `toolz` and `more-itertools`. `fncore` collects the code from these sources and wraps them in a single namespace for easy access.

## Use

Use of `fncore` is as simple as `pip` installing `fncore` and then importing the package. It is recommended that you `*` import `fncore`, even though this goes against Python conventions.

```
from fncore import *
```

Importing `fncore` in this way will bring some commonly used functions into your default namespace:

- [`functools.reduce`](https://docs.python.org/3/library/functools.html#functools.reduce)
- [`functools.partial`](https://docs.python.org/3/library/functools.html#functools.partial)
- [`toolz.functoolz.curry`](https://toolz.readthedocs.io/en/latest/curry.html)
- [`toolz.dicttoolz.merge`](https://toolz.readthedocs.io/en/latest/api.html#toolz.dicttoolz.merge)
- [`toolz.dicttoolz.merge_with`](https://toolz.readthedocs.io/en/latest/api.html#toolz.dicttoolz.merge_with)

And the functional-support code will be stored under the `fn` namespace.

| Location | Source |
| ------- | ---- | 
| `fn.functools` | [functools](https://docs.python.org/3/library/functools.html) |
| `fn.itertools` | [itertools](https://docs.python.org/3/library/itertools.html) |
| `fn.operator` | [operator](https://docs.python.org/3/library/operator.html) |
| `fn.toolz` | [toolz](https://toolz.readthedocs.io/en/latest/) |
| `fn.more_itertools` | [more-itertools](https://more-itertools.readthedocs.io/en/stable/index.html) |
