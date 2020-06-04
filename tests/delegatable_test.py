import pytest
from delegatable import delegatable, delegate


@delegatable
class DecoQueue:
    delegate("append", "pop", "__repr__", to="q")

    def __init__(self, name='default_queue'):
        self._name = name
        self.q = []
        self.s = ','

    @property
    def name(self):
        return self._name

    @property
    def all(self):
        return self.q


class DecoQueue2(DecoQueue):
    delegate("join", to="s")

    def __init__(self, name='default_queue'):
        super().__init__(name)
        self._name = name
        self.s = ','

    @property
    def name(self):
        return self._name


@delegatable
class DecoQueue3:
    """
    This class is not used in test but exists for confirming one more decorated
    class doesn't polute the first one.
    """
    delegate("items", to="q")

    def __init__(self, name='default_queue'):
        self._name = name
        self.q = []


def describe_MetaDelegatable():
    def describe_delegate():
        def when_delegated_function_called():
            def it_returns_value_of_the_delegated_function():
                que = DecoQueue('')
                que.append(1)
                que.append(2)
                que.pop(0)
                assert que.q == [2]

            def it_doesnt_polute_undelegated_property():
                que = DecoQueue('sub_queue')
                que.append(1)
                assert que.name == 'sub_queue'

        def when_undefined_function_called():
            def it_raises_error_when_undefined_attr_is_called():
                with pytest.raises(Exception) as exc_info:
                    DecoQueue('').undefined(1)
                assert "'DecoQueue' object has no attribute 'undefined'" in str(exc_info.value)

        def when_inherited():
            pass

