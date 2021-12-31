import numpy as np

years = [i for i in range(1972, 2021)]


def read_speech(_year):
    return open("nytaarstaler/" + str(_year) + ".txt", encoding="utf-8").readlines()


def contains_word(_year, word):
    _speech = read_speech(_year)
    for line in _speech:
        if word in line:
            return True
    return False


def question_2_answer():
    # hvor mange gange siger hun gud
    count = 0
    for _year in years:
        if contains_word(_year, "Søens folk"):
            print("I " + str(_year))
            count += 1
    return count


def question_3_answer():
    # hvor mange ord i hver quiz
    for _year in years:
        count = 0
        _speech = read_speech(_year)
        for line in _speech:
            count += len(line.split())
        f = open("spg2/count_words.txt", "a", encoding="utf-8")
        f.write(str(_year) + ": " + str(count) + "\n")
        f.close()


def question_32_answer():
    # hvor mange ord gennemsnitligt
    year_count = 0
    word_count = 0
    for _year in years:
        year_count += 1
        _speech = read_speech(_year)
        for line in _speech:
            word_count += len(line.split())
    return np.divide(word_count, year_count)

def question_5_answer():
    word1 = "Gud"
    word2 = "gud"
    # hvor mange af ord gennemsnitligt
    year_count = 0
    word_count = 0
    for _year in years:
        year_count += 1
        _speech = read_speech(_year)
        for line in _speech:
            word_count += len(line.split())
    return np.divide(word_count, year_count)


if __name__ == '__main__':
    print(question_32_answer())