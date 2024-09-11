vowels = "aeiouAEIOU"  
string = input("Enter a string: ") 

vowels_list = [char for char in string if char in vowels]

print(vowels_list)