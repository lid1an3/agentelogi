class AgenteLogico:

    def decidir_assistir_filme(self, idade, classificacao_etaria):
        if idade >= classificacao_etaria:
            return "Você pode assistir ao filme."
        else:
            return "Você não pode assistir ao filme devido à classificação etária."

if __name__ == "__main__":
    agente = AgenteLogico()

    idade = int(input("Digite a sua idade: "))
    classificacao_etaria = int(input("Digite a classificação etária do filme: "))

    decisao = agente.decidir_assistir_filme(idade, classificacao_etaria)
    print(decisao)
