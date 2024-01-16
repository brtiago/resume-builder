def read_file(file_path):
    try:
        # Abre o arquivo em modo de leitura
        with open(file_path, 'r') as arquivo:
            # Lê o conteúdo do arquivo
            conteudo = arquivo.read()
            return(conteudo)

    except FileNotFoundError:
        return(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        return(f"Ocorreu um erro: {e}")
