import streamlit  as st
from services.blob_service import upload_blob
from services.documento_service import analyze_document_from_url

def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio 2 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo para enviar", type=["pdf", "png", "jpg", "jpeg"])
    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Blob Storage.")
            document_info = analyze_document_from_url(blob_url)  #chamar a funcao de deteccao de dados do documento
            show_image_and_validation(blob_url, document_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para o Blob Storage.")

def show_image_and_validation(blob_url, document_info):
    st.image(blob_url, caption="Arquivo enviado", use_container_width=True)
    st.write("Resultados da Análise do Documento:")
    if document_info:
        st.markdown(f"<H1 stye='color:green;'>Documento Válido</H1>", unsafe_allow_html=True)
        st.write(f"Nome: {document_info.get('name')}")
        st.write(f"Empresa: {document_info.get('company')}")
        st.write(f"Telefone: {document_info.get('phone')}")
        st.write(f"Email: {document_info.get('email')}")
        st.write(f"Website: {document_info.get('website')}")
    else:
        st.markdown(f"<H1 style='color:red;'>Documento Inválido</H1>", unsafe_allow_html=True)
        st.write("Não foi possível extrair as informações do documento.")

if __name__ == "__main__":
    configure_interface()