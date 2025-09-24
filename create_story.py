import re

from ollama import ChatResponse, chat
from pydantic import BaseModel

IMAGE_PROMPT_MODEL = "impactframes/llama3_ifai_sd_prompt_mkr_q4km:latest"
ARTICLE_GENERATION_MODEL = "deepseek-r1:7b"

DONT_WANT = ["^", "{", "}", "#", "_"]


class NewsArticle(BaseModel):
    article_content: str
    article_title: str
    article_image_description: str
    article_author: str
    short_image_caption: str
    article_date: str


def _create_story(article_summary: str, year: str) -> ChatResponse:
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
                    f"Please create an article from the year {year} with the"
                    f" given content: {article_summary}"
                ),
            },
        ],
        format=NewsArticle.model_json_schema(),
    )


def _stable_diffusion_prompt(
    image_description: str, prompt_model: str = IMAGE_PROMPT_MODEL
) -> str:
    return chat(
        model=prompt_model,
        messages=[
            {
                "role": "user",
                "content": (
                    f"{image_description}, photorealistic, 4K, detailed,"
                    " cinematic lighting"
                ),
            },
        ],
    )


def _clear_weird_characters(text: str) -> str:
    text = (
        re.sub(r"[^\x00-\x7F]+", "", text)
        .replace("\\", r"\textbackslash{}")
        .replace("&", r"\&")
        .replace("$", r"\$")
        .replace("%", r"\%")
    )
    for char in DONT_WANT:
        text = text.replace(char, "")
    return text


def create_story(article_summary: str, year: str):
    response: ChatResponse = _create_story(article_summary, year)
    news_article = NewsArticle.model_validate_json(response.message.content)

    # remove other characters that deepseek sometimes spits out
    news_article.article_content = _clear_weird_characters(
        news_article.article_content
    )
    news_article.article_title = _clear_weird_characters(
        news_article.article_title
    )
    news_article.article_image_description = _clear_weird_characters(
        news_article.article_image_description
    )
    news_article.article_author = _clear_weird_characters(
        news_article.article_author
    )

    image_prompt = _stable_diffusion_prompt(
        news_article.article_image_description
    ).message.content

    return (news_article, image_prompt)
