from ollama import ChatResponse, chat
from pydantic import BaseModel

# will experiment with this...
IMAGE_PROMPT_MODEL = "brxce/stable-diffusion-prompt-generator:latest"


class NewsArticle(BaseModel):
    news_source_name: str
    article_content: str
    article_image_description: str
    image_caption: str


def _create_story(article_title: str) -> ChatResponse:
    return chat(
        model="dolphin-phi:latest",
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


def _stable_diffusion_prompt(image_description: str) -> str:
    return chat(
        model=IMAGE_PROMPT_MODEL,
        messages=[
            {
                "role": "user",
                "content": image_description,
            },
        ],
    )


response: ChatResponse = _create_story(
    "Researchers crack the Stonehenge code!"
)

newsarticle = NewsArticle.model_validate_json(response.message.content)
print(
    _stable_diffusion_prompt(
        newsarticle.article_image_description
    ).message.content
)
