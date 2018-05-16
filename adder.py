#!/usr/bin/env python
import click

def add(a, b):
    return a + b

@click.command()
@click.option('--lhs', type=int, required=True)
@click.option('--rhs', type=int, required=True)
def main(lhs, rhs):                     
    result = add(lhs, rhs)
    print(result)

if __name__ == '__main__':
    main(auto_envvar_prefix='ADDER')

