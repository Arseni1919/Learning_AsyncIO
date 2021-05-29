# Learning Async IO

## About [Async IO](https://docs.python.org/3/library/asyncio.html)

Async IO is a concurrent programming design that has received dedicated support in Python,
evolving rapidly from Python 3.4 through 3.7, and probably beyond.

`asyncio` is a library to write concurrent code using the `async`/`await` syntax.

`asyncio` is used as a foundation for multiple Python asynchronous frameworks
that provide high-performance network and web-servers,
database connection libraries, distributed task queues, etc.

`asyncio` is often a perfect fit for IO-bound and high-level structured network code.

At the heart of async IO are coroutines.
A coroutine is a specialized version of a Python generator function.
Let’s start with a baseline definition and then build off of it as you progress here:
a coroutine is a function that can suspend its execution before reaching return,
and it can indirectly pass control to another coroutine for some time.

`time.sleep()` can represent any time-consuming blocking function call,
while `asyncio.sleep()` is used to stand in for a non-blocking call
(but one that also takes some time to complete).



## Credits:

- [Real Python Tutorials - Async IO](https://realpython.com/async-io-python/#odds-and-ends)
- [Real Python Tutorials - Regular Expressions: Regexes in Python](https://realpython.com/regex-python/#regexes-in-python-and-their-uses)
- [Real Python Tutorials - `try`, `except`, `else`, `finally`](https://realpython.com/python-exceptions/#cleaning-up-after-using-finally)
- [PEP - asynchronous context managers](https://www.python.org/dev/peps/pep-0492/#asynchronous-context-managers-and-async-with)


















