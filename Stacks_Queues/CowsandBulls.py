from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cows = 0
        bulls = 0

        s_counter = Counter()
        g_counter = Counter()

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                s_counter[secret[i]] += 1
                g_counter[guess[i]] += 1
        
        for char in g_counter:
            cows += min(g_counter[char], s_counter[char])

        return str(bulls) + "A" + str(cows) + "B"

