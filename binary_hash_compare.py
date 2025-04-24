import hashlib

def calculate_file_hash(filename, hash_algorithm='sha256'):
    """Calculate hash of a file using specified algorithm."""
    hash_obj = hashlib.new(hash_algorithm)
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def compare_files(file1, file2):
    """Compare two files both in raw binary and hash values."""
    # Compare file sizes
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        content1 = f1.read()
        content2 = f2.read()
        
    print(f"\nFile size comparison:")
    print(f"{file1}: {len(content1)} bytes")
    print(f"{file2}: {len(content2)} bytes")
    
    # Compare raw binary content
    print("\nRaw binary content comparison:")
    if content1 == content2:
        print("Raw binary content is identical")
    else:
        print("Raw binary content is different")
        # Find the first difference
        for i, (b1, b2) in enumerate(zip(content1, content2)):
            if b1 != b2:
                print(f"First difference at byte position {i}")
                print(f"File1 byte: {hex(b1)}")
                print(f"File2 byte: {hex(b2)}")
                break
    
    # Compare different hash algorithms
    algorithms = ['md5', 'sha1', 'sha256', 'sha512']
    print("\nHash comparison:")
    for algorithm in algorithms:
        hash1 = calculate_file_hash(file1, algorithm)
        hash2 = calculate_file_hash(file2, algorithm)
        print(f"\n{algorithm.upper()} Hash:")
        print(f"{file1}: {hash1}")
        print(f"{file2}: {hash2}")
        print(f"Hashes {'match' if hash1 == hash2 else 'do not match'}")

if __name__ == "__main__":
    file1 = "collision1.bin"
    file2 = "collision2.bin"
    
    print("Comparing files:", file1, "and", file2)
    try:
        compare_files(file1, file2)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please make sure both binary files exist in the current directory.")