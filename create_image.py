import gc

try:
    import torch
    from diffusers import DiffusionPipeline
except ModuleNotFoundError:
    pass


IMAGE_MODEL = "segmind/tiny-sd"


def create_image(prompt: str):
    pipe = DiffusionPipeline.from_pretrained(
        IMAGE_MODEL, torch_dtype=torch.float16
    )
    pipe = pipe.to("cuda")
    image = pipe(prompt).images[0]

    torch.cuda.empty_cache()
    gc.collect()

    return image
