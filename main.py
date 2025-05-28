import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Contador de Silêncio", layout="centered")
st_autorefresh(interval=1000, key="silencio")

data_solicitacao = datetime(2025, 5, 23, 12, 0, 0)

st.markdown("""
<h1 style='text-align: center; color: white;'>⏰ Contador de Silêncio da Gestão do Condomínio</h1>
<p style='font-size: 18px; text-align: center;'>
Desde o dia <strong>23 de maio de 2025, às 12h</strong>, aguarda-se uma resposta formal da gestão (síndico e conselho fiscal)
sobre questionamentos relevantes apresentados pelos condôminos.
</p>
<p style='font-size: 18px; text-align: center;'>
O tempo decorrido desde então está sendo monitorado em tempo real abaixo:
</p>
""", unsafe_allow_html=True)

agora = datetime.now()
tempo_passado = agora - data_solicitacao
dias = tempo_passado.days
horas, resto = divmod(tempo_passado.seconds, 3600)
minutos, segundos = divmod(resto, 60)

st.markdown(f"""
<div style='text-align: center; font-size: 38px; font-weight: bold; color: red; margin: 20px 0;'>
⏳ {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; padding: 15px; background-color: #003566; border-radius: 8px; color: white; font-size: 16px;'>
A falta de resposta pode configurar omissão de dever legal conforme o art. 1.348, VIII do Código Civil.
</div>

<blockquote style='margin-top: 30px; font-style: italic; text-align: center; font-size: 18px;'>
"Transparência não é opção, é obrigação."
</blockquote>

<p style='text-align: center; font-size: 14px; margin-top: 10px;'>
Aplicativo desenvolvido para fins de fiscalização cidadã e gestão condominial transparente.
</p>
""", unsafe_allow_html=True)
