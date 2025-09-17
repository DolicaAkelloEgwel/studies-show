from create_image import create_image
from create_story import create_story
from printer_wrapper import print_document
from write_document import write_document


class Searcher:
    def __init__(self):
        self._search_in_progress = False

    def search(
        title: str, year: str, create_image: bool = True, print: bool = True
    ):
        self._search_in_progress = True
        article, image_prompt = create_story(title, year)
        if create_image:
            img = create_image(image_prompt)
            img.save("output.jpg")
        write_document(article)
        if print:
            print_document()
        self._search_in_progress = False

    @property
    def search_in_progress(self):
        return self._search_in_progress
