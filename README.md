[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

# Combinatorial Zoo

WIP Python library providing tools for combinatorial maths.



## Table of Contents
* [Table of Contents](#table-of-contents)
* [Repo Organization](#repo-organization)
* [Example Usage](#example-usage)
* [Contact](#contact)
* [License](#license)



## Repo Organization

This repo is organized as follows:

```bash
combinatorial-zoo
├── general  # general utilities, e.g. OEIS lookup
├── graph  # graph problems, e.g. counting spanning trees
├── posets    # constructing and analyzing partially-ordered set
```


## Example Usage

```python
import posets

example = posets.ExamplePosets()
coverage = example.finite_chain(10)

p = posets.Poset(coverage)
print(p.is_Eulerian())
```

```bash
>>> False
```

## Contact
- Lucas Hurley McCabe ([email](mailto:lucasmccabe@gwu.edu))

## License
[MIT](https://choosealicense.com/licenses/mit/)
