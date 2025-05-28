import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# ✅ Configuração inicial — deve ser o primeiro comando
st.set_page_config(page_title="Contador de Silêncio", layout="centered")

# 🔁 Auto atualização a cada 1 segundo
st_autorefresh(interval=1000, key="silencio")

# 📅 Data de início do silêncio
data_solicitacao = datetime(2025, 5, 23, 12, 0, 0)
agora = datetime.now()
tempo_passado = agora - data_solicitacao
dias = tempo_passado.days
horas, resto = divmod(tempo_passado.seconds, 3600)
minutos, segundos = divmod(resto, 60)

# 🎯 Estilo e cabeçalho
st.markdown("""
    <h1 style='text-align: center; color: #d90429; font-size: 42px;'>📢 CONTADOR DE SILÊNCIO</h1>
    <p style='text-align: center; font-size: 20px;'>
        Aguardamos desde <strong>23 de maio de 2025 às 12h</strong> uma resposta formal do <strong>síndico e conselho</strong> do condomínio.
    </p>
""", unsafe_allow_html=True)

# 🕒 Contador em destaque
st.markdown(f"""
    <div style='text-align: center; font-size: 48px; font-weight: bold; color: red; margin: 20px 0;'>
        ⏱️ {dias} dias, {horas:02}h {minutos:02}min {segundos:02}s de silêncio
    </div>
""", unsafe_allow_html=True)

# 🔘 Botões de denúncia e compartilhamento
url_site = "https://silencio.streamlit.app"
msg_whatsapp = "Veja o tempo de silêncio da gestão do nosso condomínio ⏱️\nhttps://silencio.streamlit.app"
msg_email = "Prezados,%0A%0AO silêncio da gestão condominial persiste desde 23/05/2025 às 12h.%0AConfira o contador em tempo real: https://silencio.streamlit.app%0A%0AAtenciosamente,%0ACondômino vigilante"

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
        <a href="https://wa.me/?text={msg_whatsapp}" target="_blank">
            <button style="padding: 10px 20px; font-size: 18px; background-color: #25D366; color: white; border: none; border-radius: 5px;">
                📲 Compartilhar no WhatsApp
            </button>
        </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <a href="mailto:sindico@exemplo.com?subject=Omissão de resposta&body={msg_email}" target="_blank">
            <button style="padding: 10px 20px; font-size: 18px; background-color: #d00000; color: white; border: none; border-radius: 5px;">
                🚨 Denunciar por E-mail
            </button>
        </a>
    """, unsafe_allow_html=True)

# 📌 Informativo Legal
st.markdown("""
    <div style='text-align: center; background-color: #003566; color: white; padding: 12px; border-radius: 8px; font-size: 16px; margin-top: 30px;'>
        ⚖️ O Código Civil (art. 1.348, VIII) exige que o síndico preste contas e responda aos condôminos. A omissão pode configurar infração legal.
    </div>
""", unsafe_allow_html=True)

# 📢 Frase de impacto e rodapé
st.markdown("""
    <blockquote style='text-align: center; font-style: italic; font-size: 18px; margin-top: 20px;'>
        “Transparência não é favor. É dever.”
    </blockquote>
    <p style='text-align: center; font-size: 14px;'>
        Aplicativo criado por condôminos vigilantes para promover transparência e boa gestão.
    </p>
""", unsafe_allow_html=True)
