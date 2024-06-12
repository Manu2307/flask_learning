import json
import os
from datetime import datetime
from tut1.sample import add, validate_age, save_dict, find_senior, is_eligible_for_degree, guess_number, get_ip, random_sum, silly
import pytest
import sys
from unittest import mock
from unittest.mock import call


class TestSample:
    def test_add_num(self):
        assert add(2, 3) == 5

    def test_add_str(self):
        assert add("MA", "NOJ") == "MANOJ"

    def test_validate_age_valid_age(self):
        validate_age(10)

    def test_validate_age_invalid_age(self):
        with pytest.raises(ValueError, match="Age cannot be less than zero"):
            validate_age(-1)

    @pytest.mark.skip(reason="Just wanna skip it normally")
    def test_sample_3(self):
        assert add(1, 2) == 3

    @pytest.mark.skipif(sys.version_info > (3, 10), reason="Use python 3.7 or less")
    def test_sample_4(self):
        assert add("RA", "HUL") == "RAHUL"

    @pytest.mark.xfail(sys.platform == 'linux', reason="Don't run on linux")
    def test_sample_5(self):
        assert add("HE", "MA") == "HEMA"
        raise Exception()

    @pytest.mark.parametrize("a, b, c", [(1, 2, 3), ("MA", "NOJ", "MANOJ"), ([1, 2], [3], [1, 2, 3])],
                             ids=["nums", "str", "list"])
    def test_add_using_parameters(self, a, b, c):
        assert add(a, b) == c

    # built-in fixtures example
    def test_save_dict(self, tmpdir, capsys):
        filepath = os.path.join(tmpdir, "test.json")
        _dict = {"a": 1, "b": 2}
        save_dict(_dict, filepath)
        assert json.load(open(filepath, 'r')) == _dict
        assert capsys.readouterr().out == "saved\n"


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_add_credits(dummy_student):
    dummy_student.add_credits(5)
    assert dummy_student.get_credits() == 5


def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 0


def test_find_senior(make_dummy_engineer):
    engineers = [
        make_dummy_engineer("Manoj", 2),
        make_dummy_engineer("Rahul", 6),
        make_dummy_engineer("Hema", 4)
    ]

    topper = find_senior(engineers)

    assert topper == engineers[1]


@pytest.mark.parametrize("dummy_student, expected", [(19, False), (21, True)],
                         indirect=["dummy_student"], ids=["ineligible", "eligible"])
def test_student_is_eligible_for_degree(dummy_student, expected):
    assert is_eligible_for_degree(dummy_student) is expected


@pytest.mark.parametrize("_input, expected", [(3, "You won!"), (4, "You lost!")])
@mock.patch("tut1.sample.roll_dice")
def test_guess_number(mock_roll_dice, _input, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once()


@mock.patch("tut1.sample.requests.get")
def test_get_ip(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="Response mock",
                                               **{"status_code": 200,
                                                  "json.return_value": {"origin": "0.0.0.0"}})
    assert get_ip() == '0.0.0.0'
    mock_requests_get.assert_called_once_with("https://httpbin.org/ip")


@mock.patch("tut1.sample.random.randint")
def test_random_sum(mock_randint):
    mock_randint.side_effect = [3, 4]
    assert random_sum() == 7
    mock_randint.assert_has_calls(calls=[call(1, 10), call(1, 7)])


@mock.patch("tut1.sample.random.randint")
@mock.patch("tut1.sample.time.time")
@mock.patch("tut1.sample.requests.get")
def test_silly(mock_requests_get, mock_time, mock_randint):
    test_params = {
        "timestamp": 123,
        "number": 5
    }
    mock_time.return_value = test_params['timestamp']
    mock_randint.return_value = 5
    mock_requests_get.return_value = mock.Mock(**{"status_code": 200, "json.return_value": {"args": test_params}})

    assert silly() == test_params
    