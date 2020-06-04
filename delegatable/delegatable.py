# -*- coding: utf-8 -*-
'''
Convenient classes to enable delegate
..codeauthor Tatsuya Suzuki <tatsuya.suzuki@nftlearning.com>
'''
import inspect
import copy
import logging as log
from typing import Sequence, Any, Dict, Tuple


_delegates = {'object': {}}


def delegatable(cls):
    def __getattr__(self, name) -> Any:
        """
        Look for delegated funcion

        If any found, raises AttributeError
        """
        callers = [cls.__name__ for cls in (self.__class__,) + self.__class__.__bases__]
        for caller in callers:
            log.debug(f'delegates={_delegates[caller]}')
            for to, funcs in _delegates[caller].items():
                funcs = (funcs,) if type(funcs) is str else funcs
                for func in funcs:
                    # Check if func is in any of the delegates
                    if name == func and hasattr(getattr(self, to), func):
                        # Delegate the call
                        return getattr(getattr(self, to), func)
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")  # noqa: E501

    def _new(func):
        def _wrap(cls, *args, **kwargs):
            instance = func(cls)
            return instance
        return _wrap

    cls.__new__ = _new(cls.__new__)
    cls.__getattr__ = __getattr__
    return cls


def delegate(*funcs, to: str) -> Sequence:
    frame = inspect.currentframe().f_back
    caller = inspect.getargvalues(frame).locals['__qualname__']
    print(inspect.getargvalues(inspect.currentframe()).locals)
    raise Exception('')
    if not _delegates.get(caller):
        _delegates[caller] = {}

    _delegates[caller].update({to: funcs})
    return _delegates[caller]
