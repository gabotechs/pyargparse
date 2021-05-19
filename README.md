# PyArgParse
<p align="center">
    <img src="https://github.com/GabrielMusat/pyargparser/actions/workflows/test.yml/badge.svg">
</p>
Parse arguments by just defining a typed class for your Python programs in a flexible and typed way from commandline arguments,
environment variables, and/or yml config files.

## Install
```shell
pip install pyargparse
```
## Usage

Define a class that inherits from PyArgs class
```python
from typing import Optional
from pyargparse import PyArgs

class Args(PyArgs):
    mandatory_string: str
    optional_integer: Optional[int]
    default_float: float = 0.5

args = Args()
print(args)
```
launch the script with your configuration
```shell
python3 script.py --mandatory-string=foo --optional-integer=1
```
or
```shell
MANDATORY_STRING=foo DEFAULT_FLOAT=1.0 python3 script.py
```
or
```shell
echo "
mandatory_string: foo
optional_integer: 2
default_float: 1.0
" > config.yml
python3 script.py
```

The priority is: CLI > ENV > YML

If you don't want to have all that possibilities for parsing arguments, there are more parsing classes 
available:

```python
from pyargparse import PyArgs, CliArgs, CliEnvArgs, CliYmlArgs, EnvArgs, EnvYmlArgs, YmlArgs

CliArgs  # only parse from command line
CliEnvArgs  # parse from command line and from environment variables
CliYmlArgs  # parse from command line and a yml config file
EnvArgs  # parse only from environment variables
EnvYmlArgs  # parse from environment variables and a yml config file
YmlArgs  # parse only from yml config file
PyArgs  # parse from everything!
```
