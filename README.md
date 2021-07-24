# py-unicode
> A unicode rendering system on the command line.

py-unicode is a mini-project written in Python 3.8 for rendering
unicode for Windows, Mac, and Linux systems.

## Installation

Install the repository as a .zip file, then extract the contents to whereever best.

In order to use py-unicode, the following programs need to be installed:

* [Python 3.8](https://www.python.org/downloads/) (Tested, though any version of Python 3 should work)
  * [pyperclip](https://pypi.org/project/pyperclip/)

## Usage example

```sh
python unicode.py 203d
```
Now, the unicode character with the code `203d`(‽) should be copied to your clipboard.

```sh
python unicode.py 3c9
```
This causes the unicode character with the code `3c9`(ω) to be copied to your clipboard.

## Release History

* 1.0.0
  * Initial release.

## Meta

Distributed under the MIT license. See ``LICENSE`` for more information.

[Me on Github!](https://github.com/MochiLunchbox/)

## Contributing

1. Fork it (<https://github.com/MochiLunchbox/py-unicode/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
