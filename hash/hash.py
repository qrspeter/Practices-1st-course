from random import shuffle

def table_generator(size: int) -> list:
    example_table = list(range(0, size)) 
    shuffle(example_table) 
    return example_table

def hash8(message: str, table) -> int: 
    """Pearson hashing.""" 
    hash = len(message) % 256 
    for i in message:
        i = bytes(i, encoding='cp1251')
        hash = table[hash ^ ord(i)] 
        
    return hash 

filename = 'meeting_saved_chat.txt'
with open(filename, 'r', encoding='cp1251') as fin:
    f = fin.readlines()
    
table_size = 256
example_table = table_generator(table_size)
hash_lst = []
for i in f:
    hash_lst.append(hash8(i, example_table))
    
print(f"Hash list is \n{hash_lst}")
    
