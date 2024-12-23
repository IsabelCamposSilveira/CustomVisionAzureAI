import streamlit as st
from services.blob_service import upload_blob
from services.custom_vision import custom_vision

def configure_interface():
    st.title("Upload de arquivos - Azure")

    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name

        #Envia para o Blob a imagem
        blob_url = upload_blob(uploaded_file, fileName)

        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso!")

            returnCuston = custom_vision(blob_url) # Chamar a funcao para enviar ao custom vision
            st.write(returnCuston)

        else:
            st.write(f"Erro ao enviar o arquivo {fileName} ao Blob.")


if __name__ == "__main__":
    configure_interface()