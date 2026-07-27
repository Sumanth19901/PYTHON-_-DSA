s1=input("Enter the first string: ").replace(" ","").lower()
s2=input("Enter the second string: ").replace(" ","").lower()
if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
else:
    print("The strings are not anagrams.")