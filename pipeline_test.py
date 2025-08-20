from create_image import create_image
from create_story import create_story

title = "Mathematicians make shocking discovery. 1 + 1 is now 3!"

article, image_prompt = create_story(title)
img = create_image(image_prompt)
img.save("output.jpg")