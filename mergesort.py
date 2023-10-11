def merge(a, b):
  """Merge two sorted lists."""
  c = []
  i = j = 0
  while i < len(a) and j < len(b):
    if a[i] < b[j]:
      c.append(a[i])
      i += 1
    else:
      c.append(b[j])
      j += 1
  c += a[i:]
  c += b[j:]
  return c


def merge_sort(a):
  """Merge sort a list."""
  if len(a) <= 1:
    return a
  else:
    mid = len(a) // 2

    
    return merge(merge_sort(a[:mid]), merge_sort(a[mid:]))
  
a=list(map(int,input().split()))
print(*merge_sort(a))