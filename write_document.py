import os
from random import choice, randint

import constants

SLOGANS = [
    "For when your pineal gland gets murky.",
    "Telling the news before it happens!",
    "Keeping your finger on the pulse.",
]


def write_document(article) -> int:
    fname = "output.tex"
    with open(fname, "w") as outfile:

        # start by putting the top stuff in the file
        with open(
            os.path.join(constants.ASSETS_PATH, "document-01"), "r"
        ) as doc:
            outfile.write(doc.read())
        outfile.write("\n")

        # article info/args
        outfile.write("\\date{" + article.article_date + "}\n")
        outfile.write("\\currentvolume{" + str(randint(100, 500)) + "}\n")
        outfile.write("\\currentissue{" + str(randint(1, 20)) + "}\n")
        outfile.write("\\SetPaperName{" + "Recollector Times:" + "}\n")
        outfile.write("\\SetPaperLocation{" + "London" + "}\n")
        outfile.write("\\SetPaperSlogan{``" + choice(SLOGANS) + "''}\n")
        outfile.write("\\SetPaperName{" + "Recollector Times:" + "}\n")
        outfile.write("\\SetPaperPrice{" + "£3.99" + "}\n")

        # start by putting the top stuff in the file
        with open(
            os.path.join(constants.ASSETS_PATH, "document-02"), "r"
        ) as doc:
            outfile.write(doc.read())
        outfile.write("\n")

        # write a byline
        outfile.write(
            "\\byline{"
            + article.article_title
            + "}{"
            + article.article_author
            + "}\n"
        )

        # put our stable diffusion image at the top of the article
        outfile.write(
            "\\begin{window}[2,r,\\includegraphics[width=2.2in]{./output.jpg}"
            + ",{\\centering "
            + article.short_image_caption
            + "\\par}]\n"
        )
        outfile.write("\\end{window}")

        # write out the actual article
        outfile.write(article.article_content)

        # put in the remaining stuff
        with open(
            os.path.join(constants.ASSETS_PATH, "document-03"), "r"
        ) as doc:
            outfile.write(doc.read())

    return os.system("pdflatex -halt-on-error output.tex")
