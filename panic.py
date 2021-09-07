phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)

for i in range(4):
    plist.pop()

plist.remove("'")
plist.pop(0)
plist.insert(2, plist.pop(3))
plist.insert(4, plist.pop(-1))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
