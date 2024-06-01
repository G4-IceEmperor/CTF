import base64
import sys

def decode_file(input_file, output_file='output.txt', iterations=50):
    with open(input_file, 'rb') as f:
        encoded_content = f.read()

    decoded_content = encoded_content
    for _ in range(iterations):
        decoded_content = base64.b64decode(decoded_content)

    with open(output_file, 'wb') as f:
        f.write(decoded_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file")
        sys.exit(1)

    input_file = sys.argv[1]

    decode_file(input_file)
