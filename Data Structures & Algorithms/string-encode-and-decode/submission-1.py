class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += s + "\0"
        return encoded_string;
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        word = []
        for c in s:
            if c != "\0":
                word.append(c)
            else:
                decoded_strs.append("".join(word))
                word = []
        return decoded_strs;
