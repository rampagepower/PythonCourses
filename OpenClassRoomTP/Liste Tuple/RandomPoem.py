import random

"""
write a programe which gives a random poem
"""


def write_random_poem(bundle_words):

    
    nous = bundle_words[0]
    verb = bundle_words[1]
    adj = bundle_words[2]
    adv = bundle_words[3]

    for x in range(8):
        print("\t"*x if x < 4 else "\t"*(8 -x),nous[random.sample(range(7), 1)[0]] + " " + verb[0] + " " + adj[0] + " " + adv[
            random.sample(range(7), 1)[0]])


def create_empty_list(n):
    lists = list()
    lists = ([] for i in range(n))
    return lists


def unduplicate_bundle_words(bundle_words):
    clean_bundle = list()

    for i in range(len(bundle_words)):
        clean_bundle.append(list(set(bundle_words[i])))

    return clean_bundle


# create a parser which give Noun Verb Adjectif Adverb, Objectif
def create_bundle_words(string):
    phrases = string.split('.')
    bundle_words = list()
    nous, verb, adj, obj = create_empty_list(4)

    # Loop n times inside of phrases to create bundle of phrases
    for phrase in range(len(phrases) - 1):
        bundle_words.append(list(phrases[phrase].split(' ')))

    # Get nous,verb, adjectif, adverb, obj
    for word in range(len(bundle_words)):
        nous.append(bundle_words[word][0])
        verb.append(bundle_words[word][1])
        adj.append(bundle_words[word][2] + " " + bundle_words[word][3])
        obj.append(bundle_words[word][4])

    bundle_words = list()
    bundle_words.append((nous))
    bundle_words.append((verb))
    bundle_words.append((adj))
    bundle_words.append((obj))

    # Use set trick to clean up duplicated words
    clean_bundle_words = unduplicate_bundle_words(bundle_words)

    return clean_bundle_words


def main():
    string = "Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability is better than rapidity."
    bundle_words = create_bundle_words(string)
    write_random_poem(bundle_words)


if __name__ == "__main__":
    main()
