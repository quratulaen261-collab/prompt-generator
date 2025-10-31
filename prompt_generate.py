import streamlit as st
import random

st.set_page_config(page_title="Prompt Generator", page_icon="🤖", layout="centered")

st.title("Prompt Generator")
st.write("Generate 5 prompts for your next content idea!")

prompt_templates = [
    "Write a {tone} blog post about {topic} for {audience}.",
    "Create {number} creative headlines for {topic}.",
    "Generate ideas for {topic} that appeal to {audience}.",
    "Design a social media caption about {topic} with a {tone} tone.",
    "Make a list of {number} engaging questions on {topic}.",
    "Craft a {tone} product description for {topic}.",
    "Brainstorm {number} content ideas about {topic} for {audience}.",
]

topics = ["AI content creation", "digital marketing", "remote work", "productivity hacks", "personal branding"]
tones = ["fun", "professional", "casual", "motivational", "educational"]
audiences = ["entrepreneurs", "content creators", "freelancers", "students", "marketers"]
numbers = ["5", "10", "15"]

if st.button("Generate Prompts"):
    st.subheader("Here are your 5 AI prompts:")
    for i in range(5):
        prompt = random.choice(prompt_templates).format(
            tone=random.choice(tones),
            topic=random.choice(topics),
            audience=random.choice(audiences),
            number=random.choice(numbers)
        )
        st.markdown(f"**{i+1}.** {prompt}")

st.write("---")
st.caption("Built")
