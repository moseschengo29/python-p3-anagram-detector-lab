# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the word to lowercase for case-insensitive matching

    def match(self, possible_anagrams):
        # Create a function to normalize a word (convert to lowercase and sort characters)
        def normalize(word):
            return ''.join(sorted(word.lower()))

        # Normalize the original word
        normalized_word = normalize(self.word)

        # Filter possible anagrams that match the normalized word
        anagrams = [word for word in possible_anagrams if normalize(word) == normalized_word]

        return anagrams  
           
    
    
anagram = Anagram("listen")
matches = anagram.match(['enlists', 'google', 'inlets', 'banana'])
print(matches)

# word = ['a','m','x','d','e']
# print(sorted(word)) 