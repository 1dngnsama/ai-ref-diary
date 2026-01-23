from google import genai
from dotenv import load_dotenv
import os
from logger_config import logger
from asyncio import Semaphore
import asyncio
import time

load_dotenv()

semaphore = Semaphore(10)


class LlmService:
    def __init__(
        self,
        system_prompt: str,
        provider: str = "google",
        model: str = "models/gemini-flash-latest",
        temperature: float = 1.0,
    ):
        self.provider = provider
        self.model = model
        self.temperature = temperature
        self.system_prompt = system_prompt

        if self.provider == "google":
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                logger.error("GOOGLE_API_KEY is not set")
                raise ValueError("Missing GOOGLE_API_KEY")

            self.client = genai.Client(api_key=api_key)
            logger.info("Google Gemini client initialized")

    async def get_response(self, user_prompt: str) -> str:
        request_id = f"gemini_{int(time.time() * 1000)}"

        logger.info(
            "LLM REQUEST | id={} | provider={} | model={} | system_prompt={} | user_prompt={}",
            request_id,
            self.provider,
            self.model,
            self.system_prompt,
            user_prompt,
        )

        async with semaphore:
            try:
                response = await self.client.models.aio.generate_content(
                    model=self.model,
                    system=self.system_prompt,
                    prompt=user_prompt,
                    temperature=self.temperature,
                )

                answer = response.text

                logger.info(
                    "LLM RESPONSE | id={} | answer={}",
                    request_id,
                    answer,
                )

                return answer

            except Exception as e:
                logger.exception(
                    "LLM ERROR | id={} | error={}",
                    request_id,
                    str(e),
                )