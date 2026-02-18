
from google import genai
import streamlit as st
import random
def get_joke() :
    jokes = [
        "why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the Javascript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why don't programmers like nature? It has too many bugs.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the Javascript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why do Python programmers prefer using snake_case? Because it's easier to read!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 -- Dec 25.",
        "Why did the programmer get kicked out of the beach? Because he kept using the 'C' language!",
        "Why was the computer cold? It left its Windows open."
    ]
    return random.choice(jokes)
# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="✍️",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #f9f9f9; }
    .stButton>button {
        background-color: #4F8EF7;
        color: white;
        border-radius: 8px;
        padding: 0.5em 2em;
        font-size: 16px;
        border: none;
    }
    .stButton>button:hover { background-color: #2f6ed5; }
    .blog-output {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #ddd;
        white-space: pre-wrap;
        line-height: 1.7;
        font-size: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ── Title ─────────────────────────────────────────────────────────────────────
st.title("✍️ AI Blog Generator")
st.markdown("Powered by **Gemini 2.5 Flash** · Enter a topic and get a ready-to-publish blog post.")

st.divider()

# ── Inputs ────────────────────────────────────────────────────────────────────
col1, col2 = st.columns([3, 1])
with col1:
    topic = st.text_input(
        "📌 Blog Topic",
        placeholder="e.g. The Future of Renewable Energy",
    )
with col2:
    word_count = st.selectbox(
        "📝 Word Count",
        options=[200, 400, 600, 800, 1000],
        index=1,
    )

tone = st.selectbox(
    "🎨 Writing Tone",
    options=["Informative", "Casual & Friendly", "Professional", "Persuasive", "Story-telling"],
)

keywords = st.text_input(
    "🔑 Keywords to include (optional, comma-separated)",
    placeholder="e.g. sustainability, solar panels, carbon footprint",
)

# ── Generate Button ───────────────────────────────────────────────────────────
generate_btn = st.button("🚀 Generate Blog Post", use_container_width=True)

# ── Generation Logic ──────────────────────────────────────────────────────────
def build_prompt(topic: str, word_count: int, tone: str, keywords: str) -> str:
    kw_line = f"\n- Naturally include these keywords: {keywords}" if keywords.strip() else ""
    return f"""You are an expert blog writer. Write a complete, engaging blog post with the following specs:

- Topic: {topic}
- Target word count: approximately {word_count} words
- Tone: {tone}{kw_line}

Structure the post with:
1. A catchy title (use # Markdown heading)
2. An engaging introduction
3. Well-organised body sections (use ## headings)
4. A concise conclusion

Write only the blog post — no commentary or meta-text outside of it."""

api_key = "AIzaSyDjRzvzyLINhpT2vGWrvCGKqdxG5dw6Ad4"

def generate_blog(api_key: str, topic: str, word_count: int, tone: str, keywords: str) -> str:
    st.write("### @ Generating your recepie ... ")
    st.write(f"While I work on creating your blog, here's a little joke to keep you entertained: \n\n ** {get_joke()} ** ")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.5-flash"
    prompt = build_prompt(topic, word_count, tone, keywords)

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text
if generate_btn:
    # Validation
    if not api_key:
        st.warning("⚠️ Please enter your Gemini API key in the sidebar.")
    elif not topic.strip():
        st.warning("⚠️ Please enter a blog topic.")
    else:
        with st.spinner("✨ Generating your blog post…"):
            try:
                blog_text = generate_blog(api_key, topic, word_count, tone, keywords)

                st.success("✅ Blog post generated!")
                st.divider()

                # Display rendered markdown
                st.markdown("### 📄 Your Blog Post")
                st.markdown(blog_text)

                st.divider()

                # Copy / Download options
                col_a, col_b = st.columns(2)
                with col_a:
                    st.download_button(
                        label="⬇️ Download as .txt",
                        data=blog_text,
                        file_name=f"{topic[:30].replace(' ', '_')}_blog.txt",
                        mime="text/plain",
                        use_container_width=True,
                    )
                with col_b:
                    st.download_button(
                        label="⬇️ Download as .md",
                        data=blog_text,
                        file_name=f"{topic[:30].replace(' ', '_')}_blog.md",
                        mime="text/markdown",
                        use_container_width=True,
                    )

            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info("Double-check your API key and make sure it has access to Gemini 1.5 Flash.")

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built with Streamlit + Google Gemini 2.5 Flash 🤖")