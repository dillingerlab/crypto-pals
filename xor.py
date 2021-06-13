def main():
    """Description of the function"""
    input1 = '1c0111001f010100061a024b53535009181c1c0111001f010100061a024b53535009181c'
    input2 = '686974207468652062756c6c277320657965'

    byte_input1 = bytes.fromhex(input1)
    byte_input2 = bytes.fromhex(input2)
    # print(byte_input1)
    # print(byte_input2)

    ## need to make iterable
    xor_output = bytes([first_byte ^ second_byte for first_byte, second_byte in zip(byte_input1, byte_input2)]).hex()
    #print(xor_output)


    temp_iter = zip(byte_input1, byte_input2)
    out_string = ''
    for x, y in temp_iter:
        print(x, y)
        print(x ^ y)
        print([x ^ y])
        print(type(x ^ y))
        print(type([x ^ y]))
        print(bytes([x ^ y]))
        print(bytes([x ^ y]).hex())

        out_string = out_string + bytes([x ^ y]).hex()
    print(out_string)


if __name__=="__main__":
    main()

