import os
import pathlib
import importlib
from ggcli import PACKAGE_ROOT
import ggcli.cli.model.option as o


class OptionProvider:

    def get(self):
        result = dict()
        root_options_path = pathlib.Path(self._get_options_path())
        options_paths = [x for x in root_options_path.glob('./*.py')]

        for option_path in options_paths:
            module_path = str(option_path)
            spec = importlib.util.spec_from_file_location(
                module_path, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            option = o.Option(
                option_path.stem,
                getattr(module, "main", lambda: None)
            )
            result[option.name] = option
        return result

    def _get_options_path(self):
        return os.path.join(os.path.dirname(PACKAGE_ROOT), "ggcli/options/")


instance = OptionProvider()
