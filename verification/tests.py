"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [7, 28, 4],
            "answer": 6,
        },
        {
            "input": [-77, 19, 10],
            "answer": 9,
            "explanation": "5+7=?"
        },
        {
            "input": [1, 10**12 - 1, 5],
            "answer": 199999999999,
        },
    ],
    "Extra": [
        {
            "input": [-19, -13, 10],
            "answer": 0,
        },
        {
            "input": [0, 10**12 - 1, 5],
            "answer": 200000000000,
        },
        {
            "input": [0, 10**12, 5],
            "answer": 200000000001,
        },
        {
            "input": [-10**12, 10**12, 12345],
            "answer": 162008911,
        },
        {
            "input": [-4, 0, 4],
            "answer": 2,
        },
    ]
}
