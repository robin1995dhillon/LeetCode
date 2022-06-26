#Time=O(N*M*log(M))
#Space = O(N)

def findHash(s):
    return str(sorted(s))


def groupAnagrams(strs):
    answers = []
    map_val = {}
    for s in strs:
        hashed = findHash(s)
        if(hashed not in map_val):
            map_val[hashed] = []
        map_val[hashed].append(s)

    for p in map_val.values():
        answers.append(p)

    return answers



strs = ["eat","tea","tan","ate","nat","bat"]
value = groupAnagrams(strs)
print(value)