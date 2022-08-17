# GG-CLI

A prototype cli for every day things. GG because GG is easy to type.

## Structure

We have the concept of options (aka global options), commands (aka root level commands), positional arguments, and optional arguments.

 `ggcli [options] <command> <subcommand> [arguments]`

- with commands as the primary handler and positional arguments
  - `ggcli [options] <command> [command's positional arguments] [command's optional arguments]`
- with subcommands as handlers we cannot have positional arguments without confusing the two.
  - `ggcli [options] <command> [command's optional arguments] <subcommand> [subcommand's positional arguments] [subcommand's optional arguments]`
  - *Note* if subcommands and command positional arguments are defined we will ignore command positional arguments in favor for subcommands.

## Options

Example Option

```python
def debug_callback(args):
    print("debug is {args.debug}")

Option(name="debug", short_name="d", nargs=0, func=debug_callback)
```

## Commands, Subcommands, and Arguments

Commands can have root level handlers or subcommand handlers or both, but if both are used, then root level handlers cannot have positional arguments. For example:

- `hello world` - root level handler with positional argument.
- `hello brenden` - subcommand handler and no arguments.

We would not know if `world` should be interpreted as a positional argument of the root command `hello` or if we should call the handler of the subcommand `brenden`. We might be able to define some heuristic/decision tree logic, but it is not very intuitive. In the case above we would complain to the console, and ignore positional arguments in the presence of subcommands.

Example Commands

Using command level handler

``` python

def hello_main(args): # handler function when running the `ggcli hello` command
    prefix = args.prefix+'.' if args.prefix is not None else ''
    print(f"hello {prefix}{args.firstname} {args.lastname}")

command = Command(
    name="hello",
    index=hello_main, # handler
    arguments=[
        Argument( # a generic argument set as an optional argument, not a positional argument
            name="prefix",
            type=str,
            positional=False,
            default="Mr",
            help="Optional arg"
        ),
        PositionalArgument( # Argument subclass that marks an argument as a positional argument. If no default and not provided it will provide an error message showing that it is required.
            name="firstname",
            type=str,
            default="Brenden",
            help="Positional arg"
        ),
        OptionalArgument( # Argument subclass that marks an argument as a optional argument, if no default and not provided by user it will be None.
            name="lastname",
            type=str,
            help="Optional arg"
        )
    ],
    subcommands=[
    ],
    help="This is the good old 'hello' function"
)
```

- usage: `ggcli [-h] hello [-prefix PREFIX] [firstname] [lastname]`
- `lastname` will be `None` if not provided
- `firstname` will be defaulted to `Brenden` if not provided. If `firstname` did not have a default it would error out if not provided.
- This is setup as a root level handler with positional arguments and no subcommands it will call the `hello_main` handler.

or using subcommands handlers

``` python

command = Command(
    name="foo",
    short_name="f",
    subcommands=[
        Subcommand(
            name="bar",
            short_name="b",
            func=foobar_main,
            help="This is the good old 'foo bar' function"
        )
    ],
    help="This is the good old 'foo' function"
)

```

- usage: `ggcli [-h] foo {bar,b}`

## Future Features

### Plugins

*A naive plugin solution was removed in past commit in order to focus on the core mechanics, but plugins is still a desired feature.*
