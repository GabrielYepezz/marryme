import streamlit as st

st.title("❤️")
st.subheader("Pedido de Casamento")

# Criando os dois inputs
nome = st.text_input("Digite seu nome completo")
resposta = st.radio("Você aceita casar comigo?", ("Sim!", "Com certeza!"))


# Botão para processar os dados
if st.button("Enviar"):
    if nome and "Sim" in resposta:
        
        st.success(f" AGORA VOCÊ TEM DONO! 💍")
        st.success(f"TEU NOME AGORA É {nome.upper().replace('DALLI', 'YEPEZ')}, CONSIDERE-SE CASADO!")
        
    else:
        st.warning("Por favor, preencha seu nome e selecione uma resposta.")
