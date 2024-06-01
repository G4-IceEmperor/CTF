import base64
import sys

def decode_file(input_file, iterations, output_file='output.txt'):
    with open(input_file, 'rb') as f:
        encoded_content = f.read()

    decoded_content = encoded_content
    for _ in range(iterations):
        decoded_content = base64.b64decode(decoded_content)

    with open(output_file, 'wb') as f:
        f.write(decoded_content)
    
    print("Written to file: output.txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py input_file")
        sys.exit(1)

    input_file = sys.argv[1]

    # Taking user input for iterations
    iterations = int(input("Enter number of iterations: "))

    decode_file(input_file, iterations)
