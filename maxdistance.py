class TrieNode:
    def __init__(self):
        self.ch = collections.defaultdict(TrieNode)
        self.end = False
        self.h = 0 # longest tail from this node
        
    def add(self, s):
        node, n = self, len(s)
        for i, b in enumerate(s):
            node = node.ch[b]
            node.h = max(node.h, n - i)
        node.end = True
        
    def dist(self, s):
        node, n, cand = self, len(s), []
        for i, b in enumerate(s):
            # word in A reaches end
            if node.end: cand.append(n - i)
            # find the first mismatch
            bb = '1' if b == '0' else '0'
            if bb in node.ch:
                cand.append(n - i + node.ch[bb].h)
            # go to next trie node
            if b in node.ch:
                node = node.ch[b]
                continue
            # nowhere to go, break
            cand.append(n - i + node.h - 1)
            break
        else:
            # word in B is substring of word in A
            cand.append(node.h - 1)
        return max(cand)

def maxDistance(A, B):
    if len(B) > len(A): A, B = B, A
    root = TrieNode()
    for a in A: root.add(a)
    return max(root.dist(b) for b in B)

from random import randint

def dist(a, b):
    ans = len(a) + len(b)
    for s, t in zip(a, b):
        if s == t: ans -= 2
        else: break
    return ans

trial = 10
for _ in range(trial):
    size_A, size_B = randint(1, 3), randint(1, 3)
    A = [bin(randint(0, 1<<6))[2:] for _ in range(size_A)]
    A = [a.zfill(len(a) + randint(0, 3)) for a in A]
    B = [bin(randint(0, 1<<6))[2:] for _ in range(size_B)]
    B = [b.zfill(len(b) + randint(0, 3)) for b in B]
    d1 = max(dist(a, b) for a in A for b in B)
    d2 = maxDistance(A, B)
    if trial <= 10 or d1 != d2:
        print(A, B)
        print(f'brute: {d1}, maxDistance: {d2}')
    
