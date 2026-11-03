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

def main():
    print(30*"=")
    print("Bem-vindo ao Guardiões JF!")
    print(30*"=")

# Boa Prática. faz o main() rodar só quando vocês executam o arquivo diretamente.
if __name__ == "__main__":
    main()