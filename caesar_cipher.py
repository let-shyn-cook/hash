def encrypt(plaintext, shift):
    ciphertext = ""
    # Convert text to uppercase and process only A-Z
    plaintext = plaintext.upper()
    
    for char in plaintext:
        # Check if character is a letter
        if char.isalpha():
            # Convert to number (0-25), apply shift, and convert back to letter
            char_code = ord(char) - ord('A')
            shifted_code = (char_code + shift) % 26
            ciphertext += chr(shifted_code + ord('A'))
        else:
            ciphertext += char
    
    return ciphertext

def decrypt(ciphertext, shift):
    # Decryption is just encryption with negative shift
    return encrypt(ciphertext, -shift)

def brute_force_analysis(ciphertext):
    print("\nBrute Force Analysis:")
    print("Testing all possible 26 shifts (0-25):")
    
    # Dictionary of common English words to detect likely correct decryption
    common_words = ["THE", "AND", "THAT", "HAVE", "FOR", "NOT", "WITH", "YOU", "THIS", "BUT",
                   "HIS", "FROM", "THEY", "SAY", "SHE", "WILL", "ONE", "WOULD", "THERE", "THEIR"]
    
    potential_matches = []
    
    # Try all possible shifts including 0
    for shift in range(26):
        possible_plaintext = decrypt(ciphertext, shift)
        match_score = sum(word in possible_plaintext for word in common_words)
        
        # Format the output with score
        score_indicator = "*" * match_score if match_score > 0 else ""
        print(f"Shift {shift:2d}: {possible_plaintext} {score_indicator}")
        
        # Store potential matches for summary
        if match_score > 0:
            potential_matches.append((shift, possible_plaintext, match_score))
    
    # Print summary of potential matches
    if potential_matches:
        print("\nPotential matches (based on common word detection):")
        # Sort by match score (highest first)
        for shift, plaintext, score in sorted(potential_matches, key=lambda x: x[2], reverse=True):
            print(f"Shift {shift:2d}: {plaintext} (Score: {score})")
    


def analyze_letter_frequency(text):
    """Analyze letter frequency in text to assist cryptanalysis"""
    # Only count letters A-Z
    text = ''.join(char for char in text.upper() if char.isalpha())
    
    if not text:
        return {}
        
    # Count frequency of each letter
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # Convert to percentage
    total = len(text)
    for char in freq:
        freq[char] = (freq[char] / total) * 100
    
    # Sort by frequency (highest first)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_freq

def frequency_analysis(ciphertext):
    """Attempt to crack Caesar cipher using letter frequency analysis"""
    print("\nFrequency Analysis:")
    
    # Most common letters in English: E, T, A, O, I, N...
    english_common = "ETAOINSRHDLUCMFYWGPBVKXQJZ"
    
    # Get letter frequency in ciphertext
    freq = analyze_letter_frequency(ciphertext)
    if not freq:
        print("Text too short for meaningful frequency analysis")
        return
    
    print("Letter frequencies in ciphertext:")
    for char, percentage in freq[:6]:
        print(f"{char}: {percentage:.2f}%")
    
    # Assume the most frequent letter might be 'E'
    if freq:
        most_common = freq[0][0]  # Most common letter in ciphertext
        potential_shift = (ord(most_common) - ord('E')) % 26
        
        print(f"\nAssuming most common letter '{most_common}' is 'E':")
        print(f"Suggested shift: {potential_shift}")
        possible_plaintext = decrypt(ciphertext, potential_shift)
        print(f"Possible plaintext: {possible_plaintext}")

def test_cipher():
    examples = [
        ("HELLO", 3),
        ("PYTHON", 5),
        ("SECURITY", 7)
    ]
    
    print("Caesar Cipher Examples:")
    print("-" * 60)
    
    for text, shift in examples:
        print(f"\nExample with plaintext '{text}' and shift {shift}:")
        encrypted = encrypt(text, shift)
        decrypted = decrypt(encrypted, shift)
        
        print(f"Plaintext:  {text}")
        print(f"Encrypted:  {encrypted}")
        print(f"Decrypted:  {decrypted}")
        print(f"Shift used: {shift}")
        
        # Perform brute force analysis on this example
        print("\nDemonstrating brute force attack on this cipher:")
        brute_force_analysis(encrypted)
        
        # Add frequency analysis when text is long enough
        if len(text) >= 10:
            frequency_analysis(encrypted)
        
        print("-" * 60)

def main():
    # First run the test examples
    print("=== Running Test Examples ===")
    test_cipher()
    
    # Then allow user input
    while True:
        print("\n=== Caesar Cipher Program ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Brute force a ciphertext")
        print("4. Frequency analysis")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Exiting program. Goodbye!")
            break
            
        if choice in ['1', '2']:
            text = input("Enter the text: ")
            while True:
                try:
                    shift = int(input("Enter the shift (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Shift must be between 1 and 25")
                except ValueError:
                    print("Please enter a valid number")
            
            if choice == '1':
                result = encrypt(text, shift)
                print(f"\nEncrypted text: {result}")
            else:
                result = decrypt(text, shift)
                print(f"\nDecrypted text: {result}")
                
        elif choice == '3':
            text = input("Enter the ciphertext to crack: ")
            brute_force_analysis(text)
            
        elif choice == '4':
            text = input("Enter the ciphertext for frequency analysis: ")
            frequency_analysis(text)
            
        else:
            print("Invalid choice. Please try again.")
# Performance analysis
print("\nPerformance Analysis:")
print("- Time complexity: O(n) where n is the length of the ciphertext")
print("- Space complexity: O(n) for storing all possible plaintexts")
print("- Security assessment: Extremely weak, breakable instantly by brute force")
print("- With only 26 possible keys, Caesar cipher can be broken in microseconds by modern computers")
print("- This demonstrates why Caesar cipher is only used for educational purposes today")

if __name__ == "__main__":
    main()