s = 'sea'
# ans = sum(ord(c) for c in s)
ans = sum(map(ord, s[:2]))
print(ans)
