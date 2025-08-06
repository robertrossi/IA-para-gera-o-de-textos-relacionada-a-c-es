import streamlit as st
from src.llm_config import load_llm
from src.generate import llm_generate

st.set_page_config(page_title="Gerador de conteúdo 🤖", page_icon="🤖")
st.title("Gerador de conteúdo")

# Campos do formulário
topic = st.text_input("Tema:", placeholder="Ex: Raças, alimentação saudável, curiosidades...")
platform = st.selectbox("Plataforma:", ['Instagram', 'Facebook', 'LinkedIn', 'Blog', 'E-mail, whatsapp'])
tone = st.selectbox("Tom:", ['Normal', 'Informativo', 'Inspirador', 'Urgente', 'Informal'])
length = st.selectbox("Tamanho:", ['Curto', 'Médio', 'Longo'])
audience = st.selectbox("Público-alvo:", ['Geral', 'Jovens adultos', 'Famílias', 'Idosos', 'Adolescentes'])
cta = st.checkbox("Incluir CTA")
hashtags = st.checkbox("Retornar Hashtags")
keywords = st.text_area("Palavras-chave (SEO):", placeholder="Ex: bem-estar, curiosidades, raças...")

if st.button("Gerar conteúdo"):
    prompt = f"""
    Escreva um texto com SEO otimizado sobre o tema '{topic}'.
    Retorne em sua resposta apenas o texto final e não inclua ela dentro de aspas.
    - Onde será publicado: {platform}.
    - Tom: {tone}.
    - Público-alvo: {audience}.
    - Comprimento: {length}.
    - {"Inclua uma chamada para ação clara." if cta else "Não inclua chamada para ação"}
    - {"Retorne ao final do texto hashtags relevantes." if hashtags else "Não inclua hashtags."}
    {"- Palavras-chave que devem estar presentes nesse texto (para SEO): " + keywords if keywords else ""}
    """
    try:
        llm = load_llm()
        res = llm_generate(llm, prompt)
        st.markdown(res)
    except Exception as e:
        st.error(f"Erro: {e}")
