"""Streamlit chat interface for the e-commerce AI assistant."""

import asyncio
import os
import sys

import streamlit as st
from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner
from google.genai import types

# Ensure the package directory is on the path so sibling imports work
# when Streamlit is launched from outside the package folder.
sys.path.insert(0, os.path.dirname(__file__))

from agent import create_runner  # noqa: E402
from config import PAGE_ICON, PAGE_TITLE, WELCOME_MESSAGE  # noqa: E402

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

load_dotenv()  # reads .env in the working directory or parent dirs

# ---------------------------------------------------------------------------
# Page config & light CSS branding
# ---------------------------------------------------------------------------

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")

st.markdown(
    """
    <style>
    .stApp {max-width: 800px; margin: 0 auto;}
    .stChatMessage {border-radius: 12px;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(f"{PAGE_ICON} {PAGE_TITLE}")

# ---------------------------------------------------------------------------
# Session state initialization
# ---------------------------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "runner" not in st.session_state:
    st.session_state.runner = create_runner()

if "session_id" not in st.session_state:
    # Create a new ADK session via the runner's built-in session service
    runner: InMemoryRunner = st.session_state.runner
    session = asyncio.run(
        runner.session_service.create_session(
            app_name=runner.app_name, user_id="web_user"
        )
    )
    st.session_state.session_id = session.id

# ---------------------------------------------------------------------------
# Helper: call the ADK agent (synchronous)
# ---------------------------------------------------------------------------


def get_agent_response(user_message: str) -> str:
    """Send a message to the agent and return the final text response."""
    runner: InMemoryRunner = st.session_state.runner
    content = types.Content(
        role="user", parts=[types.Part.from_text(text=user_message)]
    )

    async def _run() -> str:
        text = ""
        async for event in runner.run_async(
            user_id="web_user",
            session_id=st.session_state.session_id,
            new_message=content,
        ):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        text += part.text
        return text

    final_text = asyncio.run(_run())

    return final_text.strip() if final_text else "I'm sorry, I couldn't process that. Could you try rephrasing?"


# ---------------------------------------------------------------------------
# Chat display
# ---------------------------------------------------------------------------

# Welcome message (not stored in history — shown every reload)
with st.chat_message("assistant", avatar=PAGE_ICON):
    st.markdown(WELCOME_MESSAGE)

# Render conversation history
for msg in st.session_state.messages:
    avatar = PAGE_ICON if msg["role"] == "assistant" else None
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# ---------------------------------------------------------------------------
# User input handling
# ---------------------------------------------------------------------------

if prompt := st.chat_input("Ask me about products, orders, or shopping..."):
    # Display and store user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get agent response
    with st.chat_message("assistant", avatar=PAGE_ICON):
        with st.spinner("Thinking..."):
            response = get_agent_response(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
