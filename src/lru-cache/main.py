import cProfile
from ..common.utils import log, check

from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.key_stack = deque()
        # self.key_stack = []

    def __do_stack(self, key: int) -> None:
        stack_len = len(self.key_stack)
        key_idx = -1
        if key in self.cache:
            key_idx = self.key_stack.index(key)

        if key_idx != -1:
            del self.key_stack[key_idx]

        self.key_stack.insert(0, key)
        # log(f'1 key_stack:{self.key_stack}')
        if key_idx == -1 and stack_len == self.cap:
            del self.cache[self.key_stack.pop()]
        # log(f'2 key_stack:{self.key_stack}')

    def get(self, key: int) -> int:
        # log(f'getting key:{key} from self.cache:{self.cache}')
        if key in self.cache:
            self.__do_stack(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # log(f'adding key:{key} value:{value}')
        self.__do_stack(key)
        self.cache[key] = value


###################################


def do_all_tests():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    assert (lRUCache.get(1) == 1)  # return 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert (lRUCache.get(2) == -1)  # returns -1 (not found)
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    assert (lRUCache.get(1) == -1)  # return -1 (not found)
    assert (lRUCache.get(3) == 3)  # return 3
    assert (lRUCache.get(4) == 4)  # return 4

    LEN = 1024 * 32
    HALF = int(LEN / 2)

    lRUCache = LRUCache(HALF)
    for i in range(LEN):
        lRUCache.put(i, i)

    for i in range(LEN):
        ret = lRUCache.get(i)
        if i < HALF:
            assert (lRUCache.get(i) == -1), f'{ret} != {i}'
            continue
        assert (lRUCache.get(i) == i), f'{ret} != {i}'


if __name__ == '__main__':
    # cProfile.run('do_all_tests()')
    do_all_tests()
