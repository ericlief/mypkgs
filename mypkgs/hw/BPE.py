#Algorithm 1
#Learn BPE operations

import re, collections

def get_stats(vocab):
    pairs = collections.defaultdict(int)

    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i],symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, v_in):
    print('pair', pair)
    v_out = {}
    bigram = re.escape(' '.join(pair))
    print(bigram)
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        print('word', word)
        w_out = p.sub(''.join(pair), word)
        print('w ouit', w_out)
        v_out[w_out] = v_in[word]
        
    return v_out

vocab = {'l o w </w>' : 5, 'l o w e r </w>' : 2,
'n e w e s t </w>':6, 'w i d e s t </w>':3}
num_merges = 10

for i in range(num_merges):
    pairs = get_stats(vocab)
    print('pairs', pairs)
    best =max(pairs, key=pairs.get)
    print('best', best)
    vocab = merge_vocab(best, vocab)
    print(best)

    print(vocab)