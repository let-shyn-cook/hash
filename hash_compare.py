import hashlib
import random

def calculate_hashes(content):
    # Calculate SHA-256
    sha256_hash = hashlib.sha256(content.encode()).hexdigest()
    
    # Calculate SHA-3
    sha3_hash = hashlib.sha3_256(content.encode()).hexdigest()
    
    # Calculate MD5
    md5_hash = hashlib.md5(content.encode()).hexdigest()
    
    return sha256_hash, sha3_hash, md5_hash

def compare_hashes(original_hashes, modified_hashes):
    for hash_type, (orig, mod) in zip(['SHA-256', 'SHA-3', 'MD5'], 
                                    zip(original_hashes, modified_hashes)):
        same_chars = sum(1 for a, b in zip(orig, mod) if a == b)
        percentage = (same_chars / len(orig)) * 100
        print(f"\n{hash_type} comparison:")
        print(f"Original : {orig}")
        print(f"Modified : {mod}")
        print(f"Similarity: {percentage:.2f}%")

def modify_character(content, position, new_char):
    return content[:position] + new_char + content[position + 1:]

# Create a sample text file if it doesn't exist
with open('sample.txt', 'w') as f:
    f.write("This is a sample text for hash comparison.")

while True:
    # Read the original content
    with open('sample.txt', 'r') as f:
        content = f.read()
    
    print("\nCurrent content:", content)
    print("\nOriginal hashes:")
    original_hashes = calculate_hashes(content)
    print("SHA-256:", original_hashes[0])
    print("SHA-3:", original_hashes[1])
    print("MD5:", original_hashes[2])
    
    print("\nSelect an option:")
    print("1: Input a character to change and compare hashes")
    print("2: Change a random character and compare hashes")
    print("3: Exit program")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        pos = int(input("Enter position to change (0-" + str(len(content)-1) + "): "))
        new_char = input("Enter new character: ")
        if 0 <= pos < len(content):
            modified_content = modify_character(content, pos, new_char)
            modified_hashes = calculate_hashes(modified_content)
            compare_hashes(original_hashes, modified_hashes)
            
            # Save the modified content
            with open('sample.txt', 'w') as f:
                f.write(modified_content)
    
    elif choice == '2':
        pos = random.randint(0, len(content)-1)
        new_char = chr(random.randint(32, 126))  # ASCII printable characters
        print(f"Changing character at position {pos} to '{new_char}'")
        modified_content = modify_character(content, pos, new_char)
        modified_hashes = calculate_hashes(modified_content)
        compare_hashes(original_hashes, modified_hashes)
        
        # Save the modified content
        with open('sample.txt', 'w') as f:
            f.write(modified_content)
    
    elif choice == '3':
        print("Program ended.")
        break
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")