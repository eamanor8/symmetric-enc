# XOR two bytearrays
def xor(first, second):
    return bytearray(x ^ y for x, y in zip(first, second))

# Given the following:
P1 = "This is a known message!"  # Plaintext 1
C1 = bytes.fromhex("a469b1c502c1cab966965e50425438e1bb1b5f9037a4c159")  # Ciphertext 1 (in hex)
C2 = bytes.fromhex("bf73bcd3509299d566c35b5d450337e1bb175f903fafc159")  # Ciphertext 2 

# Convert P1 to bytes
P1_bytes = bytes(P1, 'utf-8')

# Calculate the keystream
keystream = xor(P1_bytes, C1)

# Use the keystream to recover P2 by XORing with C2
P2_bytes = xor(keystream, C2)

# Convert P2 bytes back to a string 
P2 = P2_bytes.decode('utf-8')
print(f"Recovered P2: {P2}")
