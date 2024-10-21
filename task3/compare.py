def compare_with_bin_file(file_path, generated_ciphertext):
    """
    Compare the content of a binary file with the generated ciphertext.
    
    :param file_path: Path to the binary file to compare
    :param generated_ciphertext: The ciphertext generated from the encryption
    :return: True if the content matches, False otherwise
    """
    try:
        with open(file_path, 'rb') as f:
            expected_ciphertext = f.read()
            if expected_ciphertext == generated_ciphertext:
                print(f"\nOutput of encrypting the plaintext matches {file_path}!")
                return True
            else:
                print(f"Ciphertext does NOT match for {file_path}.")
                return False
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return False
