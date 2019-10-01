"""Solution 1.

The basic solution here is to have a subset function that takes
in a set, looks at each value of the set sequentially, and forms
the set of that value plus the subsets of all of the other values.

Pseudocode:

    subsets(set):
        all_sets = set()
        for element in set:
            all_sets.add(element)
            for subset in set - element:
                all_sets.add(element + subset)

One interesting note is that we can't do a set of the empty set in Python.
My first thought was that we could get around this by adding an empty list
to the set or something like that, if desired, but it doesn't look like
Python lets us do this either.
"""

def power_set(s):
    all_subsets = set()
    for element in s:
        all_subsets.add(frozenset([element]))
        element_set = set([element])
        elementless_power_set = power_set(s - element_set)
        for subset in elementless_power_set:
            all_subsets.add(frozenset(element_set | subset))
    
    return all_subsets

if __name__ == "__main__":
    s = set([1,2,3,4,5,6,7,8])
    s_power_set = power_set(s)
    for elem in s_power_set:
        print(elem)
    
    print(len(s_power_set) + 1, 2 ** len(s))
