# This is a sample Python script.

import asyncio
import time
from termcolor import colored


my_dict = {
    'counter': 0,
    'info': 'logs: '
}

colors = ['red', 'green', 'blue']


async def agent(n):
    print(colored(f'start of agent {n}', colors[n]))
    print(colored(f'inside update_counter {n}', color=None, on_color='on_white', attrs=['bold']))
    await asyncio.sleep(1)
    # time.sleep(1)
    my_dict['counter'] += 1
    my_dict['info'] += f'- agent {n} -'
    print(colored(my_dict, colors[n]))
    print(colored(f'finish of agent {n}', colors[n]))


async def main():
    await asyncio.gather(agent(0), agent(1), agent(2))


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    f = time.perf_counter() - s
    print(f'{__file__} executed in {f:0.2f} seconds.')

