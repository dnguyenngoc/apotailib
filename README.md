# Apotailib
This is a sample for how to create library on pypi and using it from pip install.

## Installing from PyPI
We publish apotailib as `apotailib` package in PyPI.

1. Installing with pip:

```bash
pip install 'apache-airflow==2.2.3'
```

2. Sample python code:

```python
from calculator import EasyCalculator
esc = EasyCalculator()
print(esc.add_num(1,2))
```
