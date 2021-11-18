[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

# TUSC 🐘: Toolbox for Understanding Some things in Combinatorics

WIP Python library providing tools for combinatorial maths (partially-ordered sets, graph polynomials, etc.).

## Table of Contents
* [Table of Contents](#table-of-contents)
* [Repo Organization](#repo-organization)
* [Setup](#setup)
* [Example Usage](#example-usage)
* [Requirements](#requirements)
* [Contact](#contact)
* [License](#license)


## Repo Organization

This repo is organized as follows:

```bash
tusc
├── src
│   ├── general  # general utilities, e.g. OEIS lookup
│   │   ├── utils
│   ├── graph  # graph problems, e.g. counting spanning trees, retrieving graph polynomials
│   │   ├── distance
│   │   ├── enumeration
│   │   ├── manipulation
│   │   ├── matching
│   │   ├── polynomial
│   ├── posets    # constructing and analyzing partially-ordered sets
│   │   ├── utils
│   │   ├── example_posets
│   │   ├── poset
```

## Setup

1. Clone this repo
2. cd into the `tusc` directory and run the following in your shell: ```pip install -r requirements.txt```


## Example Usage

Retrieving the Tutte polynomial for the five-vertex cycle graph (C<sub>5</sub>):

```python
import tusc
import networkx as nx

C5 = nx.cycle_graph(5)
tutte_C5 = tusc.graph.polynomial.Tutte(C5)
tutte_C5.polynomial
```

```bash
'x^4 + x^3 + x^2 + x + y'
```

Evaluating the polynomial to find the number of acyclic orientations of C<sub>5</sub>:

```python
tutte_C5.evaluate(2, 0)
```

```bash
30
```

## Requirements
This project was created with:

- `requests==2.24.0`
- `numpy==1.19.5`
- `sympy==1.6.2`
- `networkx==2.5`


## Contact
- Lucas Hurley McCabe ([email](mailto:lucasmccabe@gwu.edu))

## License
[MIT](https://choosealicense.com/licenses/mit/)
