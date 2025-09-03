import os
import subprocess

import constants


def write_document(article):
    fname = "output.tex"
    with open(fname, "w") as outfile:

        # start by putting the top stuff in the file
        with open(
            os.path.join(constants.ASSETS_PATH, "document-01"), "r"
        ) as doc:
            outfile.write(doc.read())
        outfile.write("\n")

        outfile.write("\\date{" + article.article_date + "}\n")
        outfile.write("\\currentvolume{" + "12" + "}\n")
        outfile.write("\\currentissue{" + "3" + "}\n")
        outfile.write("\\SetPaperName{" + "Recollector Times:" + "}\n")
        outfile.write("\\SetPaperLocation{" + "London" + "}\n")
        outfile.write("\\SetPaperName{" + "Recollector Times:" + "}\n")
        outfile.write("\\SetPaperPrice{" + "£3.99" + "}\n")

        # start by putting the top stuff in the file
        with open(
            os.path.join(constants.ASSETS_PATH, "document-02"), "r"
        ) as doc:
            outfile.write(doc.read())
        outfile.write("\n")

        outfile.write(
            "\\byline{"
            + article.article_title
            + "}{"
            + article.article_author
            + "}\n"
        )
        outfile.write(
            "\\begin{window}[2,r,\\includegraphics[width=2.2in]{./output.jpg}"
            + ",\\centerline{"
            + article.image_caption
            + "}]\n"
        )
        outfile.write("\\end{window}")
        outfile.write(article.article_content)

        # start by putting the top stuff in the file
        with open(
            os.path.join(constants.ASSETS_PATH, "document-03"), "r"
        ) as doc:
            outfile.write(doc.read())

    os.system("pdflatex output.tex")
