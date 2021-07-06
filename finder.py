def main():
    """Description of the function"""

    hex_cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    cipher = bytes.fromhex(hex_cipher)
    potential_answers = []

    for value in range(256):
        output_bytes = b''
        for byte in cipher:
            output_bytes += bytes([byte ^ value])

            ## Reference for scoring: https://en.wikipedia.org/wiki/Letter_frequency
            character_frequencies = {'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
                                     'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
                                     'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
                                     'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
                                     'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
                                     'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
                                     'y': .01974, 'z': .00074, ' ': .13000}

            rating = sum([character_frequencies.get(chr(byte), 0) for byte in output_bytes.lower()])

            sort = {'message': output_bytes,
                    'score': rating}

            potential_answers.append(sort)

    print((sorted(potential_answers, key=lambda x: x['score'], reverse=True)[0]['message']).decode("utf-8"))


if __name__=="__main__":
    main()

