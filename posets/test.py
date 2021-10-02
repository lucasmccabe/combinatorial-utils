import posets.poset
import posets.example_posets

example = example_posets.ExamplePosets()
coverage = example.finite_chain(10)

p = poset.Poset(coverage)
print(p.is_Eulerian())
