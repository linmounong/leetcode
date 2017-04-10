def foo(words):
  before = {}
  voc = set()
  for word in words:
    voc.update(word)
    for i, j in zip(word[:-1], word[1:]):
      if i != j:
        if j not in before:
          before[j] = set()
        before[j].add(i)
  memo = {}
  def bar(c):
    if c not in memo:
      if c not in before:
        memo[c] = 0
      else:
        memo[c] = max(bar(c2) for c2 in before[c]) + 1
    return memo[c]
  return sorted(voc, key=bar)

print foo([
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
])
