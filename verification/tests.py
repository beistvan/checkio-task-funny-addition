"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [3, 2],
            "answer": 5,
        },
        {
            "input": [5, 7],
            "answer": 12,
        },
        {
            "input": [5, 5],
            "answer": 0,
        },

    ],
    "Extra": [
        {
            "input": [6, 3],
            "answer": 9,
        },
        {
            "input": [6, 7],
            "answer": 13,
        },
        {
            "input": [10, 7],
            "answer": 17,
        },

    ]
}
