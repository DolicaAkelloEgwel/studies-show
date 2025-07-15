import os

import constants


class ArticleInfo:
    def __init__(self):
        self.date = "June 10th 1991"
        self.volume = "3"
        self.issue = "12"
        self.paper_name = "Whatever Times:"
        self.price = "99p"
        self.title = "Stone Henge Mysteries Revealed!"
        self.author = "Firstname Lastname"
        self.content = (
            "In a groundbreaking development that has sent shockwaves through"
            " the archaeological community, researchers from the prestigious"
            " University of Oxford have unveiled what they claim is the final"
            " puzzle of Stonehenge. The ancient site, which has puzzled"
            " experts for centuries, was believed to be a place of ritual or"
            " ceremonial significance. However, according to the latest"
            " findings, Stonehenge might not just be about religion. The team,"
            " led by Dr. Emily Carter, a world-renowned archaeologist and"
            " professor at Oxford, revealed that Stonehenge could also serve"
            " as a sophisticated system for tracking celestial events. 'This"
            " is a game-changer,' said Dr. Carter in a press conference."
            " 'Stonehenge was not just about the dead; it was also about the"
            " living.' The researchers used advanced laser scanning technology"
            " to map the layout of the stones and identified patterns that"
            " suggested a complex mathematical framework underlying the"
            " structure. They also discovered ancient carvings that appear to"
            " depict constellations, further supporting their theory. These"
            " findings have led them to conclude that Stonehenge was not"
            " merely a burial ground but also an observatory used by ancient"
            " astronomers. 'The precision of the alignment is unparalleled,'"
            " added Dr. Carter. 'These stones were meticulously arranged to"
            " follow a specific mathematical sequence.' The study has been"
            " praised by leading astrophysicists, including Professor Harold"
            " Kimball from the University of Cambridge, who commented that the"
            " findings could rewrite the history of human knowledge. 'This"
            " discovery challenges everything we thought we knew about"
            " Stonehenge,' said Professor Kimball. 'If this is correct, then"
            " our understanding of ancient civilizations will be redefined.'"
            " The research has been published in the prestigious journal"
            " 'Antiquity', and the team is now seeking funding to create a"
            " full-scale model of the alleged observatory system. There's also"
            " talk of a major exhibition at the British Museum showcasing"
            " artifacts related to Stonehenge. In response, tourism officials"
            " have expressed concern about the potential impact on visitor"
            " numbers, as the new interpretation could change how people view"
            " the site. 'This is a once-in-a-lifetime opportunity for"
            " tourists,' said Mr. James Weatherby, head of tourism for the"
            " South West region. 'We need to prepare for an influx of visitors"
            " eager to learn more about Stonehenge's multifaceted history.'"
            " The discovery has sparked heated debates in academic circles,"
            " with some critics arguing that the evidence is not sufficient to"
            " support the new theory. However, Dr. Carter remains confident"
            " that their research is solid and that further discoveries will"
            " only strengthen their case. 'We are at the tip of the iceberg,'"
            " she said. 'There's so much more to uncover about this ancient"
            " wonder.' The team has already started working on expanding their"
            " findings into a full-length book, which they hope will be"
            " published next year. In the meantime, enthusiasts can follow"
            " updates on their website and social media channels for exclusive"
            " content and behind-the-scenes access. Stonehenge, once a"
            " mysterious enigma, is now at the center of a new scientific"
            " revolution."
        )


def write_document(article: ArticleInfo):
    with open("output.tex", "w") as outfile:

        # start by putting the top stuff in the file
        with open(
            os.path.join(constants.ASSETS_PATH, "document-01"), "r"
        ) as doc:
            outfile.write(doc.read())
        outfile.write("\n")

        outfile.write("\\date{" + article.date + "}\n")
        outfile.write("\\currentvolume{" + article.volume + "}\n")
        outfile.write("\\currentissue{" + article.issue + "}\n")
        outfile.write("\\SetPaperName{" + article.paper_name + "}\n")
        outfile.write("\\SetPaperPrice{" + article.price + "}\n")

        # start by putting the top stuff in the file
        with open(
            os.path.join(constants.ASSETS_PATH, "document-02"), "r"
        ) as doc:
            outfile.write(doc.read())
        outfile.write("\n")

        outfile.write(
            "\\byline{" + article.title + "}{" + article.author + "}\n"
        )
        outfile.write(article.content)
        outfile.write("\\closearticle\n")

        # start by putting the top stuff in the file
        with open(
            os.path.join(constants.ASSETS_PATH, "document-03"), "r"
        ) as doc:
            outfile.write(doc.read())


write_document(ArticleInfo())
