# При создании экземпляра класса ArgumentParser есть возможность использовать различные аргументы.
# https://docs.python.org/3.10/library/argparse.html#argumentparser-objects
# prog - The name of the program
#   (default: os.path.basename(sys.argv[0]))
# usage - The string describing the program usage
#   (default: generated from arguments added to parser)
# description - Text to display before the argument help
#   (by default, no text)
# epilog - Text to display after the argument help
#   (by default, no text)
# parents -
#   A list of ArgumentParser objects whose arguments should also be included
# formatter_class -
#   A class for customizing the help output
# prefix_chars - The set of characters that prefix optional arguments
#   (default: ‘-‘)
# fromfile_prefix_chars - The set of characters that prefix files from which additional arguments should be read
#   (default: None)
# argument_default - The global default value for arguments
#   (default: None)
# conflict_handler - The strategy for resolving conflicting optionals
#   (usually unnecessary)
# add_help - Add a -h/--help option to the parser
#   (default: True)
# allow_abbrev - Allows long options to be abbreviated if the abbreviation is unambiguous.
#   (default: True)
# exit_on_error - Determines whether or not ArgumentParser exits with error info when an error occurs.
#   (default: True)

# Но большинство из них имеют оптимальные значения по умолчанию.

import argparse

parser = argparse.ArgumentParser(prog='average',
                                 description='My first argument parser',
                                 epilog='Returns the arithmetic mean')
...
# ● prog — заменяет название файла в первой строке справки на переданное имя,
# ● description — описание в начале справки
# ● epilog — описание в конце справки
