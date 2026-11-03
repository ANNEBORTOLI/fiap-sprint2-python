# CONSTANTES DO PROGRAMA

# Níveis de risco. A posição na lista funciona como código do nível: 0 a 3.
NIVEIS_RISCO = ["NORMAL", "ATENÇÃO", "ALERTA", "EMERGÊNCIA"]
NORMAL = 0
ATENCAO = 1
ALERTA = 2
EMERGENCIA = 3

# Quantidade de chuva: chuva em mm e nível da água em cm - em 24h.
CHUVA_ATENCAO = 30
CHUVA_ALERTA = 60
CHUVA_EMERGENCIA = 100
NIVEL_ATENCAO = 120
NIVEL_ALERTA = 200
NIVEL_EMERGENCIA = 300

# Bairros de Juiz de Fora.
BAIRROS = [
    "Parque Burnier",
    "Industrial",
    "Três Moinhos",
    "Santa Rita",
    "Costa Carvalho",
    "Igrejinha",
    "Linhares",
    "Vila Ideal",
]

# Abrigos: a posição do index de cada lista se refere ao bairro i.
ABRIGOS = [
    "Escola Municipal A",
    "Ginásio Poliesportivo B",
    "Escola Estadual C",
    "Centro Comunitário D",
    "Escola Municipal E",
    "Salão Paroquial F",
    "Escola Estadual G",
    "Centro Comunitário H",
]

DISTANCIAS_ABRIGO_M = [850, 600, 1200, 700, 950, 500, 1100, 750]
RUAS_EVITAR = [
    "Rua da encosta principal",
    "Avenida junto ao córrego",
    "Rua da baixada",
    "Travessa do morro",
    "Rua beira-rio",
    "Ladeira da escola",
    "Rua do canal",
    "Rua da várzea",
]

DIAS_SEMANA = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

# Missões de prevenção (Gamificação): [nome, pontos, motivo prático].
MISSOES = [
    ["Registrar bueiro entupido na sua rua", 40,
     "Bueiro entupido alaga a rua na chuva."],
    ["Descartar o lixo só no dia da coleta", 20,
     "Lixo na rua é levado pela água e entope a drenagem."],
    ["Plantar uma muda em área de encosta", 50,
     "As raízes ajudam a segurar o solo."],
    ["Conferir a rota até o seu abrigo", 30,
     "Na hora do alerta, não dá tempo de procurar o caminho."],
    ["Participar do simulado de evacuação", 60,
     "Quem já treinou sai mais rápido e com menos medo."],
    ["Avisar um vizinho sem celular (vigia)", 30,
     "Quem não tem smartphone depende do aviso de alguém."],
]

# Posições dos campos dentro da lista de cada morador.
NOME = 0
BAIRRO = 1
PONTOS = 2
TEM_CELULAR = 3
CONFIRMOU = 4

# Criando os dados para rodar o programa
def criar_matriz_chuvas():
    """Devolve a matriz bairros x dias com chuva (mm) já cadastrada.
    Linha = bairro (mesma ordem de BAIRROS)
    coluna = dia da semana."""
    return [
        [12, 35, 48, 0, 5, 22, 0],   # Parque Burnier
        [10, 30, 40, 2, 4, 18, 0],   # Industrial
        [8, 28, 52, 0, 6, 20, 1],    # Três Moinhos
        [15, 25, 33, 0, 3, 12, 0],   # Santa Rita
        [9, 31, 44, 1, 7, 15, 0],    # Costa Carvalho
        [11, 22, 38, 0, 2, 10, 0],   # Igrejinha
        [14, 27, 41, 3, 5, 19, 2],   # Linhares
        [7, 20, 30, 0, 4, 9, 0],     # Vila Ideal
    ]


def criar_moradores():
    """Devolve a lista de moradores já cadastrados.
    Cada morador é uma lista: [nome, índice do bairro, pontos,
    tem celular (True/False), confirmou segurança (True/False)].
    """
    return [
        ["Cláudia", 0, 120, True, False],
        ["Joaquim", 0, 60, False, False],
        ["Marcos", 1, 90, True, False],
        ["Fernanda", 2, 150, True, False],
        ["Lúcia", 3, 40, False, False],
        ["Rafael", 4, 70, True, False],
        ["Beatriz", 0, 80, True, False],
    ]

def main():
    chuvas = criar_matriz_chuvas()
    moradores = criar_moradores()

    print("==== Bem-vindo ao Guardiões JF ====")

    print(f"Bairros monitorados: {len(BAIRROS)}")
    print(f"Moradores cadastrados: {len(moradores)}")
    print(f"Missões disponíveis: {len(MISSOES)}")

    # Teste rápido: acessando a matriz por [linha][coluna]
    print(f"Chuva no {BAIRROS[0]} na {DIAS_SEMANA[2]}: "
          f"{chuvas[0][2]} mm")
    print(f"Primeiro morador: {moradores[0][NOME]}, "
          f"{moradores[0][PONTOS]} pontos")

# Boa Prática. faz o main() rodar só quando vocês executam o arquivo diretamente.
if __name__ == "__main__":
    main()