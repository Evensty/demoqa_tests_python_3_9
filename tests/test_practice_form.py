from demoqa_tests.model.data.user import test_user
from demoqa_tests.model.pages.practice_form import PracticePage


def test_practice_form():
    practice_form = PracticePage(test_user)
    practice_form.fill_form()
    practice_form.check_results()
