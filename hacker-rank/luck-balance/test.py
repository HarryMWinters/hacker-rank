import unittest
from solution import luckBalance as func

# If the test_data were to continue to grow it'd make sense to move it into it's own file.
test_data = [
    # {
    #     "input": {
    #         "max_loss": 3,
    #         "contest_array": [
    #             # [luck, importance]
    #             [5, 1],
    #             [2, 1],
    #             [1, 1],
    #             [8, 1],
    #             [10, 0],
    #             [5, 0],
    #         ]
    #     },
    #     "solution": 29
    # },
    # {
    #     "input": {
    #         "max_loss": 2,
    #         "contest_array": [
    #             [5, 1],
    #             [4, 0],
    #             [6, 1],
    #             [2, 1],
    #             [8, 0],
    #         ]
    #     },
    #     "solution": 21
    # },
    # {
    #     "input": {
    #         "max_loss": 5,
    #         "contest_array": [
    #             [13, 1],
    #             [10, 1],
    #             [9, 1],
    #             [8, 1],
    #             [13, 1],
    #             [12, 1],
    #             [18, 1],
    #             [13, 1],
    #         ]
    #     },
    #     "solution": 42
    # },
    # {
    #     "input": {
    #         "max_loss": 0,
    #         "contest_array": [
    #             [13, 1],
    #             [10, 1],
    #             [9, 1],
    #             [8, 1],
    #             [13, 1],
    #             [12, 1],
    #             [18, 1],
    #             [13, 1],
    #         ]
    #     },
    #     "solution": -96
    # },
    # {
    #     "input": {
    #         "max_loss": 0,
    #         "contest_array": []
    #     },
    #     "solution": 0
    # },
    # {
    #     "input": {
    #         "max_loss": 10,
    #         "contest_array": []
    #     },
    #     "solution": 0
    # },
    # {
    #     "input": {
    #         "max_loss": 10,
    #         "contest_array": [
    #             [13, 0],
    #             [10, 0],
    #             [9, 0],
    #             [8, 0],
    #             [13, 0],
    #             [12, 0],
    #             [18, 0],
    #             [13, 0],
    #         ]
    #     },
    #     "solution": 96
    # },
    {
        "input": {
            "max_loss": 58,
            "contest_array": [
                [105, 0],
                [103, 0],
                [106, 1],
                [106, 1],
                [103, 0],
                [103, 1],
                [105, 1],
                [106, 1],
                [105, 0],
                [104, 0],
                [103, 0],
                [102, 0],
                [104, 0],
                [105, 0],
                [104, 0],
                [102, 1],
                [104, 0],
                [106, 1],
                [104, 1],
                [101, 1],
                [105, 0],
                [103, 0],
                [104, 0],
                [106, 0],
                [102, 1],
                [103, 0],
                [102, 0],
                [103, 1],
                [106, 0],
                [104, 1],
                [101, 1],
                [101, 1],
                [106, 0],
                [103, 1],
                [103, 0],
                [104, 1],
                [101, 0],
                [105, 1],
                [105, 0],
                [104, 1],
                [105, 0],
                [106, 0],
                [104, 0],
                [105, 0],
                [101, 1],
                [106, 1],
                [105, 0],
                [103, 0],
                [104, 1],
                [101, 1],
                [106, 1],
                [104, 0],
                [106, 1],
                [105, 0],
                [103, 1],
                [101, 0],
                [103, 0],
                [101, 0],
                [105, 1],
                [104, 1],
                [104, 1],
                [105, 1],
                [105, 1],
                [103, 0],
                [101, 0],
                [104, 1],
                [106, 1],
                [105, 1],
                [105, 0],
                [106, 1],
                [104, 1],
                [105, 1],
                [103, 1],
                [102, 1],
                [106, 0],
                [101, 0],
                [105, 1],
                [104, 1],
                [103, 1],
                [106, 1],
                [101, 0],
                [106, 1],
                [103, 0],
                [106, 1],
                [102, 1],
                [103, 0],
                [101, 1],
                [102, 1],
                [101, 1],
                [104, 0],
                [106, 0],
                [102, 0],
                [104, 0],
                [105, 0],
                [105, 0],
                [102, 1],
                [103, 1],
            ]
        },
        "solution": 10069
    },

]


class TestLuckBalance(unittest.TestCase):
    def test__func(self):
        for case in test_data:
            A, B = case["input"]["max_loss"], case["input"]["contest_array"]
            with self.subTest(f"\nA = {A}\n\tB = {B}"):
                self.assertEqual(
                    case["solution"],
                    func(A, B)
                )


if __name__ == '__main__':
    unittest.main()