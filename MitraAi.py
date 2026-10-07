import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="MitraAI",
    page_icon="🤝",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🤝 MitraAI")
    st.caption("Your AI companion")

    st.divider()

    # New chat button
    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.subheader("Recent")

    st.button("💬 Python project help", use_container_width=True)
    st.button("💬 Data Science notes", use_container_width=True)
    st.button("💬 Explain Machine Learning", use_container_width=True)
    st.button("💬 Create a Resume", use_container_width=True)

    st.divider()

    st.subheader("Workspace")

    st.button("🏠 Home", use_container_width=True)
    st.button("🔖 Saved", use_container_width=True)
    st.button("⚙️ Settings", use_container_width=True)

    st.divider()

    # Dark mode
    st.session_state.dark_mode = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state.dark_mode
    )

    st.divider()

    st.caption("MitraAI v1.0")
    st.caption("Your AI companion 🤝")


# ---------------- MAIN AREA ----------------

st.title("🤝 Meet MitraAI")

st.write(
    "Your intelligent AI companion for learning, coding, "
    "creativity and everyday questions."
)

st.divider()


# ---------------- FEATURE CARDS ----------------

st.subheader("What can I help you with?")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info(
        """
        ### 💡 Brainstorm

        Generate ideas and solutions.
        """
    )

    if st.button("Try Brainstorm", key="brainstorm"):
        st.session_state.messages.append(
            {
                "role": "user",
                "content": "Help me brainstorm some project ideas."
            }
        )
        st.rerun()


with col2:
    st.info(
        """
        ### 💻 Code

        Build, debug and learn code.
        """
    )

    if st.button("Get Coding Help", key="code"):
        st.session_state.messages.append(
            {
                "role": "user",
                "content": "Help me with coding."
            }
        )
        st.rerun()


with col3:
    st.success(
        """
        ### 📚 Learn

        Understand difficult topics.
        """
    )

    if st.button("Start Learning", key="learn"):
        st.session_state.messages.append(
            {
                "role": "user",
                "content": "Explain machine learning in simple words."
            }
        )
        st.rerun()


with col4:
    st.warning(
        """
        ### ✨ Create

        Write, plan and create anything.
        """
    )

    if st.button("Create Something", key="create"):
        st.session_state.messages.append(
            {
                "role": "user",
                "content": "Give me some creative ideas."
            }
        )
        st.rerun()


st.divider()


# ---------------- CHAT AREA ----------------

st.subheader("💬 Conversation")


# Display messages
for message in st.session_state.messages:

    if message["role"] == "user":

        with st.chat_message("user"):
            st.write(message["content"])

    else:

        with st.chat_message("assistant"):
            st.write(message["content"])


# ---------------- CHAT INPUT ----------------

user_message = st.chat_input("Message MitraAI...")


if user_message:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    # Simple demo response
    if "python" in user_message.lower():

        response = """
        🐍 Python is a beginner-friendly programming language.

        You can start with:
        - Variables
        - Data types
        - Conditions
        - Loops
        - Functions
        - Lists and dictionaries
        """

    elif "machine learning" in user_message.lower():

        response = """
        🤖 Machine Learning is a branch of AI where computers
        learn patterns from data and use those patterns to make
        predictions or decisions.
        """

    elif "hello" in user_message.lower() or "hi" in user_message.lower():

        response = """
        Hello! 👋

        I'm MitraAI 🤝

        What would you like to learn or create today?
        """

    else:

        response = f"""
        🤝 I received your message:

        **{user_message}**

        I'm currently running in demo mode.
        """

    # Add AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "✨ MitraAI can make mistakes. Check important information."
)