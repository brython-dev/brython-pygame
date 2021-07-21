# Brython-pygame

Motivation: to write a pygame module that allows interoperability
for a game initially written for only pygame+pygame,
and let users run this program in a web context


## Installation

[1]
If you want to run examples, just move the pygame folder to `scripts/Lib/site-packages`,
then run a HTTP server using `serve_files_HTTP.py`. Browse using Firefox or Chrome,
and go to `examples` to see what can be done with *Brython-pygame*.

[2]
If your goal is to make an existing program work in the web, copy the
`serve_files_HTTP.py` file, and the `pygame/` folder, and the `scripts/` folder
into your project's source folder.

You will also need an `index.html` file, you can take one from `examples/` and modify
it to suit your needs.

## Credits

Thanks to everyone who have helped in making this python module
possible and useful.
* creators of the [Pygame lib](https://github.com/pygame/pygame)
* Billy Earney (first sketch)
* Thomas Iwaszko (feature implementation, pygame 2.01 compatibility, testing)


## License

This python module is distributed under [GNU LGPL version 2.1](https://www.gnu.org/copyleft/lesser.html),
which can be found in the file docs/LGPL.txt.
