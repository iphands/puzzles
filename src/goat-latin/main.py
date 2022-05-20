from ..common.utils import log, check


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        count = 1
        ret = []
        vowels = ['a', 'e', 'i', 'o', 'u']

        for word in sentence.split():
            char = word[0].lower()
            if char not in vowels:
                word = list(word)
                word.append(word.pop(0))
                word = ''.join(word)
            ret.append(word + 'ma' + ''.join(['a'] * count))
            count += 1

        log(ret)
        return ' '.join(ret)


###################################


def test(sentence, ans):
    log("\n\nTesting: sentence:{}".format(sentence))
    check(Solution().toGoatLatin(sentence), ans, sentence)


def do_all_tests():
    test("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")


if __name__ == '__main__':
    do_all_tests()
