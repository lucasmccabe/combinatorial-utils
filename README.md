[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

# Combinatorial Zoo

WIP Python library providing tools for combinatorial maths (partially-ordered sets, graph polynomials, etc.).

## Table of Contents
* [Table of Contents](#table-of-contents)
* [Repo Organization](#repo-organization)
* [Example Usage](#example-usage)
* [Contact](#contact)
* [License](#license)


## Repo Organization

This repo is organized as follows:

```bash
combinatorial_zoo
├── src
│   ├── general  # general utilities, e.g. OEIS lookup
│   ├── graph  # graph problems, e.g. counting spanning trees
│   ├── posets    # constructing and analyzing partially-ordered set
```


## Example Usage

Retrieving the Tutte polynomial for the five-vertex cycle graph (C<sub>5</sub>):

```python
import combinatorial_zoo as cz
import networkx as nx

C5 = nx.cycle_graph(5)
tutte_C5 = cz.graph.polynomial.Tutte(C5)
tutte_C5.polynomial
```

```bash
>>> 'x^4 + x^3 + x^2 + x + y'
```

Evaluating the polynomial to find the number of acyclic orientations of C<sub>5</sub>:

```python
tutte_C5.evaluate(2, 0)
```

```bash
>>> 30
```


## Contact
- Lucas Hurley McCabe ([email](mailto:lucasmccabe@gwu.edu))

## License
[MIT](https://choosealicense.com/licenses/mit/)
