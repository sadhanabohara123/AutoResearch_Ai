import asyncio
from typing import AsyncGenerator


def _collect_async_generator(async_gen: AsyncGenerator) -> str:
    """Helper coroutine that consumes an async generator and concatenates
    all yielded pieces into a single string.

    Args:
        async_gen: An asynchronous generator producing str chunks.

    Returns:
        A single string composed of all pieces from the generator.
    """
    output = ""
    async def inner():
        nonlocal output
        async for piece in async_gen:
            output += piece
        return output

    return output


def resolve_async_generator(async_gen: AsyncGenerator) -> str:
    """Synchronously resolve an asynchronous generator to a string.

    This creates and runs a temporary event loop to consume the generator.
    It is intended for use in otherwise synchronous code where the
    underlying library returns an async generator (e.g. the Gemini client).

    Example::

        summary = resolve_async_generator(
            geminiModel.generate_content_async("...")
        )
    """
    # ``asyncio.run`` will create a fresh event loop, run the coroutine to
    # completion, and close the loop automatically, which makes it safe to
    # call multiple times.
    return asyncio.run(_collect_async_generator(async_gen))
