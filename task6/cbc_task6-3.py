# XOR two bytearrays
def xor(first, second):
    return bytearray(x ^ y for x, y in zip(first, second))

def prepare_ciphertext_guess(padded_plaintext, known_iv, next_iv):

    # XOR the padded plaintext with the next IV (which the oracle will use)
    xor_with_next_iv = xor(padded_plaintext, next_iv)

    # XOR the result with the known IV (which was used by Bob's secret message)
    manipulated_ciphertext = xor(xor_with_next_iv, known_iv)

    print(f"Manipulated Ciphertext Guess (hex): {manipulated_ciphertext.hex()}")

# Bob's IV used in the first encryption (known)
known_iv = bytes.fromhex("ef7fd84fdbeab0aa3c6ac3ad3f4295f0")

next_iv = bytes.fromhex("ebfc9f0bdceab0aa3c6ac3ad3f4295f0") # The next IV 

# Pre-padded guesses for "Yes" and "No"
padded_yes = bytes.fromhex("5965730d0d0d0d0d0d0d0d0d0d0d0d0d")
padded_no  = bytes.fromhex("4e6f0e0e0e0e0e0e0e0e0e0e0e0e0e0e")

# Choose the guess to test
padded_plaintext = padded_yes

# run the function
prepare_ciphertext_guess(padded_plaintext, known_iv, next_iv)
