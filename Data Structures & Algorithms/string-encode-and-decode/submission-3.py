class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_strs = ""

        for s in strs:
            s_len = len(s)
            encoded_strs += str(s_len)
            encoded_strs += "#"
            encoded_strs += s 
            

        print(encoded_strs)

        return encoded_strs

    def decode(self, s: str) -> List[str]:

        decoded_str = []
        curr_word = ""
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word_start = j+1
            word_end = word_start + length
            word = s[word_start : word_end]
            decoded_str.append(word)
            i = word_end
            

        return decoded_str