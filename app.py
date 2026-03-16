import streamlit as st
from streamlit_confetti import confetti


st.title("❤️")
st.subheader("Pedido de Casamento")

# Criando os dois inputs
nome = st.text_input("Digite seu nome de solteiro?")
resposta = st.radio("Você aceita casar comigo?", ("Sim!", "Com certeza!"))


# Botão para processar os dados
if st.button("Enviar"):
    if nome and "Sim" in resposta:
        # Dispara o efeito de fogos/confete
        confetti(emojis=["🎉", "🎊", "❤️", "✨", ""])
        
        st.success(f" AGORA VOCÊ É MEU! 💍")
        st.success(f"TEU NOME AGORA É {nome.upper().replace('DALLI', 'YEPEZ')}, CONSIDERE-SE CASADO!")
        
    else:
        st.warning("Por favor, preencha seu nome e selecione uma resposta.")