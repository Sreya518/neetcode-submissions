from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Brute-Force Solution
        #TC - O(N^2 * k log k) where k = lenght of each string
        #SC - O(N * K) for results where N is total no.of words and k is length of each string. For sorted(group) no need to store as it don't add up
        # result = []
        # for word in strs:
        #     placed = False
        #     for group in result:
        #         if sorted(word) == sorted(group[0]):
        #             group.append(word)
        #             placed = True
        #             break
        #     if not placed:
        #         result.append([word])
        # return result  

        #Better Solution
        #TC - O(N * k log k)
        #SC - O(N * K)
        # anagram_map = defaultdict(list) 
        # for word in strs:
        #     key = ''.join(sorted(word))
        #     anagram_map[key].append(word)
        # return list(anagram_map.values())

        #Optimal Soution
        #TC - O(N * k)
        #SC - O(N * K)
        anagram_map = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count) #can't use list as a key. so converting it into tuple
            anagram_map[key].append(word)
        return list(anagram_map.values())

