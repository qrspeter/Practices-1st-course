from random import shuffle
s1='\0\0\0\0'
s2='\0\0\0\0\0\0\0\0'
example_table = list(range(0, 256))
shuffle(example_table)
def xor8(message: str) -> int:
    hash = len(message) % 256
    for i in message:
        hash = hash ^ ord(i)
    return message

def hash8(message: str, table) -> int:
    """Pearson hashing."""
    hash = len(message) % 256
    for i in message:
        hash = table[hash ^ ord(i)]
    return hash

print(hex(hash8(s1, example_table)))
print(hex(hash8(s2, example_table)))

print(hex(xor8(s1)))
print(hex(xor8(s2)))