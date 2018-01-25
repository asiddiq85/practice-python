# given 2 strings, check if they are anagram of each other
# an anagram is when 2 strings can be written using the exact same letters; so the letters can be rearranged to get a
# different phrase or word


def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False
    word_count = {}
    for letter in str2:
        if letter in word_count:
            word_count[letter] += 1
        else:
            word_count[letter] = 1

    for letter in str1:
        if letter in word_count:
            word_count[letter] -= 1
        else:
            word_count[letter] = 1
    print(word_count)

    for key in word_count:
        if word_count[key] != 0:
            return False

    return True


# print(is_anagram("public relations", "crap built on lies"))
# print(is_anagram("dog", "o dg"))
# print(is_anagram("dag", "o dg"))


# array pair sum; given an array of numbers and a number n, find a pair of distinct numbers
#  that add up to the given number n.

def pair_sum(numbers, number):
    # edge case
    if len(numbers) < 2:
        return

    # seen = set()
    # output = set()
    # for num in numbers:
    #     target = number - num
    #     if target not in seen:
    #         seen.add(target)
    #     else:
    #         output.add((num))
    # # print(seen)
    # # print(output)
    # print("\n".join(map(str, list(output))))
    # return output




