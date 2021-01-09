#!/usr/bin/python3

"""
   Copyright  2021  Andrea Tedeschi  DontPanicO

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import os
import sys
import subprocess
import argparse

__author__ = "DontPanicO"
__version__ = "1.0"

DEVNULL = open(os.devnull, 'wb')
USAGE = """
python3 ifind.py <directory> <search> [options]; OR (if the file has been correctly installed)
ifind  [options] <directory> <search>
=======================================
Examples:                            ¦¦
ifind . '^thi.+ mine$' --regex       ¦¦
ifind . 'hello world'                ¦¦
=======================================
"""


if __name__ == '__main__':

        # Inatialize the argument parser
        parser = argparse.ArgumentParser(
                        usage=USAGE,
                        description="A tool to scan recursively a directory and grep in the content of its files",
                )

        parser.add_argument(
                        "directory",
                        help="The research root directory",
                )

        parser.add_argument(
                        "search",
                        help="The text or the pattern to look for in files content",
                )

        parser.add_argument(
                        "-r", "--regex",
                        help="A flag telling the script to treat",
                        action="store_true", default=False,
                )
        parser.add_argument(
                        "-i", "--case-insensitive",
                        help="If present the script will act case insensitive",
                        action="store_true", default=False,
                )

        # Parse args
        args = parser.parse_args()

        # Get positional args values
        directory = args.directory
        search = args.search

        # Store options in a dict object adn define a string containing all options
        options = dict()
        options['regex'] = "-E" if args.regex else ""
        options['insensitive'] = "-i" if args.case_insensitive else ""
        parsed_options = " ".join(options.values()).strip()

        # Define the right command. Different if there is or there is no options
        if not any(options.values()):
            command = f"find {directory} -type f -print0 | xargs -0 grep {search} | cut -d':' -f1"
        else:
            command = f"find {directory} -type f -print0 | xargs -0 grep {parsed_options} {search} | cut -d':' -f1"

        result = subprocess.check_output(command, shell=True, stdin=DEVNULL, stderr=DEVNULL).decode()

        # Output if no result has been find
        if not result:
            print(f"No results for your search '{search}'")
            sys.exit(0)

        # Output if some result has been find
        lines = []
        for line in result.split("\n"):
            if line not in lines:
                lines.append(line)

        output = "\n".join(lines)

        print(f"'{search}' is present in files:")
        print(output.rstrip())
