import pytest
from delegatable import delegatable


@delegatable
class DecoQueue:
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
    def __init__(self, name='default_queue'):
        super().__init__(name)
        self._name = name
        self.s = ','


@delegatable
class DecoQueue3:
    '''
    This class is not used in test but exists for confirming one more decorated
    class doesn't polute the first one.
    '''
    def __init__(self, name='default_queue'):
        self._name = name
        self.q = []


DecoQueue3()


def describe_MetaDelegatable():
    def describe_delegate():
        def when_delegated_function_called():
            def it_returns_value_of_the_delegated_function():
                que = DecoQueue('')
                que.delegate('append', 'pop', to='q')
                que.append(1)
                que.append(2)
                que.pop(0)
                assert que.q == [2]

            def it_doesnt_polute_undelegated_property():
                que = DecoQueue('sub_queue')
                que.delegate('append', 'pop', to='q')
                que.append(1)
                assert que.name == 'sub_queue'

        def when_undefined_function_called():
            def it_raises_error_when_undefined_attr_is_called():
                with pytest.raises(Exception) as exc_info:
                    DecoQueue('').undefined(1)
                assert "'DecoQueue' object has no attribute 'undefined'" in str(exc_info.value)

        def when_inherited():
            def it_deosnt_polute_over_instances():
                que1 = DecoQueue('')
                que2 = DecoQueue2('')
                que1.delegate('append', 'pop', to='q')
                que2.delegate('append', 'pop', to='q')
                que1.append(1)
                que2.append(2)
                assert que1.all == [1]
                assert que2.all == [2]

    def describe_delegates():
        def it_returns_delegates():
            que = DecoQueue('')
            que.delegates = {'s': 'join'}
            actual = que.delegates
            assert actual == {'s': 'join'}

        def it_returns_value_of_the_delegated_function():
            que = DecoQueue('')
            que.delegates = {'s': 'join'}
            actual = que.join('ab')
            assert actual == 'a,b'

        def it_overwirtes_existing_delegates():
            que = DecoQueue('')
            que.delegate('append', 'pop', to='q')
            que.delegates = {'s': 'join'}
            with pytest.raises(Exception) as exc_info:
                que.append(1)
            assert "'DecoQueue' object has no attribute 'append'" in str(exc_info.value)
