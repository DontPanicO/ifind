# ifind
A simple recursive tool to grep string from all files contained in a directory

### Installation

- Clone the repo:

  - git clone https://github.com/DontPanicO/ifind.git

- Then run:

  - cd ifind
  - chmod +x ifind.py
  - chmod +x ifind.sh (not needed)
  - ln -s /path/to/ifind.py /usr/local/bin/ifind

### Some Info

- This is a vey simple tool, that help me a lot when (for working or personal reasons) I deal with big project that i do not know,
  to find imports or variable in all the project. I always had to type a relative long command, or deal with not tiny output, so
  I decided to write this tool.

- By default, the tool will only lists files where the string/expression you searched for is present. If you want the tool give an
  output as grep -Fr does, use the -l option.


