from langchain_community.document_loaders import PyPDFLoader

def read_file(filename):
    try:
        return (pdf(filename))
    except FileNotFoundError:
        return (f"O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        return (f"Ocorreu um erro: {e}")

def pdf(filename):
    return PyPDFLoader(filename).load_and_split()[0]
def txt(filename):
    with open(filename, 'r') as file:
        return file.read()