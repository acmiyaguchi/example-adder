# example-adder

A click-based application running on top of pipenv and docker.


## Usage
Pipenv must be installed as a prerequisite.

```bash
$ pip install pipenv
```

### Adder

```bash
$ pipenv run python adder.py --lhs 1 --rhs 2

# equivalently
$ ADDER_LHS=1 ADDER_RHS=2 pipenv run python adder.py
```

### Docker
```bash

$ docker build -t adder:latest .

$ docker run -it adder:latest \
    pipenv run ./adder --lhs -1 --rhs 3

$ docker run \
    -e ADDER_LHS=-1 \
    -e ADDER_RHS=3 \
    -it adder:latest
```

### Tests
```bash
$ pipenv sync --dev
$ pipenv run python -m pytest
```

