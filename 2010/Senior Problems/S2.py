dict1 = {}
for t in range(int(input(''))):
    encoded_value = input().split(' ')
    dict1[encoded_value[0]] = encoded_value[1]
encoded_string = input('')
decoded_string = ''
index = 0
for a in range(len(encoded_string)):
    for k,v in dict1.items():
        if encoded_string[index:index+len(v)]==v:
            index=index+len(v)
            decoded_string+=k
print(decoded_string)
