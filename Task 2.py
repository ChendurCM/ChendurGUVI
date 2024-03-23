# Count vowels in Given String
def count_vowels(string):
    # Convert the string to lowercase to simplify counting
    string = string.lower()
    
    # Define a dictionary to store the count of each vowel
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Iterate through each character in the string
    for char in string:
        # Check if the character is a vowel
        if char in 'aeiou':
            # Increment the count of the vowel in the dictionary
            vowel_counts[char] += 1
    
    # Calculate the total number of vowels
    total_vowels = sum(vowel_counts.values())
    
    return total_vowels, vowel_counts

# Main function
if __name__ == "__main__":
    # Define the input string
    input_string = "Guvi Geeks Network Private Limited"
    
    # Call the function to count vowels
    total_vowels, vowel_counts = count_vowels(input_string)
    
    # Print the results
    print("Total number of vowels:", total_vowels)
    print("Count of each individual vowel:")
    for vowel, count in vowel_counts.items():
        print(vowel, ":", count)


# Pyramid of numbers
        rows = 6  # Number of rows in the pyramid
num = 1   # Starting number

# Outer loop for the number of rows
for i in range(1, rows + 1):
    # Print spaces for alignment
    for j in range(1, rows - i + 1):
        print(" ", end="")
    
    # Inner loop for printing numbers
    for k in range(1, i + 1):
        if num < 21:
            print(f" {num} ", end="")
        else:
            print(num, end="")
        num += +1
    
    # Move to the next line after printing each row
    print()


# Remove vowels from string
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    # Use generator expression to filter out vowels
    filtered_string = ''.join(char for char in input_string if char not in vowels)
    return filtered_string

# Test the function
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    result_string = remove_vowels(input_string)
    print("String with vowels removed:", result_string)


# Count of Unique characters
    def count_unique_characters(input_string):
        unique_characters = set(input_string)
        return len(unique_characters)

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    unique_count = count_unique_characters(input_string)
    print("Number of unique characters:", unique_count)


    # Palindrome or not
    def is_palindrome(input_string):
    # Convert the input string to lowercase to ignore case sensitivity
        input_string = input_string.lower()
    # Remove spaces from the input string
        input_string = input_string.replace(" ", "")
    
    # Check if the string is equal to its reverse
        return input_string == input_string[::-1]

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


#common substring
        def longest_common_substring(string1, string2):
    # Initialize a matrix to store the length of the longest common suffix
    # of substrings ending at each pair of indexes
            matrix = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

    # Variable to store the length of the longest common substring
            max_length = 0
    # Variable to store the ending index of the longest common substring in the first string
            end_index = 0

            for i in range(1, len(string1) + 1):
                for j in range(1, len(string2) + 1):
                     if string1[i - 1] == string2[j - 1]:
                        matrix[i][j] = matrix[i - 1][j - 1] + 1
                        if matrix[i][j] > max_length:
                            max_length = matrix[i][j]
                            end_index = i
                     else:
                        matrix[i][j] = 0

    # Extract the longest common substring
            longest_substring = string1[end_index - max_length: end_index]
            return longest_substring

if __name__ == "__main__":
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    longest_substring = longest_common_substring(string1, string2)

    if longest_substring:
        print("The longest common substring is:", longest_substring)
    else:
        print("There is no common substring.")


# Most frequent character
def most_frequent_character(input_string):
    # Create a dictionary to store character frequencies
            char_frequency = {}

    # Count frequencies of characters in the string
            for char in input_string:
                if char in char_frequency:
                    char_frequency[char] += 1
                else:
                    char_frequency[char] = 1

    # Find the character with the maximum frequency
            max_frequency = 0
            most_frequent_char = None
            for char, frequency in char_frequency.items():
                if frequency > max_frequency:
                    max_frequency = frequency
                    most_frequent_char = char

            return most_frequent_char

if __name__ == "__main__":
    input_string = input("Enter a string: ")

    most_frequent_char = most_frequent_character(input_string)

    if most_frequent_char:
        print("The most frequent character is:", most_frequent_char)
    else:
        print("The string is empty.")


def is_anagram(string1, string2):
    # Remove spaces and convert strings to lowercase for case-insensitive comparison
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Check if the length of both strings is the same
    if len(string1) != len(string2):
        return False

    # Sort both strings and compare if they are equal
    return sorted(string1) == sorted(string2)

if __name__ == "__main__":
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    if is_anagram(string1, string2):
        print("The strings are anagrams of each other.")
    else:
        print("The strings are not anagrams of each other.")


def count_words(input_string):
    # Split the string into words based on whitespace
    words = input_string.split()
    # Return the number of words
    return len(words)

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    word_count = count_words(input_string)
    print("Number of words:", word_count)