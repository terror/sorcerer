# sorcerer :crystal_ball:
[![Build Status](https://travis-ci.com/terror/sorcerer.svg?branch=master)](https://travis-ci.com/terror/sorcerer)  
Programming problem solution README table generator

# Installation
You can simply use pip to install sorcerer:  
```bash
$ pip install sorcerer
```

# Usage
Run sorcerer as a command
```bash
$ sorcerer
```  
This will prompt you for your github repository link and absolute path to the repository.

## Example
```bash
Github link to repository: https://github.com/sorcerer/example
Local path to repository: /Absolute/path/to/repository
```

This will then look for a `config.json` file that looks something like this

```JSON
{
"Ignore": ["CSES"],
"Paths": ["Kattis", "Dmoj", "Leetcode"]
}
```

## File Structure
`sorcerer` as of now, requires a specific file structure in order to work.

```
Github/lazy/example/
├── SITE_NAME
│   └── PROBLEM_ID
│       └── solution.cpp
├── SITE_NAME
│   ├── PROBLEM_ID
│   │   └── solution.cpp
│   └── PROBLEM_ID
│       └── solution.py
├── SITE_NAME
│   ├── PROBLEM_ID
│   │   ├── solution.cpp
│   │   └── solution.py
│   └── PROBLEM_ID
│       └── solution.py
├── README.md
└── config.json
```

Where PROBLEM_ID is the id for the solved problem and SITE_NAME is the problem website name.  
For instance, https://open.kattis.com/problems/opensource -> Kattis/opensource/solution

## Result

Potential sample result for a folder in the sample file structure above.

### Kattis
| Problem | Languages |
| ------- | --------- |
 [Gerrymandering](https://open.kattis.com/problems/gerrymandering) | [Python](https://github.com/terror/sorcerer/blob/master/example/Kattis/gerrymandering/solution.py)
 [Fenwick](https://open.kattis.com/problems/fenwick) | [C++](https://github.com/terror/sorcerer/blob/master/example/Kattis/fenwick/solution.cpp), [Python](https://github.com/terror/sorcerer/blob/master/example/Kattis/fenwick/solution.py)


The current sites being supported can be found [here](https://github.com/terror/sorcerer/blob/master/constants/sites.py). A full sample repository can be found [here](https://github.com/terror/sorcerer/tree/master/example) 

# Development
Fork the repository
```bash
$ git clone <fork>
```
```
$ pip3 install -r requirements.txt
```
```
$ python3 sorcerer
```

# License
MIT
