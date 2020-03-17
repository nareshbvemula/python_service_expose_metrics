#### String Methods
s = "hello world, am learning string data type"

alpha = ('a','b','c','d','e','f','g','h')
print(s.title()) # print the o/p as a Titel
print(s.endswith("e")) # Returns True/False based on the last char of the string
print(s.endswith(alpha)) # Returns with True/Fast based on the last char present in Tuple
print(s.startswith(alpha)) # Returns with True/Fast based on the first char present in Tuple
print(s.isalnum()) # True if string contains alpha numeric
print(s.isalpha()) # True if string is only alphabetic
print(s.replace("type", "type from scratch-")) # find and replace
print("\n")
print(s.join("ABCD")) # this will concinate iterable at the starting of the string repeatedly. Mainly used when we need
                        # add space or , or any delimiter before a string
print(s.istitle()) # True if the String is titel form
print(s.split(" ")) # Trurn a list and sprint based on the separator
print(s.index('data')) # return index of string in s, raise an exception if the string not found.
print(s.encode(encoding='UTF-8',errors='ignore'))
print(s.find('string')) # returns index of first occurrence of a sub string, returns -1 if the string not found.
print(s.isidentifier()) # Tur if the string is an identifier in Python