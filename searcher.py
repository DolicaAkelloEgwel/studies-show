import time

from create_image import create_image
from create_story import create_story
from printer_wrapper import print_document
from write_document import write_document


class Searcher:
    def __init__(self):
        """An object for generating articles."""
        self._search_in_progress = False
        self._begun_printing = False
        self._finished_search = False

    def search(
        self,
        summary: str,
        year: str,
        generate_image: bool = True,
        print: bool = True,
    ):
        """Generates article text + image + caption, creates a document, then prints it.

        Args:
            summary (str): The article summary provided by the user.
            year (str): The year of the article.
            create_image (bool, optional): Whether or not to create an image. Defaults to True.
            print (bool, optional): Whether or not to print the document. Defaults to True.
        """
        self._search_in_progress = True
        article, image_prompt = create_story(summary, year)
        if generate_image:
            img = create_image(image_prompt)
            img.save("output.jpg")
        write_document(article)
        self._begun_printing, self._search_in_progress = (
            self._search_in_progress,
            self._begun_printing,
        )
        if print:
            print_document()
        time.sleep(10)
        self._begun_printing, self._finished_search = (
            self._finished_search,
            self._begun_printing,
        )
        time.sleep(10)
        self._finished_search = False

    @property
    def search_in_progress(self):
        return self._search_in_progress

    @property
    def begun_printing(self):
        return self._begun_printing

    @property
    def finished_search(self):
        return self._finished_search

    @property
    def busy(self):
        return (
            self._search_in_progress
            or self._begun_printing
            or self._finished_search
        )
