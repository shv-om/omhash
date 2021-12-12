"""
*** Om-Hash ***

A simple Hash Algorithm

This is just a simple and maybe not-so-secure Hash Algorithm implementation..

"""

class Omhash:
    """This Class will accept text a parameter and return a Hash of 168 bytes Length"""

    def __init__(self, text):
        self.text = text
        self.hash = ''
        self.IV = '0x61736264207e71656f6972706f6974706a2064732c612061736e736120617364666e617320662c2073663b6b7177207766206c776b65726d71773b726b6d717765746d3b7320636120736466776f65726c73662061732c646620617077726a776f6520722c647a206620736164666b6e6120732c646620617364666d61736466'
        self.text_stream = ['0x'+self.__stream(text[i:i+64]) for i in range(0, len(text), 64)]

    def __stream(self, text):
        if len(text) > 0:
            return self.__stream(text[:-1]) + hex(ord(text[-1])).lstrip('0x')
        else:
            return ''

    def op1(self, hexnum1, hexnum2):
        if str(hexnum1).startswith('0x'):
            pass
        else:
            hexnum1 = '0x' + str(hexnum1)

        self.hash = int(hexnum1, 16) ^ int(hexnum2, 16)
        if self.hash % int(hexnum2, 16) != 0:
            self.hash += (self.hash // int(hexnum2, 16))
            self.hash = self.hash >> 1
        else:
            self.hash = self.hash << 1
        return self.hash

    def operation(self, text_stream):

        if len(text_stream) > 1:
            #print(self.op1(self.operation(text_stream[1:]), text_stream[0]))
            op1 = self.op1(self.operation(text_stream[1:]), text_stream[0])
            return op1
        else:
            return self.op1(self.IV, text_stream[0])


if __name__ == '__main__':

    text = input("Enter your text: ")
    omhash = Omhash(text)
    hash = hex(omhash.operation(omhash.text_stream)).upper()[16:184]
    print("Hash -->", hash)
    print(len(hash))
