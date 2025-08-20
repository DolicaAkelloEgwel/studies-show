import torch
from diffusers import DiffusionPipeline

IMAGE_MODEL = "segmind/tiny-sd"
pipe = DiffusionPipeline.from_pretrained(IMAGE_MODEL, torch_dtype=torch.float16)

def draw_image(prompt: str):
    pipe = pipe.to("cuda")
    image = pipe(prompt).images[0]
    return image

