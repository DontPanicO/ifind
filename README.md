# ifind
A simple recursive tool to grep string from all files contained in a directory

### Installation

- Clone the repo:

  - git clone https://github.com/DontPanicO/ifind.git

- Then run:

  - cd ifind
  - chmod +x ifind.py; OR chmod +x ifind.sh (if you have no python3 interpreter)
  - ln -s /path/to/ifind.py /usr/local/bin/ifind

### Some Info

- This is a very simple tool, that helped me when, at work or for personal reasons, I deal with big prjects that I don't know. In order
  to find imports and variables grep -Fr is all that you need, but the output can sometimes be too much. This tool, by default, provides
  a simple list of file where the string/regex is present. Anyway it includes options to display also line numbers or lines (as grep -Fr
  does).


