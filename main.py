import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from preprocess import process_posts
import json

length = ['short', 'medium', 'long']
language = ['English', 'Roman Urdu']
influencer = ['Cassie Kozyrkov', 'Fabio Moioli', 'Helen Yu']  # ideally: real names like ['Ali Abdaal', 'Gary Vee', ...]

# === Triggered when influencer is changed ===
fs = FewShotPosts()
def on_influencer_change():
    selected_influencer = st.session_state.influencer
    process_posts(selected_influencer, "processed_posts.json")

    # Recreate FewShotPosts after processing new data
    st.session_state.tags = fs.get_tags()

def main():
    st.title('LinkedIn Post Generator.')
    with st.sidebar:
        st.markdown("### 🙌 Credit")
        st.markdown(
        "Writing style inspired by:\n"
        "- Cassie Kozyrkov\n"
        "- Fabio Moioli\n"
        "- Helen Yu\n\n"
        "_This tool is for educational and creative inspiration purposes._"
    )

    # Set default tags in session state
    if 'tags' not in st.session_state:
        st.session_state.tags = fs.get_tags()

    # First row: Influencer
    st.selectbox(
        'Influencer',
        options=influencer,
        key='influencer',
        on_change=on_influencer_change
    )

    # Second row: Topic, Length, Language
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_tags = st.selectbox('Topic', options=st.session_state.tags, key='topic')
    with col2:
        selected_length = st.selectbox('Length', options=length, key='length')
    with col3:
        selected_language = st.selectbox('Language', options=language, key='language')

    if st.button('Generate'):
        post = generate_post(
            st.session_state.length,
            st.session_state.language,
            st.session_state.topic
        )
        st.write(post)

if __name__ == '__main__':
    main()
