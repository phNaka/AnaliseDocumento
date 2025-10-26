from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from uteis.config import Config

def analyze_document_from_url(blob_url):
    try:
        credential = AzureKeyCredential(Config.KEY)
        client = DocumentAnalysisClient(Config.ENDPOINT, credential)
        
        # Usar analyze_document_from_url
        poller = client.begin_analyze_document_from_url("prebuilt-businessCard", blob_url)
        result = poller.result()

        print("=" * 50)
        print(f"Documentos encontrados: {len(result.documents)}")
        
        if result.documents:
            document = result.documents[0]
            fields = document.fields
            
            print("\nCAMPOS EXTRAÍDOS:")
            for field_name, field_value in fields.items():
                print(f"  {field_name}: {field_value}")
            
            doc_info = {}
            
            # Nome
            if "ContactNames" in fields and fields["ContactNames"].value:
                contact_names = fields["ContactNames"].value
                if len(contact_names) > 0:
                    contact = contact_names[0].value
                    first_name = contact.get("FirstName")
                    last_name = contact.get("LastName")
                    
                    name_parts = []
                    if first_name:
                        name_parts.append(first_name.value)
                    if last_name:
                        name_parts.append(last_name.value)
                    
                    doc_info["name"] = " ".join(name_parts) if name_parts else None
            
            # Empresa
            if "CompanyNames" in fields and fields["CompanyNames"].value:
                companies = fields["CompanyNames"].value
                if len(companies) > 0:
                    doc_info["company"] = companies[0].value
            
            # Telefone
            if "WorkPhones" in fields and fields["WorkPhones"].value:
                phones = fields["WorkPhones"].value
                if len(phones) > 0:
                    doc_info["phone"] = phones[0].content
            
            # Celular (alternativa)
            if not doc_info.get("phone") and "MobilePhones" in fields and fields["MobilePhones"].value:
                phones = fields["MobilePhones"].value
                if len(phones) > 0:
                    doc_info["phone"] = phones[0].content
            
            # Email
            if "Emails" in fields and fields["Emails"].value:
                emails = fields["Emails"].value
                if len(emails) > 0:
                    doc_info["email"] = emails[0].value
            
            # Website
            if "Websites" in fields and fields["Websites"].value:
                websites = fields["Websites"].value
                if len(websites) > 0:
                    doc_info["website"] = websites[0].value
            
            print(f"\nINFORMAÇÕES EXTRAÍDAS:")
            print(doc_info)
            print("=" * 50)
            
            return doc_info if doc_info else None
        
        print("Nenhum documento reconhecido")
        print("=" * 50)
        return None
        
    except Exception as e:
        print(f"ERRO: {e}")
        import traceback
        traceback.print_exc()
        return None