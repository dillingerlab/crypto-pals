from base64 import b64encode, b64decode

def main():
    """Description of the function"""
    hex_in = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    base64_out = b64encode(bytes.fromhex(hex_in)).decode()
    print(base64_out)

if __name__=="__main__":
    main()

