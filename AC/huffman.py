import heapq
from collections import Counter, namedtuple

class HuffmanNode(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class HuffmanLeaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def huffman_coding(s):
    h = [(weight, HuffmanLeaf(char)) for char, weight in Counter(s).items()]
    heapq.heapify(h)

    while len(h) > 1:
        lo = heapq.heappop(h)
        hi = heapq.heappop(h)
        node = HuffmanNode(lo, hi)
        heapq.heappush(h, (lo[0] + hi[0], node))

    code = {}
    if h:
        [(_weight, root)] = h
        root.walk(code, "")

    return code

# Example usage:
data = "huffman coding is fun"
huffman_codes = huffman_coding(data)

# Print Huffman codes
for char, code in huffman_codes.items():
    print(f"{char}: {code}")
