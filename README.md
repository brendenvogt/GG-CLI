# GG-CLI

A prototype cli for every day things. GG because GG is easy to type.

# Description

# Synopsis

`ggcli [options] <command> <subcommand> [parameters]`

## Environment Variables

## Options

-   `--debug`
-   `--version`

## Commands

## Plugins

GG CLI aims to support plugins. Where users can write their own plugins and install them as needed.

# Development

-   clone repo
-   run command:
    -   change directory `cd ./GG-CLI/ggcli`
    -   run `python3 . [options] <command> <subcommand> [parameters]`
-   run tests:
    -   change directory `./GG-CLI`,
    -   run `pytest`

## Philosophy

-   command structure: `ggcli [options] <command> <subcommand> [parameters]`
-   for options and the main parsing we have `MainArgParser`
-   for the commands we have a `CommandArgParser`
-   for the subcommands we have a `SubcommandArgParser`

# Components

## CLIOption

-   `--debug`
-   `--version`
-   `--help`
-   `--verbose`

## CLICommand

-   `plugins`

## CLISubcommand

## CLIArgument
