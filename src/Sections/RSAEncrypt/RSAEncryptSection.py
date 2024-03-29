from RSA.RSA import RSA
from Sections.RSAEncrypt.Prompts.RSAEncryptPrompt import RSAEncryptPrompt

class RSAEncryptSection():
    def start(self):
        self.rsa = RSA()
        self.prompts = RSAEncryptPrompt()

        self.showPrompts()
        self.encrypt()

    def showPrompts(self):
        self.prompts.show()

        # get data
        self.n = int(self.prompts.getAnswer('n'))
        self.e = int(self.prompts.getAnswer('e'))
        self.source = int(self.prompts.getAnswer('source'))
        self.outputType = self.prompts.getAnswer('outputType')

        # read from keyboard
        if self.source == 1:
            self.content = self.prompts.showContentPrompt()

        # read from file
        if self.source == 2:
            path = self.prompts.showInputPathPrompt()
            with open(path) as fileContent:
                self.content = fileContent.read()

        # get output file path
        if self.outputType == 1:
            self.outputPath = self.prompts.showOutputPathPrompt()

    def encrypt(self):
        # generate encrypted content
        encrypted = []

        for char in self.content:
            encrypted.append(str(self.rsa.encrypt(self.n, self.e, ord(char))))

        # generate output
        output = ' '.join(encrypted)
        if self.outputType == 1:
            f = open(self.outputPath, 'w')
            f.write(output)

        # print result
        print()
        print('Encrypted content:')
        print()
        print(output)
