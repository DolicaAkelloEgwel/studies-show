from create_image import create_image
from create_story import create_story
from printer_wrapper import print_document
from write_document import write_document


class Searcher:
    def __init__(self):
        self._search_in_progress = False
        self._begun_printing = False

    def search(
        self,
        title: str,
        year: str,
        create_image: bool = True,
        print: bool = True,
    ):
        self._search_in_progress = True
        article, image_prompt = create_story(title, year)
        if create_image:
            img = create_image(image_prompt)
            img.save("output.jpg")
        write_document(article)
        self._begun_printing, self._search_in_progress = (
            self._search_in_progress,
            self._begun_printing,
        )
        if print:
            print_document()

    @property
    def search_in_progress(self):
        return self._search_in_progress

    @property
    def begun_printing(self):
        return self._begun_printing
