# This is a sample Python script.

import asyncio
import time


async def count(w):
    print('one')
    await asyncio.sleep(w)
    print('two')


async def main():
    await asyncio.gather(count(1), count(2), count(3))


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    f = time.perf_counter() - s
    print(f'{__file__} executed in {f:0.2f} seconds.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
