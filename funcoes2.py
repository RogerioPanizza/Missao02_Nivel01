# MicroAtividade Seis

def loginUsuario(perfil):
    if perfil.lower() == "admin":
        print("Bem-vindo, Administrador")
    else:
        print("Bem-vindo, Usuário")

recebe = input("Digite seu nome de usuário: ")
 
loginUsuario(recebe)
 