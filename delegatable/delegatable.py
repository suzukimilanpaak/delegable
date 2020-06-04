# -*- coding: utf-8 -*-
'''
Convenient classes to enable delegate
..codeauthor Tatsuya Suzuki <tatsuya.suzuki@nftlearning.com>
'''
import copy
import logging as log
from typing import Sequence, Any, Dict, Tuple

# def delegatable(cls):
    # def __new__(cls, *args, **kwargs):
        # instance = super().__new__(cls)
        # instance.delegates = {}
        # return instance

    # @property
    # def delegates(self) -> Dict[str, Tuple[str]]:
        # return self._delegates

    # @delegates.setter
    # def delegates(self, delegates: Dict[str, Tuple[str]]) -> Dict[str, Tuple[str]]:
        # self._delegates = delegates
        # return self.delegates

    # def delegate(self, *funcs, to: str) -> Sequence:
        # self.delegates.update({to: funcs})
        # return self.delegates

    # def __getattr__(self, name) -> Any:
        # log.debug(f'delegates={self._delegates}')
        # for to, funcs in self._delegates.items():
            # funcs = (funcs,) if type(funcs) is str else funcs
            # for func in funcs:
                # # Check if func is in any of the delegates
                # if name == func and hasattr(getattr(self, to), func):
                    # # Delegate the call
                    # return getattr(getattr(self, to), func)
        # raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")  # noqa: E501

class MetaDelegatable(type):
    _delegates = {}

    def _get_delegates(cls) -> Dict[str, Tuple[str]]:
        return cls._delegates

    def _set_delegates(cls, delegates: Dict[str, Tuple[str]]) -> Dict[str, Tuple[str]]:
        cls._delegates = delegates
        return cls._delegates

    def delegate(*funcs: Sequence[str], to: str) -> Dict[str, Tuple[str]]:
        __class__._delegates.update({to: funcs})
        return __class__._delegates

    def __getattr__(self, name) -> Any:
        log.debug(f'delegates={self.__class__._delegates}')
        for to, funcs in self.__class__._delegates.items():
            funcs = (funcs,) if type(funcs) is str else funcs
            for func in funcs:
                # Check if func is in any of the delegates
                if name == func and hasattr(getattr(self, to), func):
                    # Delegate the call
                    return getattr(getattr(self, to), func)
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")  # noqa: E501


    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        _dict_ = {}
        _dict_['delegate'] = metacls.delegate
        metacls.delegates = property(MetaDelegatable._get_delegates, MetaDelegatable._set_delegates)
        return _dict_


    def __new__(cls, name, bases, attrs):
        attrs['__getattr__'] = cls.__getattr__
        instance = super().__new__(cls, name, bases, attrs)
        return instance


class Delegatable:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.delegates = {}
        return instance

    @property
    def delegates(self) -> Dict[str, Tuple[str]]:
        return self._delegates

    @delegates.setter
    def delegates(self, delegates: Dict[str, Tuple[str]]) -> Dict[str, Tuple[str]]:
        self._delegates = delegates
        return self.delegates

    def delegate(self, *funcs, to: str) -> Sequence:
        self.delegates.update({to: funcs})
        return self.delegates

    def __getattr__(self, name) -> Any:
        log.debug(f'delegates={self._delegates}')
        for to, funcs in self._delegates.items():
            funcs = (funcs,) if type(funcs) is str else funcs
            for func in funcs:
                # Check if func is in any of the delegates
                if name == func and hasattr(getattr(self, to), func):
                    # Delegate the call
                    return getattr(getattr(self, to), func)
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")  # noqa: E501
