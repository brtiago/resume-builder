from file import read_file
import resume

# resume_txt = read_txtfile(input("Digite o caminho completo do arquivo txt: "))
resume_pdf = read_file(input("Digite o caminho completo do currículo pdf: "))

palavras_chave = input("Digite as palavras-chave a serem utilizadas para a criação do RESUMO PROFISSIONAL: ")
palavras_chave = """desenvolvedor java, java EE, JSF 2, desenvolvimento e manutenção, SQL, dados oracle, tecnologias, 
desenvolvimento de aplicações, MVC, utilizando, EJB, JSP, web, hibernate, spring, JPA, 
desenvolvimento de sistemas, banco de dados """

print(resume.create_resumo(resume_pdf, palavras_chave))
