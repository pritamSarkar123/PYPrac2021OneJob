from itertools import permutations,combinations,combinations_with_replacement,product

print(list(product([1,2,3],repeat=2)))
print(list(product([1,2,3],[4,5,6,7])))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
# [(1, 4), (1, 5), (1, 6), (1, 7), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7)]

print(list(permutations(range(3))))
print(list(permutations(range(3),2)))
print(list(permutations('abc',3)))
# [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
print(list(combinations(range(3),2)))
print(list(combinations('abc',3)))
# [(0, 1), (0, 2), (1, 2)]
# [('a', 'b', 'c')]
print(list(combinations_with_replacement(range(3),2)))
print(list(combinations_with_replacement('abc',3)))
# [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
# [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'b', 'b'), ('a', 'b', 'c'), ('a', 'c', 'c'), ('b', 'b', 'b'), ('b', 'b', 'c'), ('b', 'c', 'c'), ('c', 'c', 'c')]
