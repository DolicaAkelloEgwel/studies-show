import datetime
import shutil
import time

from create_image import create_image
from create_story import create_story
from printer_wrapper import print_document
from write_document import write_document


class Searcher:
    def __init__(self, manager):
        """An object for generating articles."""
        self._search_in_progress = manager.Value("b", False)
        self._begun_printing = manager.Value("b", False)
        self._finished_search = manager.Value("b", False)
        self._search_failed = manager.Value("b", False)

    def search(
        self,
        summary: str,
        year: str,
        generate_image: bool = True,
        print: bool = True,
    ):
        """Generates article text + image + caption, creates a document, then
           prints it.

        Args:
            summary (str): The article summary provided by the user.
            year (str): The year of the article.
            create_image (bool, optional): Whether or not to create an image.
            Defaults to True.
            print (bool, optional): Whether or not to print the document
            Defaults to True.
        """
        article, image_prompt = create_story(summary, year)
        if generate_image:
            img = create_image(image_prompt)
            img.save("output.jpg")
        latex_success = write_document(article)

        if latex_success == 0:
            self._begun_printing.value, self._search_in_progress.value = (
                self._search_in_progress.value,
                self._begun_printing.value,
            )
            if print:
                print_document()
            current_time = (
                str(datetime.datetime.now())
                .replace(" ", "-")
                .replace(":", "")
                .replace(".", "")
            )[:15]
            shutil.copyfile("output.pdf", f"exhibition/{current_time}.pdf")
            time.sleep(10)
            self._begun_printing.value, self._finished_search.value = (
                self._finished_search.value,
                self._begun_printing.value,
            )
            time.sleep(10)
            self._finished_search.value = False
        else:
            # may want to store the bad latex here...
            self._search_failed.value, self._search_in_progress.value = (
                self._search_in_progress.value,
                self._search_failed.value,
            )
            time.sleep(3)
            self._search_failed.value = False

    @property
    def search_in_progress(self):
        return self._search_in_progress.value

    @search_in_progress.setter
    def search_in_progress(self, val: bool):
        self._search_in_progress.value = val

    @property
    def begun_printing(self):
        return self._begun_printing.value

    @property
    def finished_search(self):
        return self._finished_search.value

    @property
    def search_failed(self):
        return self._search_failed.value

    @property
    def busy(self):
        return (
            self.search_in_progress
            or self.begun_printing
            or self.finished_search
            or self.search_failed
        )
