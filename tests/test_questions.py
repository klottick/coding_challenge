"""
Test cases for questions 1 - 5
"""
from coding_challenge.questions import *


def test_question_1():
    assert question_1("Checkpont is a cool place to work!") == "tnopkcehC si a looc ecalp ot krow!"
    assert question_1("I love the python programming language") == "I evol eht nohtyp gnimmargorp egaugnal"


def test_question_2():
    hash1 = {
        "data": {
            "cpu": [1, 1, 42, 20],
            "mem": [100, 100, 125, 90],
            "disk": {"read": [0, 40, 10, 4], "write": [224, 98, 70, 200], "swap": 0},
        },
        "foo": 11,
    }
    hash2 = {
        "data": {
            "cpu": [5, 6],
            "disk": {"read": [100], "write": [100, 110, 120, 130, 140], "swap": 1},
            "net": [20, 30, 40],
        },
        "foo": 0,
        "bar": 19,
    }

    assert question_2(hash1, hash2) == {
        "data": {
            "cpu": [1, 1, 42, 20, 5, 6],
            "mem": [100, 100, 125, 90],
            "disk": {"read": [0, 40, 10, 4, 100], "write": [224, 98, 70, 200, 100, 110, 120, 130, 140], "swap": 1},
            "net": [20, 30, 40],
        },
        "foo": 0,
        "bar": 19,
    }


def test_question_3():
    dup_array = [
        80,
        93,
        17,
        64,
        93,
        17,
        41,
        86,
        8,
        51,
        69,
        4,
        27,
        75,
        49,
        56,
        95,
        8,
        16,
        2,
        73,
        34,
        85,
        89,
        96,
        39,
        99,
        64,
        13,
        94,
        93,
        25,
        76,
        11,
        26,
        91,
        85,
        28,
        11,
        55,
        9,
        36,
        68,
        96,
        23,
        53,
        66,
        90,
        68,
        79,
        17,
        68,
        85,
        91,
        49,
        94,
        90,
        16,
        96,
        74,
        9,
        69,
        84,
        14,
        99,
        50,
        15,
        90,
        13,
        3,
        17,
        64,
        26,
        48,
        68,
        99,
        99,
        50,
        91,
        91,
        89,
        93,
        36,
        22,
        67,
        43,
        90,
        49,
        76,
        34,
        16,
        80,
        29,
        18,
        53,
        27,
        33,
        71,
        37,
        62,
    ]
    expected = sorted([93, 17, 8, 64, 85, 11, 96, 68, 91, 49, 94, 90, 16, 9, 69, 99, 13, 26, 50, 89, 36, 76, 34, 80, 53, 27])

    result = sorted(question_3(dup_array))
    assert result == expected


def test_question_4():
    cipher = "d, i, q, z, e, f, v, p, s, o, u, k, l, g, h, w, a, m, j, n, c, y, t, x, r, b".split(", ")
    phrase = "a, have, reward, end, sentence, proving, words, the, not, sorry, clever, sorted, the, that, you, are, this, lists, correctly, but, be, the, more, hard, was, should".split(
        ", "
    )

    assert (
        question_4(cipher, phrase)
        == "this should be a sentence proving that you have correctly sorted the lists but sorry the reward was not more clever words are hard the end"
    )


def test_question_5():
    assert sorted(question_5("cats")) == sorted([
        "cast",
        "cats",
        "ctsa",
        "ctas",
        "csat",
        "csta",
        "atsc",
        "atcs",
        "asct",
        "astc",
        "acts",
        "acst",
        "tsca",
        "tsac",
        "tcas",
        "tcsa",
        "tasc",
        "tacs",
        "scat",
        "scta",
        "satc",
        "sact",
        "stca",
        "stac",
    ])
