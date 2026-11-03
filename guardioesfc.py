# =====================================================================
# CONSTANTES DO PROGRAMA
# =====================================================================
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

# =====================================================================
# CRIAÇÃO DOS DADOS INICIAIS
# =====================================================================
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

# =====================================================================
# FUNÇÕES DE ENTRADA (VALIDAÇÃO DOS INPUTS)
# =====================================================================
def ler_inteiro(mensagem, minimo, maximo):
    """Pede um número inteiro até ele ser válido e estar na faixa."""
    while True:
        entrada = input(mensagem).strip()
        if not entrada.isdigit() or not entrada.isascii():
            print(f"  Valor inválido. Digite um número inteiro "
                  f"de {minimo} a {maximo}.")
            continue
        valor = int(entrada)
        if valor < minimo or valor > maximo:
            print(f"  Fora da faixa permitida ({minimo} a {maximo}). "
                  f"Tente de novo.")
            continue
        return valor


def ler_texto(mensagem, tamanho_minimo):
    """Pede um texto só com letras e espaços, com tamanho mínimo."""
    while True:
        texto = input(mensagem).strip()
        sem_espacos = texto.replace(" ", "")
        if len(sem_espacos) < tamanho_minimo:
            print(f"  Digite pelo menos {tamanho_minimo} letras.")
        elif not sem_espacos.isalpha():
            print("  Use apenas letras e espaços.")
        else:
            return texto.title()


def ler_sim_nao(mensagem):
    """Pede uma resposta S/N e devolve True para sim, False para não."""
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ["s", "sim"]:
            return True
        if resposta in ["n", "nao", "não"]:
            return False
        print("  Responda com S (sim) ou N (não).")

# =====================================================================
# FUNÇÕES AUXILIARES
# =====================================================================

def escolher_bairro(bairros):
    """Lista os bairros numerados e devolve o índice escolhido."""
    for i in range(len(bairros)):
        print(f"  {i + 1}. {bairros[i]}")
    opcao = ler_inteiro("Número do bairro: ", 1, len(bairros))
    return opcao - 1


def contar_moradores_bairro(moradores, indice_bairro):
    """Conta quantos moradores do bairro têm e não têm celular."""
    com_celular = 0
    sem_celular = 0
    for morador in moradores:
        if morador[BAIRRO] != indice_bairro:
            continue   # morador de outro bairro: pula
        if morador[TEM_CELULAR]:
            com_celular += 1
        else:
            sem_celular += 1
    return com_celular, sem_celular

# =====================================================================
# REGRAS DE NEGÓCIO
# =====================================================================

def classificar_risco(chuva_mm, nivel_cm):
    """Classifica o risco a partir da chuva (mm/24 h) e do nível da
    água (cm). Vale o pior dos dois indicadores. Devolve 0 a 3."""
    if chuva_mm >= CHUVA_EMERGENCIA or nivel_cm >= NIVEL_EMERGENCIA:
        return EMERGENCIA
    elif chuva_mm >= CHUVA_ALERTA or nivel_cm >= NIVEL_ALERTA:
        return ALERTA
    elif chuva_mm >= CHUVA_ATENCAO or nivel_cm >= NIVEL_ATENCAO:
        return ATENCAO
    else:
        return NORMAL


def obter_orientacao(indice_risco):
    """Devolve a lista de passos de "O que fazer agora" para o nível."""
    match indice_risco:
        case 0:
            return ["Sem risco no momento.",
                    "Aproveite para conferir a rota até o seu abrigo."]
        case 1:
            return ["Fique atento aos próximos avisos oficiais.",
                    "Separe documentos, remédios e lanterna.",
                    "Desconfie de mensagens que não sejam da "
                    "Defesa Civil."]
        case 2:
            return ["Saia da encosta e vá para o abrigo indicado.",
                    "Não atravesse ruas alagadas, nem a pé nem de carro.",
                    "Avise um vizinho que não tem celular."]
        case 3:
            return ["Saia AGORA para o abrigo indicado.",
                    "Se não conseguir sair, vá para o ponto mais alto "
                    "e ligue 199 (Defesa Civil) ou 193 (Bombeiros).",
                    "Não volte para buscar objetos."]
        case _:
            return ["Nível de risco desconhecido."]


def exibir_cartao_alerta(indice_bairro, chuva_mm, nivel_cm, indice_risco):
    """Mostra o cartão de alerta: nível, o que fazer agora, abrigo e 
    rua a evitar."""
    print("\n" + "-" * 62)
    print(f" {NIVEIS_RISCO[indice_risco]}  |  {BAIRROS[indice_bairro]}")
    print("-" * 62)
    print(f" Chuva em 24 h: {chuva_mm} mm   |   "
          f"Nível da água: {nivel_cm} cm")
    print("\n O que fazer agora:")
    passos = obter_orientacao(indice_risco)
    for numero in range(len(passos)):
        print(f"   {numero + 1}. {passos[numero]}")
    print(f"\n Abrigo mais próximo: {ABRIGOS[indice_bairro]}, "
          f"{DISTANCIAS_ABRIGO_M[indice_bairro]} m")
    if indice_risco >= ALERTA:
        print(f" Evite: {RUAS_EVITAR[indice_bairro]}")
    print("-" * 62)

# =====================================================================
# FUNCIONALIDADES DO MENU
# =====================================================================

def registrar_leitura(chuvas, niveis_agua, riscos, moradores):
    """Opção 1: registra uma leitura, classifica o risco e mostra o
    alerta com orientação. Devolve o nível de risco calculado."""
    print("\n" + "=" * 62)
    print(" REGISTRAR LEITURA E CLASSIFICAR RISCO")
    print("=" * 62)
    indice_bairro = escolher_bairro(BAIRROS)

    print("\nDia da leitura:")
    for i in range(len(DIAS_SEMANA)):
        print(f"  {i + 1}. {DIAS_SEMANA[i]}")
    indice_dia = ler_inteiro("Número do dia: ", 1, len(DIAS_SEMANA)) - 1

    chuva = ler_inteiro("Chuva nas últimas 24 h (0 a 500 mm): ", 0, 500)
    nivel = ler_inteiro("Nível da água do córrego (0 a 1000 cm): ",
                        0, 1000)

    risco_novo = classificar_risco(chuva, nivel)

    # Guarda os dados: a chuva vai para a matriz (bairro x dia).
    chuvas[indice_bairro][indice_dia] = chuva
    niveis_agua[indice_bairro] = nivel
    riscos[indice_bairro] = risco_novo

    exibir_cartao_alerta(indice_bairro, chuva, nivel, risco_novo)

    # Alerta multicanal: quem não tem smartphone recebe ligação de voz.
    if risco_novo >= ATENCAO:
        com_celular, sem_celular = contar_moradores_bairro(
            moradores, indice_bairro)
        print(f" Aviso enviado a {com_celular + sem_celular} morador(es)"
              f" cadastrado(s):")
        print(f"   {com_celular} por push/SMS e {sem_celular} por "
              f"ligação de voz.")
    return risco_novo

# =====================================================================
# MENU PRINCIPAL
# =====================================================================
def exibir_menu():
    """Mostra as opções do menu principal."""
    print("Guardiões JF - Juiz de Fora/MG")
    print("  1. Registrar leitura e classificar risco do bairro")
    print("  2. Relatório de chuvas da semana")
    print("  3. Consultar abrigo do meu bairro")
    print("  4. Cadastrar morador")
    print("  5. Registrar missão de prevenção")
    print("  6. Ranking comunitário")
    print("  7. Confirmar que estou em segurança")
    print("  8. Painel da Defesa Civil")
    print("  0. Sair")


def main():
    """Cria os dados e mantém o menu rodando até o usuário sair."""
    chuvas = criar_matriz_chuvas()
    moradores = criar_moradores()
    niveis_agua = [80, 60, 90, 50, 70, 40, 85, 45]   # cm, simulado
    riscos = [NORMAL] * len(BAIRROS)

    executando = True
    while executando:
        exibir_menu()
        opcao = ler_inteiro("Escolha uma opção: ", 0, 8)
        match opcao:
            case 1:
                registrar_leitura(chuvas, niveis_agua, riscos, moradores)
            case 2:
                print("\nRelatório de chuvas")
            case 3:
                print("\nConsultar abrigo")
            case 4:
                print("\nCadastrar morador")
            case 5:
                print("\nRegistrar missão")
            case 6:
                print("\nRanking comunitário")
            case 7:
                print("\nConfirmar segurança")
            case 8:
                print("\nPainel da Defesa Civil")
            case 0:
                executando = False
                print("\nAté logo! Prevenção é hábito coletivo.")

if __name__ == "__main__":
    main()