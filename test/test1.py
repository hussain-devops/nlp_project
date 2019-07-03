from textwrap import wrap

s='''log2(N) is about the expected number of probes in an average
successful search, and the worst case is log2(N), just one more
probe. If the list is empty, no probes at all are made. Thus binary
search is a logarithmic algorithm and executes in O(logN) time. In
most cases it is considerably faster than a linear search. It can
be implemented using iteration, or recursion. In some languages it
is more elegantly expressed recursively; however, in some C-based
languages tail recursion is not eliminated and the recursive
version requires more stack space.
'''

print wrap(s)          # prints '    hello\n      world\n    '
# print repr(dedent(s))  # prints 'hello\n  world\n'
