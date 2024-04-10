import base64


def decrypt_pass(encrypted_pass):
    decoded_bytes = base64.b64decode(encrypted_pass)
    print(decoded_bytes)


to_decode = input("Enter base 64: ")
decrypt_pass(to_decode)
