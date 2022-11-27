# Name:
# Matriculation number: 

def xor(x1: bytes, x2: bytes) -> bytes:
    '''
    Args:
        x1: self-explanatory
        x2: self-explanatory
    Returns:
        x1 XOR x2
    '''
    # NO TOUCHING!!!!
    return bytes(a ^ b for (a, b) in zip(x1, x2))


def exchange(plaintext: bytes, ciphertext: bytes, new_plaintext: bytes) -> bytes:
    '''
    Args:
        plaintext: any spoofed plaintext for which we know the ciphertext
        ciphertext: the matching ciphertext
        new_plaintext: the new text our cipher should decrypt to
    Returns:
        our new ciphertext
    '''

    ciphertext_one = ciphertext[:int(len(ciphertext) / 2)]
    ciphertext_two = ciphertext[int(len(ciphertext) / 2):len(ciphertext)]
    plaintext_one = plaintext[:int(len(plaintext) / 2)]
    plaintext_two = plaintext[int(len(plaintext) / 2):len(plaintext)]
    encryption_one = xor(ciphertext_one, plaintext_one)
    encryption_two = xor(ciphertext_two, plaintext_two)
    new_plaintext_one = new_plaintext[:int(len(new_plaintext) / 2)]
    new_plaintext_two = new_plaintext[int(len(new_plaintext) / 2):len(new_plaintext)]
    new_ciphertext = (xor(encryption_one, new_plaintext_one)) + (xor(encryption_two, new_plaintext_two))
    return new_ciphertext



def prst(plaintext: bytes, ciphertext: bytes): #Это я для себя делал если что
    ciphertext_one = ciphertext[:int(len(ciphertext)/2)]
    ciphertext_two = ciphertext[int(len(ciphertext)/2):len(ciphertext)]
    print(ciphertext_one)
    print(ciphertext_two)
    plaintext_one = plaintext[:int(len(plaintext)/2)]
    print(plaintext_one)









if __name__ == "__main__":
    plaintext = "Hello there!0000".encode("utf-8")
    ciphertext = b'\xee\xf3\xf4rm~\xf7[y\x08\x1c\xda\xa4\xc9Wy\xa3\xa3\x81\xc1\x7f\xa3.^Fm\xa5$[\x96\x16q'

    print(f"Known plaintext:    {plaintext}")
    print(f"Known ciphertext:   {ciphertext}")

    new_plaintext = "General Kenobi00".encode("utf-8")
    new_ciphertext = exchange(plaintext, ciphertext, new_plaintext)
    expected_ciphertext = b'\xee\xf3\xf4rm~\xf7[y\x08\x1c\xda\xa4\xc9Wy\xac\xa3\x83\xc8b\xe26\x16hz\xaej\t\xcf\x16q'

    print(f"New plaintext:      {new_plaintext}")
    print(f"New ciphertext:     {new_ciphertext}")
    print(f"Exchanged worked:   {new_ciphertext == expected_ciphertext}")

    prst(plaintext, ciphertext)



