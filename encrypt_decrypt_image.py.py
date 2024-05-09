from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import io

def encrypt_image(image_path, key, output_path):
    # Read image
    image = Image.open(image_path)
    # Convert image to bytes
    byte_io = io.BytesIO()
    image.save(byte_io, format='jpeg')
    byte_data = byte_io.getvalue()
    # Pad the bytes to match the block size
    padded_data = pad(byte_data, AES.block_size)
    # Encrypt bytes using AES
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(padded_data)
    # Save encrypted data to a file
    with open(output_path, 'wb') as f:
        f.write(ciphertext)
    return cipher.iv

def decrypt_image(encrypted_path, key, iv, output_path):
    # Read encrypted data from file
    with open(encrypted_path, 'rb') as f:
        ciphertext = f.read()
    # Decrypt bytes using AES
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    # Convert decrypted bytes to image
    image = Image.open(io.BytesIO(decrypted_data))
    # Save decrypted image to a file
    image.save(output_path)

# Generate a random 256-bit AES key
key = get_random_bytes(32)

# Encrypt image
iv = encrypt_image('image.jpeg', key, 'encrypted_image.bin')

# Decrypt image
decrypt_image('encrypted_image.bin', key, iv, 'decrypted_image.jpeg')
