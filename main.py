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

# Acumulado da semana a partir do qual o solo é tratado como encharcado.
ACUMULADO_SOLO_ENCHARCADO = 150

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


def pausar():
    """Espera o usuário apertar Enter antes de voltar ao menu."""
    input("\nPressione Enter para voltar ao menu...")
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


def calcular_estatisticas(valores):
    """Devolve total, média, maior e menor de uma lista de números."""
    total = 0
    maior = valores[0]
    menor = valores[0]
    for valor in valores:
        total += valor
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    media = total / len(valores)
    return total, media, maior, menor


def buscar_morador(moradores, nome):
    """Procura um morador pelo nome. Devolve o índice ou -1 se não
    encontrar."""
    indice_encontrado = -1
    for i in range(len(moradores)):
        if moradores[i][NOME].lower() == nome.lower():
            indice_encontrado = i
            break   # achou: não precisa olhar o resto da lista
    return indice_encontrado


def escolher_morador(moradores, bairros):
    """Lista os moradores numerados e devolve o índice escolhido."""
    for i in range(len(moradores)):
        morador = moradores[i]
        print(f"  {i + 1}. {morador[NOME]:<14} "
              f"({bairros[morador[BAIRRO]]})")
    opcao = ler_inteiro("Número do morador: ", 1, len(moradores))
    return opcao - 1
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


def relatorio_chuvas(chuvas):
    """Opção 2: percorre a matriz e mostra totais, médias, maior e
    menor valor por bairro, além do dia mais chuvoso."""
    print("\n" + "=" * 62)
    print(" RELATÓRIO DE CHUVAS DA SEMANA (mm)")
    print("=" * 62)

    # Cabeçalho da tabela
    cabecalho = f"{'Bairro':<16}"
    for dia in DIAS_SEMANA:
        cabecalho += f"{dia:>5}"
    cabecalho += f"{'Total':>7}{'Média':>7}{'Maior':>7}{'Menor':>7}"
    print(cabecalho)
    print("-" * len(cabecalho))

    # Uma linha da tabela para cada linha da matriz (bairro)
    totais_bairros = []
    for i in range(len(BAIRROS)):
        linha = f"{BAIRROS[i]:<16}"
        for valor in chuvas[i]:
            linha += f"{valor:>5}"
        total, media, maior, menor = calcular_estatisticas(chuvas[i])
        totais_bairros.append(total)
        linha += f"{total:>7}{media:>7.1f}{maior:>7}{menor:>7}"
        print(linha)

    # Soma de cada coluna (dia) da matriz
    totais_dias = []
    for j in range(len(DIAS_SEMANA)):
        soma_dia = 0
        for i in range(len(BAIRROS)):
            soma_dia += chuvas[i][j]
        totais_dias.append(soma_dia)

    # Dia com a maior soma de chuva
    indice_dia = 0
    for j in range(len(totais_dias)):
        if totais_dias[j] > totais_dias[indice_dia]:
            indice_dia = j

    # Estatísticas dos bairros
    total_geral, media_bairro, maior_total, menor_total = (
        calcular_estatisticas(totais_bairros))
    indice_mais = totais_bairros.index(maior_total)
    indice_menos = totais_bairros.index(menor_total)

    print("\nResumo:")
    print(f"  Chuva somada de todos os bairros: {total_geral} mm")
    print(f"  Média por bairro na semana: {media_bairro:.1f} mm")
    print(f"  Maior acumulado: {BAIRROS[indice_mais]} "
          f"({maior_total} mm)")
    print(f"  Menor acumulado: {BAIRROS[indice_menos]} "
          f"({menor_total} mm)")
    print(f"  Dia mais chuvoso: {DIAS_SEMANA[indice_dia]} "
          f"({totais_dias[indice_dia]} mm somando os bairros)")

    # Solo encharcado aumenta o risco de deslizamento
    print(f"\nBairros com solo encharcado "
          f"(acumulado >= {ACUMULADO_SOLO_ENCHARCADO} mm):")
    encontrou = False
    for i in range(len(BAIRROS)):
        if totais_bairros[i] < ACUMULADO_SOLO_ENCHARCADO:
            continue   # abaixo do limite: pula para o próximo bairro
        encontrou = True
        print(f"  - {BAIRROS[i]}: {totais_bairros[i]} mm. "
              f"Atenção redobrada a encostas.")
    if not encontrou:
        print("  Nenhum bairro acima do limite nesta semana.")


def consultar_abrigo(niveis_agua, riscos):
    """Opção 3: o morador escolhe o bairro e vê o abrigo, a distância,
    a rua a evitar e a situação atual."""
    print("\n" + "=" * 62)
    print(" CONSULTAR ABRIGO DO MEU BAIRRO")
    print("=" * 62)
    indice = escolher_bairro(BAIRROS)

    risco = riscos[indice]
    print(f"\n Bairro: {BAIRROS[indice]}")
    print(f" Situação atual: {NIVEIS_RISCO[risco]} "
          f"(nível da água: {niveis_agua[indice]} cm)")
    print(f" Abrigo de referência: {ABRIGOS[indice]}, "
          f"{DISTANCIAS_ABRIGO_M[indice]} m")
    print(f" Em dia de chuva forte, evite: {RUAS_EVITAR[indice]}")


def cadastrar_morador(moradores):
    """Opção 4: cadastra um novo morador na lista."""
    print("\n" + "=" * 62)
    print(" CADASTRAR MORADOR")
    print("=" * 62)

    # Repete até receber um nome que ainda não está cadastrado
    while True:
        nome = ler_texto("Nome do morador: ", 2)
        if buscar_morador(moradores, nome) == -1:
            break
        print("  Já existe um morador com esse nome. "
              "Use nome e sobrenome.")

    print("Bairro onde mora:")
    indice_bairro = escolher_bairro(BAIRROS)
    tem_celular = ler_sim_nao("Tem smartphone para receber alertas? (S/N): ")

    # Novo morador: começa com 0 pontos e sem confirmação de segurança
    moradores.append([nome, indice_bairro, 0, tem_celular, False])

    if tem_celular:
        canal = "push e SMS"
    else:
        canal = "ligação de voz e vigia de bairro"

    print(f"\n {nome} cadastrado(a) em {BAIRROS[indice_bairro]}.")
    print(f" Canal de alerta: {canal}.")
    print(f" Total de moradores cadastrados: {len(moradores)}")


def registrar_missao(moradores):
    """Opção 5: registra uma missão de prevenção e soma os pontos.
    Devolve o novo total de pontos do morador."""
    print("\n" + "=" * 62)
    print(" REGISTRAR MISSÃO DE PREVENÇÃO")
    print("=" * 62)
    print("Quem cumpriu a missão?")
    indice_morador = escolher_morador(moradores, BAIRROS)

    print("\nMissões disponíveis:")
    for i in range(len(MISSOES)):
        print(f"  {i + 1}. {MISSOES[i][0]} (+{MISSOES[i][1]} pontos)")
        print(f"     Por quê: {MISSOES[i][2]}")
    indice_missao = ler_inteiro("Número da missão: ", 1, len(MISSOES)) - 1

    # Soma os pontos da missão ao total do morador
    morador = moradores[indice_morador]
    pontos_missao = MISSOES[indice_missao][1]
    morador[PONTOS] += pontos_missao

    print(f"\n Missão registrada: {MISSOES[indice_missao][0]}")
    print(f" {morador[NOME]} ganhou +{pontos_missao} pontos. "
          f"Total: {morador[PONTOS]} pontos.")
    return morador[PONTOS]
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
                relatorio_chuvas(chuvas)
            case 3:
                consultar_abrigo(niveis_agua, riscos)
            case 4:
                cadastrar_morador(moradores)
            case 5:
                registrar_missao(moradores)
            case 6:
                print("\nRanking comunitário")
            case 7:
                print("\nConfirmar segurança")
            case 8:
                print("\nPainel da Defesa Civil")
            case 0:
                executando = False
                print("\nAté logo! Prevenção é hábito coletivo.")
          
        if executando:        
          pausar()
          
if __name__ == "__main__":
    main()