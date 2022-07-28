from setuptools import Command
import os
from ggcli import PACKAGE_ROOT
from glob import glob
import pathlib
import ggcli.cli.driver2.model.command as c
import importlib


class CommandProvider():

    def get(self):
        result = dict()
        commands_path_string = self._get_commands_path()

        commands_path = pathlib.Path(commands_path_string)

        commands = [x for x in commands_path.iterdir() if x.is_dir()
                    and not str(x.name).startswith(".")
                    and not str(x.name).startswith("__")]
        for command_path in commands:
            subcommands = list(command_path.glob('./*.py'))
            subcommands_list = []
            for subcommand_path in subcommands:
                module_path = str(subcommand_path)
                spec = importlib.util.spec_from_file_location(
                    module_path, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                subcommand = c.Command(
                    name=subcommand_path.stem,
                    main=getattr(module, "main", lambda: None),
                    help=getattr(module, "help", lambda: None),
                    alias=getattr(module, "alias", lambda: None)
                )
                subcommands_list.append(subcommand)
            result[command_path.name] = subcommands_list
        return result

    def _get_commands_path(self):
        return os.path.join(os.path.dirname(PACKAGE_ROOT), "ggcli/commands/")


instance = CommandProvider()
