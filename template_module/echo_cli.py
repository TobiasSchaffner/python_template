"""A command line interface that sends all arguments to the stdout.

Copyright 2021 Tobias Schaffner

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from typing import Any, Tuple

import click


def echo(args: Any) -> Any:
    """Return all the values given as arguments.

    Args:
        args (Any): Some values.

    Returns:
        Any: The given values.
    """
    return args


@click.command()
@click.argument("args", nargs=-1)
def echo_command(args: Tuple[Any]) -> None:
    """Print all the values given as arguments.

    Args:
        args (Tuple[Any]): Some values.
    """
    click.echo(echo(args))


if __name__ == "__main__":
    echo_command()
