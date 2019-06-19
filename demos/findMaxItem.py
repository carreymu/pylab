from collections import Counter
import heapq
if __name__ == "__main__":
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    topn = 3
    word_counts = Counter(words)
    print("word_counts is ",word_counts)
    top_three = word_counts.most_common(topn)
    print("top_three is ", top_three)

    word_counts.update(morewords)

    print("========================")
    print("Count(words + morewords) is ", Counter(words + morewords))
    print("Counter(words) + Counter(morewords) is ", Counter(words) + Counter(morewords))
    print("Counter(words)- Counter(morewords) is ", Counter(words)- Counter(morewords))

    for it in word_counts:
        print("%s count is %d" % (it,word_counts[it]))


    print("========================")
    lmb = [(x,words.count(x)) for x in words]
    print("lmb is ", lmb)
    heap = [(value, key) for key, value in dict(lmb).items()]
    print("heap is ", heap)
    largest = heapq.nlargest(topn, heap)
    print("largest tuple is %s, key is %s" % (largest,largest[0][1]))

    print("largest is ", [(value, key) for key, value in largest])
