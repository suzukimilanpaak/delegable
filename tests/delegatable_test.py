import pytest
from delegatable import Delegatable, MetaDelegatable


# @delegatable
# class DecoQueue:
    # def __init__(self, name='default_queue'):
        # self._name = name
        # self.q = []
        # self.s = ','

    # @property
    # def name(self):
        # return self._name


class MetaQueue(metaclass=MetaDelegatable):
    delegate("append", "pop", "copy", to="q")

    def __init__(self, name='default_queue'):
        self._name = name
        self.q = []
        self.s = ','

    @property
    def name(self):
        return self._name

class MetaQueue2(metaclass=MetaDelegatable):
    delegate("items", to="q")

    def __init__(self, name='default_queue'):
        self._name = name
        self.q = []


class Parent:
    pass


class Queue(Parent, Delegatable):
    def __init__(self, name='default_queue'):
        self._name = name
        self.q = []

    @property
    def name(self):
        return self._name


def describe_MetaDelegatable():
    def describe_delegate():
        def when_delegated_function_called():
            def it_returns_value_of_the_delegated_function():
                que = MetaQueue('')
                que.append(1)
                que.append(2)
                que.pop(0)
                assert que.q == [2]

            def it_doesnt_polute_undelegated_property():
                que = MetaQueue('sub_queue')
                que.append(1)
                assert que.name == 'sub_queue'

        def when_undefined_function_called():
            def it_raises_error_when_undefined_attr_is_called():
                with pytest.raises(Exception):
                    MetaQueue('').undefined(1)

    def describe_delegates():
        def when_delegated_function_called():
            def it_sets_delegates():
                MetaQueue.delegates = {"s": "join"}
                assert MetaQueue.delegates == {"s": "join"}

            def it_returns_value_of_the_delegated_function():
                MetaQueue.delegates = {"s": "join"}
                que = MetaQueue('')
                actual = que.join(['a', 'b'])
                assert actual == 'a,b'

            def it_overwrites_all_delegates():
                MetaQueue.delegates = {"s": ("join")}
                que = MetaQueue('sub_queue')
                with pytest.raises(AttributeError) as exc_info:
                    que.append('a')
                assert "'MetaQueue' object has no attribute 'append'" == str(exc_info.value)



def describe_Delegatable():
    def describe_delegate():
        def when_delegated_function_called():
            def it_returns_value_of_the_delegated_function():
                que = Queue('')
                que.delegate("append", "pop", to="q")
                que.append(1)
                que.append(2)
                que.pop(0)
                assert que.q == [2]

        def when_undelegated_function_called():
            def it_deosnt_polute_another_property():
                que = Queue('sub_queue')
                que.delegate("append", "pop", to="q")
                que.append(1)
                assert que.name == 'sub_queue'

        def when_undefined_function_called():
            def it_raises_error_when_undefined_attr_is_called():
                with pytest.raises(Exception):
                    Queue('').undefined(1)

    def describe_delegates():
        def when_delegated_function_called():
            def it_sets_delegates():
                que = MetaQueue('')
                que.delegates = {"s": "join"}
                assert que.delegates == {"s": "join"}

            def it_returns_value_of_the_delegated_function():
                que = MetaQueue('')
                que.delegates = {"s": "join"}
                actual = que.join(['a', 'b'])
                assert actual == 'a,b'
