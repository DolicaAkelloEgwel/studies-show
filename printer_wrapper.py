from subprocess import call

from constants import PRINTER_NAME


def print_document(filename: str):
    # using the lp -d command to use a printer that has 834 in the name...
    # sing while you may :)
    call(["lp", "-d", PRINTER_NAME, filename])
