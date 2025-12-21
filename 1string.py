"""
1. Create a String
2. Print String
3. String Slicing
4. Update String
5. String Methods: len(s), s.upper(), s.lower(), s.strip(), s.replace(str1, str2), s.swapcase(),
   s.count("char", start_index, end_index),
   s.startswith('char', start_index, end_index), s.endswith('char', start_index, end_index) 
6. Reverse a string: s.reverse(), s=s[::-1]
7. Check Palindrome:  print("Palindrome") if s==s[::-1]
8. Check Anagram: print("Anagram") if (srted(s.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower()))
9. Remove Dulicates
10. Count Alphabate in string: count=sum([1 for c in string if c.isalpha()])
11. Count Digit in string: count=sum([1 for c in string if c.isdigit()])
12. Characters frequency in a string
13. Count Method
"""
s="Python Programming"
print("String: ", s)

# String Slicing
print("\n----------String Slicing----------")
print(f"Characters from index 1 to 3 : ", s[1:4])        # characters from index 1 to 3
print(f"Characters from start to index 2 : ", s[:3])     # from start to index 2
print(f"Characters from index 3 to end : ", s[3:])       # from index 3 to end

# Update String
"""IMPORTANT:
Strings are immutable, which means that they cannot be changed after they are created.
If we need to manipulate strings then we can use methods like concatenation, slicing or 
formatting to create new strings based on original."""
print("\n")
s = "p" + s[1:]   # create new string
print("Created New string : ", s)

print("Length of the String: ", len(s))

# String Methods
print("String to Lower : ", s.lower())   # print(s) will still print "Python Programming" as string is immutable. So, Assign this s.lower() to same variable or to some other variable.
print("String to Upper: ", s.upper())    # print(s) will still print "Python Programming" as string is immutable. So, Assign this s.upper() to same variable or to some other variable.
print("String After Replace: ", s.replace("Programming", "Language"))
s="Python Programming"
s1=s.replace("P", "")     # IMPORTANT: 's' will remain unchanged untill you assign the updated value to the same variable, or create some other varbale
print(s)                  # This will Print "Python Programming" as string is immutable
print(s1)                 # This Will Print "ython rogramming"
print("String After strip: ", s.strip())
print("String after swaped the case: ", s.swapcase())

# Reverse the String
print(f"String in Reverse Order: ", s[::-1])             # reverse string
# Slicing ([::-1]) is generally the best choice for its simplicity, readability, and performance.
rev="".join(reversed(s))
print("Revered String: ", rev)

# Palindrome
s1="helleh"
if s1==s1[::-1]:
    print(f"The String '{s1}' is a Palindrome String")

# Anagram
s1="listen"
s2="Silent"

# Anagram
if sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower()):
    print(f"'{s1}' and '{s2}' are 'Anagram' String")

# Remove Duplicates
res=""
for c in s: 
    if c not in res:
        res+=c
print("New String After Removing the Duplicates: ", res)

# Character Frequency
frequency={}
for c in s:
    frequency[c] = frequency.get(c, 0) + 1
print("Characters frequency in a string: ", frequency)

# Count Method
sentence = "Python is fun and Python is powerful."
# Count Single Chanracter
single_char_count = sentence.count("P")
print(f"Counted 'P' in sentence {sentence}: ", single_char_count)
# Count Word
count_python = sentence.count("Python")
print(f"Counted 'Python' in sentence {sentence}: ", count_python)
# Count occurrences of "apple" from index 1 up to (but not including) index 20
s = "apple banana apple grape apple"
count_range = s.count("apple", 1, 20)
print("Count occurrences of 'apple' from index 1 up to (but not including) index 20: ", count_range)
# Case-sensitive search
text = "Hello, world! Hello again!"
count_hello_case = text.count("hello") # Case-sensitive search
count_hello_ignore_case = text.lower().count("hello") # Case-insensitive search
print(f"Case-sensitive count: {count_hello_case}")
print(f"Case-insensitive count: {count_hello_ignore_case}")