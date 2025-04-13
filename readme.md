
---

```markdown
````
# 🚀 LinkedIn Post Generator (AI-powered)

![App Screenshot](https://i.imgur.com/ZVKWwIA.png)

This is a Streamlit-based web application that generates high-quality, influencer-style LinkedIn posts using AI. Inspired by the writing styles of leading thought leaders like **Cassie Kozyrkov**, **Fabio Moioli**, and **Helen Yu**, this app helps you craft posts by selecting influencer style, post topic, language, and length.

---
```
## ✨ Features

- 🔥 **Few-shot post generation** trained on curated influencer posts  
- 🧠 Choose from 3 influencer styles to shape the tone and message  
- ✍️ Customize by topic, language (English or Roman Urdu), and post length  
- 🎯 AI-powered content filtering and style mimicry  
- 🌱 Built with LangChain + Groq LLM + Streamlit  

---

## 🖼 App Preview

> 📌 _Add a screenshot of your app interface above._  
> You can upload it to GitHub and update the image link above to point to your file.

---
```
## 🛠 Project Structure
```
├── main.py              # Streamlit app entry point
├── few_shot.py          # Tag extraction and filtering logic
├── llm_helper.py        # LangChain + Groq LLM setup
├── post_generator.py    # Post creation logic (not shown here)
├── preprocess.py        # Metadata enrichment + tag unification (not shown here)
├── data/
│   ├── cassie_kazyrkov.json
│   ├── fabio_moioli.json
│   ├── helen_yu.json
│   └── processed_posts.json

```
---

## ▶️ How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/mubashir06/linkedin-post-generator.git
cd linkedin-post-generator
```

2. **Create a virtual environment & install dependencies:**

```bash
python -m venv venv
source venv/bin/activate        # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

3. **Set up environment variables:**

Create a `.env` file and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the app:**

```bash
streamlit run main.py
```

---

## 📚 Credit & Acknowledgements

This tool draws inspiration from the writing styles and thought leadership of:

- [Cassie Kozyrkov](https://www.linkedin.com/in/kozyrkov/)
- [Fabio Moioli](https://www.linkedin.com/in/fabiomoioli/)
- [Helen Yu](https://www.linkedin.com/in/yuhelenyu/)

_All content generated is for educational and creative purposes only._

---

## 📌 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 💡 Future Ideas

- Add GPT-4 / Claude support  
- User-authenticated post history  
- One-click post to LinkedIn API  
- Style blending or custom influencer uploads  

---
```
