## sorcerer :crystal_ball:
[![Build Status](https://travis-ci.com/terror/sorcerer.svg?branch=master)](https://travis-ci.com/terror/sorcerer)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)  
Programming problem solution README table generator

### Installation
You can simply use pip to install sorcerer:  
```bash
$ pip install sorcerer
```

### Arguments

`--git, -g`: github username (required)

### Usage
Run sorcerer as a command in your solutions directory
```bash
$ sorcerer -g [github username]
```  

This will then look for a `config.json` file that looks like this: 

```JSON
{
"Paths": ["Kattis", "Dmoj", "Leetcode"]
}
```

### File Structure
`sorcerer` as of now, requires a specific file structure in order to work.

```
example/
├── CSES
│   └── weirdalgorithm.cpp
├── Dmoj
│   ├── README.md
│   ├── anoisyclass.cpp
│   └── ccc11j1.py
├── Kattis
│   ├── README.md
│   ├── fenwick.cpp
│   ├── fenwick.py
│   └── gerrymandering.py
├── README.md
└── config.json
```

- The folder names must be the corresponding problem website names.
- The solution filenames must be the corresponding problem website problem IDs. 
- The root folder name must be the name of your github repository.

### Result

Potential sample result for a folder in the sample file structure above.

### Kattis
| Problem | Languages |
| ------- | --------- |
 [Gerrymandering](https://open.kattis.com/problems/gerrymandering) | [Python](https://github.com/terror/example/blob/master/Kattis/gerrymandering.py)
 [Fenwick](https://open.kattis.com/problems/fenwick) | [C++](https://github.com/terror/example/blob/master/Kattis/fenwick.cpp), [Python](https://github.com/terror/example/blob/master/Kattis/fenwick.py)

The current sites being supported can be found [here](https://github.com/terror/sorcerer/blob/master/sorcerer/constants/sites.py).   
A full sample repository can be found [here](https://github.com/terror/sorcerer_example).  

### Development
Fork the repository
```bash
$ git clone [fork]
$ pip3 install -r requirements.txt
$ python3 sorcerer
```
### License
MIT
