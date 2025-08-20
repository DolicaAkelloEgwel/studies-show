from ollama import ChatResponse, chat
from pydantic import BaseModel

# will experiment with this...
prompt_models = [
    "trollek/qwen2-diffusion-prompter",
    "gnokit/improve-prompt:latest",
    "impactframes/llama3_ifai_sd_prompt_mkr_q4km:latest",
    "brxce/stable-diffusion-prompt-generator:latest",
]
IMAGE_PROMPT_MODEL = "trollek/qwen2-diffusion-prompter"
ARTICLE_GENERATION_MODEL = "deepseek-r1:7b"


class NewsArticle(BaseModel):
    news_source_name: str
    article_content: str
    article_image_description: str
    image_caption: str


def _create_story(article_title: str) -> ChatResponse:
    return chat(
        model=ARTICLE_GENERATION_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a news story generator. Given an article title,"
                    " you will create an extremely silly made up but"
                    " realistic-sounding 600+ word news story that continues"
                    " the theme of the article title. Throw in lots of"
                    " intimidating, clever words so that people think 'Well"
                    " this MUST be true and not fake at all because the person"
                    " who wrote this is obviously so smart.' If appropriate,"
                    " throw in weird statistics or mention universities at"
                    " which research was carried out and so on, or give the"
                    " credentials of the experts who were consulted. If"
                    " appropriate, mention statistics or results from polls."
                    " Make it sound very verbose and wordy. Please make it UK"
                    " centric."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Please create an article with the given title:"
                    f" {article_title}"
                ),
            },
        ],
        format=NewsArticle.model_json_schema(),
    )


def _stable_diffusion_prompt(image_description: str, prompt_model: str) -> str:
    return chat(
        model=prompt_model,
        messages=[
            # {
            #     "role": "system",
            #     "content": (
            #         "Given an image description, you will create a text-to-image prompt that can generate that image. Please ensure the image is photorealistic and suitable for a newspaper. Do not say anything related to digital art."
            #     ),
            # },
            {
                "role": "user",
                "content": (
                    f"{image_description}, photorealistic, 4K, detailed"
                ),
            },
        ],
    )


response: ChatResponse = _create_story(
    "Researchers crack the Stonehenge code!"
)

news_article = NewsArticle.model_validate_json(response.message.content)

print(news_article)

for model in prompt_models:
    image_prompt = _stable_diffusion_prompt(
        news_article.article_image_description, model
    ).message.content
    print("")
    print(model)
    print(image_prompt)
