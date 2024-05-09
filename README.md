# PRODIGY_CS_02
# Image Encryption and Decryption with AES

This Python script demonstrates how to encrypt and decrypt images using AES (Advanced Encryption Standard) encryption. AES is a symmetric encryption algorithm commonly used for securing sensitive data.

## Prerequisites

- Python 3.x
- `pillow` library (`pip install pillow`)
- `pycryptodome` library (`pip install pycryptodome`)

## Usage

1. **Install Dependencies**: Make sure you have installed the necessary dependencies by running the following commands:
 -pip install pillow
   -pip install pycryptodome

2. **Run the Script**: Execute the Python script `encrypt_decrypt_image.py` with the appropriate command-line arguments: python encrypt_decrypt_image.py 
    Replace `encrypt_decrypt_image.py` with the name of the Python script containing the provided code.

3. **Provide Input Image**: When prompted, enter the path to the input image file that you want to encrypt and decrypt.

4. **View Output**: The script will generate two output files:
- `encrypted_image.bin`: The encrypted image file.
- `decrypted_image.jpeg`: The decrypted image file.

## Code Explanation

The provided Python script performs the following operations:

1. **Encryption**:
- Reads an input image file.
- Converts the image to bytes.
- Pads the byte data to match the block size required for AES encryption.
- Encrypts the padded data using AES in CBC (Cipher Block Chaining) mode.
- Saves the encrypted data to a file.

2. **Decryption**:
- Reads the encrypted data from the file.
- Decrypts the data using the provided AES key and initialization vector (IV).
- Unpads the decrypted data.
- Converts the decrypted byte data back to an image.
- Saves the decrypted image to a file.






