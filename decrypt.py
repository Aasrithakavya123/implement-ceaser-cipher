def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) + shift_amount
            if char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
            elif char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char) - shift_amount
            if char.islower():
                if char_code < ord('a'):
                    char_code += 26
                decrypted_text += chr(char_code)
            elif char.isupper():
                if char_code < ord('A'):
                    char_code += 26
                decrypted_text += chr(char_code)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
        return
    
    message = input("Enter your message: ").strip()
    shift = int(input("Enter shift value: ").strip())
    
    if choice == 'E':
        result = encrypt(message, shift)
        print("Encrypted message:", result)
    elif choice == 'D':
        result = decrypt(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
