from create_image import create_image
from create_story import create_story
from printer_wrapper import print_document
from write_document import write_document

print("Enter a title:")
title = input()

article, image_prompt = create_story(title, "1991")
img = create_image(image_prompt)
img.save("output.jpg")

write_document(article)
# print_document()
