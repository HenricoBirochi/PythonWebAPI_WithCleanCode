class MinhaClasse:
    def __enter__(self):
        print("Entrando no contexto") # Qualquer ação de inicialização

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saindo do contexto") # Qualquer ação de finalização

with MinhaClasse() as mc:
    print("Dentro do bloco with")
