#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
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

