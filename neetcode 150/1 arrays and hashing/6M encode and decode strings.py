class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded = []
        for s in strs:
            encode_str = f"{len(s)}#{s}"
            encoded.append(encode_str)
        return ''.join(encoded)

    def decode(self, s):
        decoded = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[j-1])
            decoded.append(s[j+1:j+1 + length])
            i = j+ 1 + length + 1
        return decoded




class Delimiter:
    def encode(self, strs) -> str:
        return '#'.join(s for s in strs)

    def decode(self, s: str) :
        strs = s.split('#')
        result = []
        for s in strs:
            result.append(s)
        return result

if __name__=="__main__":
    print("________Length + Delimiter")
    input = ["lint","code","love","you"]
    encode = Solution().encode(input)
    print(Solution().decode(encode))



    print("________Delimiter")
    input1 = ["hello", "world"]
    encode1 = Delimiter().encode(input1)
    print(input1)
    print(encode1)
    print(Delimiter().decode(encode1))

        # class Codec:
        #     def encode(self, strs: List[str]) -> str:
        #         """Encodes a list of strings to a single string."""
        #         encoded = []
        #         for s in strs:
        #             encoded.append(f"{len(s)}#{s}")  # Prefix the length and add a delimiter
        #         return ''.join(encoded)
        #
        #     def decode(self, s: str) -> List[str]:
        #         """Decodes a single string to a list of strings."""
        #         decoded = []
        #         i = 0
        #         while i < len(s):
        #             # Find the next delimiter to extract the length
        #             j = s.find('#', i)
        #             length = int(s[i:j])  # Length is the number before '#'
        #             i = j + 1
        #             # Extract the string of that length
        #             decoded.append(s[i:i + length])
        #             i += length
        #         return decoded