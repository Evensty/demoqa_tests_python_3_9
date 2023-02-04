from selene.support.shared import browser
from demoqa_tests.utils import resources


class Uploader:
    def attach(self, selector, /, *, file):
        path = resources.path_to_dir(file)
        browser.element(selector).send_keys(path)


