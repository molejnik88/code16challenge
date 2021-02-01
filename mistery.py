#code16challenge
import base64
import timeit


statement = (
    b'CmltcG9ydCB3ZWJicm93c2VyCgp3ZWJicm93c2VyLm9wZW4oJ2h0dHBzOi8veW91dHUuYmU'
    b'vNmlGYnVJcGU2OGsnLCBuZXc9MiwgYXV0b3JhaXNlPUZhbHNlKQo='
)

result = timeit.timeit(
    stmt=base64.b64decode(statement).decode('utf-8'),
    number=1
)
print(result)
