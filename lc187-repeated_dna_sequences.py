"""
lc187-repeated_dna_sequences.py:
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". 
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

class Solution:
    def findRepeatedDnaSequences(self, s):
        repeated_dna_seq = []
        dna_size = len(s)
        beg_i, end_i = 0, 10
        dict_dna_seq = {}
        while end_i <= dna_size:
            dna_seg = s[beg_i : end_i]
            dna_seq_cnt = dict_dna_seq.get(dna_seg)
            if dna_seq_cnt:
                if dna_seq_cnt == 1:
                    repeated_dna_seq.append(dna_seg)
                    dict_dna_seq[dna_seg] = 2
            else:
                dict_dna_seq[dna_seg] = 1
            beg_i += 1
            end_i += 1
        return repeated_dna_seq
            

def main():
    test_str = "AAAAAAAAAAA"
    sln = Solution()
    dna_list = sln.findRepeatedDnaSequences(test_str)
    print("Testing DNA Sequence:", test_str)
    print("Repeated Sequences Found:")
    for dna_seq in dna_list: print(dna_seq)

if __name__ == "__main__":
    main()