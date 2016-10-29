class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words('words.txt')
        

    def decrypt_message(self):
            '''
            Decrypt self.message_text by trying every possible shift value
            and find the "best" one. We will define "best" as the shift that
            creates the maximum number of real words when we use apply_shift(shift)
            on the message text. If s is the original shift value used to encrypt
            the message, then we would expect 26 - s to be the best shift value 
            for decrypting it.

            Note: if multiple shifts are  equally good such that they all create 
            the maximum number of you may choose any of those shifts (and their
            corresponding decrypted messages) to return

            Returns: a tuple of the best shift value used to decrypt the message
            and the decrypted message text using that shift value
            '''
            valid_words_counter = 0
            max_valid_words = 0
            shift = 0
            for i in range(0, 26):
                words = self.message_text.split(' ')
                words = Message.apply_shift(self, i)
                for each in words.split():
                    if is_word(self.valid_words, each):
                        valid_words_counter += 1
                if (valid_words_counter > max_valid_words):
                    finalshift = (i, words)
                    max_valid_words = valid_words_counter
                else:
                    valid_words_counter = 0
            return finalshift


#PS5.4

def decrypt_story():
    ctm = CiphertextMessage(get_story_string())
    return (ctm.decrypt_message())

                    

                
            
