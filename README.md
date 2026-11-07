<div align="center">

# 🌧️ GUARDIÕES JF

### Motor lógico do sistema de alertas e gamificação comunitária

**Challenge N/ Lugares Futuros · Sprint 2 · Computational Thinking with Python**

📍 _Juiz de Fora/MG, depois das chuvas de fevereiro de 2026_

</div>

---

## 📖 Sobre o projeto

Em fevereiro de 2026, Juiz de Fora recebeu **584 mm de chuva** em um mês e perdeu **66 vidas**. O risco já era conhecido: um ano antes, o Cemaden havia alertado que cerca de 130 mil pessoas viviam em áreas de risco na cidade. A pesquisa do nosso grupo mostrou que o problema não foi só a falta de aviso. Mesmo quando o alerta chega, ele **não diz para onde ir**.

O **GUARDIÕES JF** é um programa de terminal que simula as regras centrais da nossa solução:

- 🚨 classifica o risco de cada bairro a partir da chuva e do nível da água;
- 🧭 mostra o que fazer, qual é o abrigo mais próximo e qual rua evitar;
- 🎮 transforma a prevenção em missões com pontos e ranking entre bairros;
- 🛡️ registra quem já chegou ao abrigo e mostra à Defesa Civil quem ainda falta.

> 💡 Na Sprint 1, a Matriz GUTO colocou o **alerta multicanal com orientação** em 1º lugar (240 pontos). Por isso, o coração deste programa é a regra que transforma uma leitura de chuva em um alerta que diz para onde ir.

> ⚠️ **Todos os dados são simulados.** Limiares, abrigos, distâncias e ruas são exemplos e não são dados oficiais da Defesa Civil. Os bairros são os mais atingidos em fevereiro de 2026, segundo a pesquisa do grupo.

---

## 👥 Integrantes – Grupo Digital Nomads

| 👤 Nome completo                          | 🆔 RM    |
| ----------------------------------------- | -------- |
| Anne Bortoli                              | RM574750 |
| Débora Gonçalves da Silva                 | RM575926 |
| Gabriel Almeida                           | RM575525 |
| Pedro Paulo Carvalho Coutinho             | RM575957 |
| Vanessa Santos Martins de Lima Nascimento | RM576450 |

**Turma:** 1ESSRQ-2026

---

## ▶️ Como executar

**Requisito:** Python 3.10 ou superior. Nenhuma biblioteca externa é necessária.

```bash
# 🪟 Windows
python main.py

# 🐧 Linux / 🍎 macOS
python3 main.py
```

Para conferir a versão instalada, use `python --version`.

---

## 🗂️ Funcionalidades do menu

As funcionalidades cobrem os quatro temas do nosso Diagrama de Afinidades da Sprint 1:

|                🔔 Alertar                 |               🧭 Orientar                |         🎮 Engajar          |             📊 Gerir             |
| :---------------------------------------: | :--------------------------------------: | :-------------------------: | :------------------------------: |
| O alerta não chega ou chega sem confiança | Mesmo avisado, ninguém sabe para onde ir | A prevenção não vira hábito | O dado existe, mas não vira ação |

| Opção | Funcionalidade                                  | Tema                     |
| :---: | ----------------------------------------------- | ------------------------ |
|  1️⃣   | Registrar leitura e classificar risco do bairro | 🔔 Alertar · 🧭 Orientar |
|  2️⃣   | Relatório de chuvas da semana                   | 📊 Gerir                 |
|  3️⃣   | Consultar abrigo do meu bairro                  | 🧭 Orientar              |
|  4️⃣   | Cadastrar morador                               | 🎮 Engajar               |
|  5️⃣   | Registrar missão de prevenção                   | 🎮 Engajar               |
|  6️⃣   | Ranking comunitário                             | 🎮 Engajar               |
|  7️⃣   | Confirmar que estou em segurança                | 🧭 Orientar · 📊 Gerir   |
|  8️⃣   | Painel da Defesa Civil                          | 📊 Gerir                 |
|  0️⃣   | Sair                                            | –                        |

Ao fim de cada funcionalidade, o programa espera o Enter e volta ao menu.

### 1️⃣ Registrar leitura e classificar risco

O usuário escolhe o bairro e o dia e digita a chuva (mm nas últimas 24 h) e o nível da água do córrego (cm). O programa grava a chuva na matriz, classifica o risco e mostra o **cartão de alerta** na mesma ordem do design system da Sprint 1: nível, o que fazer agora, abrigo mais próximo com a distância e, em ALERTA ou EMERGÊNCIA, a rua a evitar.

Também informa quantos moradores do bairro foram avisados por 📱 push/SMS e quantos por 📞 ligação de voz, para incluir quem não tem smartphone.

### 2️⃣ Relatório de chuvas da semana

Percorre a matriz **bairros × dias** e mostra, para cada bairro, o total, a média, o maior e o menor valor. No resumo aparecem a chuva somada, a média por bairro, o maior e o menor acumulado, o dia mais chuvoso e os bairros com 🟤 **solo encharcado** (acumulado a partir de 150 mm), que têm mais risco de deslizamento.

### 3️⃣ Consultar abrigo

O morador escolhe o bairro pelo número e vê a situação atual, o 🏫 abrigo de referência com a distância e a 🚫 rua a evitar.

### 4️⃣ Cadastrar morador

Nome (só letras, sem repetir um nome já cadastrado), bairro e se tem smartphone. O canal de alerta é definido a partir disso.

### 5️⃣ Registrar missão de prevenção

Cada missão tem pontos e um motivo prático ligado à prevenção:

| 🎯 Missão                             | ⭐ Pontos | 💬 Por quê                                  |
| ------------------------------------- | :-------: | ------------------------------------------- |
| Registrar bueiro entupido na sua rua  |    +40    | Bueiro entupido alaga a rua na chuva        |
| Descartar o lixo só no dia da coleta  |    +20    | Lixo na rua entope a drenagem               |
| Plantar uma muda em área de encosta   |    +50    | As raízes ajudam a segurar o solo           |
| Conferir a rota até o seu abrigo      |    +30    | Na hora do alerta, não dá tempo de procurar |
| Participar do simulado de evacuação   |    +60    | Quem já treinou sai mais rápido             |
| Avisar um vizinho sem celular (vigia) |    +30    | Quem não tem smartphone depende de alguém   |

### 6️⃣ Ranking comunitário

🏆 Ranking individual e ranking de bairros (soma dos pontos dos moradores), ordenados com um algoritmo de **ordenação por seleção** feito com laços `for`. O bairro em 1º lugar vira o destaque da semana.

### 7️⃣ Confirmar que estou em segurança

Disponível só para moradores de bairros em ALERTA ou EMERGÊNCIA. A confirmação ✅ atualiza o painel da Defesa Civil.

### 8️⃣ Painel da Defesa Civil

Mostra o nível de risco de cada bairro, quantos moradores confirmaram nos bairros em evacuação e a lista de pendentes. Quem não tem celular aparece marcado para ser procurado por um 🙋 **vigia de bairro**.

---

## 🚦 Regra de classificação de risco

Vale o **pior dos dois indicadores** (chuva ou nível da água):

| Nível             | 🌧️ Chuva em 24 h   | 🌊 Nível da água   |
| ----------------- | ------------------ | ------------------ |
| 🟢 **NORMAL**     | menos de 30 mm     | menos de 120 cm    |
| 🟡 **ATENÇÃO**    | a partir de 30 mm  | a partir de 120 cm |
| 🟠 **ALERTA**     | a partir de 60 mm  | a partir de 200 cm |
| 🔴 **EMERGÊNCIA** | a partir de 100 mm | a partir de 300 cm |

> 🔄 Quando um bairro entra em ALERTA ou EMERGÊNCIA, as confirmações de segurança desse bairro são zeradas, para a contagem começar de novo.

---

## 🤝 Decisões do grupo

| Decisão                                        | Motivo                                                                                                                 |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 🔢 Bairro escolhido por número, e não digitado | Evita erros de digitação e acento. Na hora da chuva, tocar num número é mais rápido do que escrever um nome.           |
| 🚫 Sem pontos na confirmação de segurança      | A gamificação fica restrita à prevenção, antes da chuva. Recompensar alguém durante uma emergência não seria adequado. |
| 📋 Orientação em passos numerados              | Responde à dor principal da pesquisa: o alerta oficial informa o risco, mas não diz o que fazer nem para onde ir.      |
| 🙋 Canal humano para quem não tem celular      | Moradores sem smartphone são avisados por ligação de voz e aparecem no painel para o vigia de bairro.                  |

---

## ✅ Como o código atende aos requisitos

| Requisito                            | Onde está no código                                                                                                                                                                |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔁 Menu com `while`                  | `main()`: laço `while executando` com `match-case` nas opções                                                                                                                      |
| ⚖️ Regras de negócio                 | `classificar_risco()` com `if/elif/else` e `obter_orientacao()` com `match-case`                                                                                                   |
| 🛡️ Validação de entradas             | `ler_inteiro()` (com `isdigit()` e faixa), `ler_texto()` e `ler_sim_nao()` repetem a pergunta até o valor ser válido                                                               |
| 📝 Listas                            | bairros, abrigos, distâncias, ruas, dias, missões, moradores, níveis da água e riscos                                                                                              |
| 🧮 Matriz                            | `criar_matriz_chuvas()`: 8 bairros × 7 dias com chuva em mm                                                                                                                        |
| ⏭️ `break` e `continue`              | `break` em `buscar_morador()` e `cadastrar_morador()`; `continue` em `ler_inteiro()`, `contar_moradores_bairro()`, `relatorio_chuvas()`, `exibir_ranking()` e `painel_evacuacao()` |
| 📈 Totais, médias, maior e menor     | `calcular_estatisticas()` e `relatorio_chuvas()`                                                                                                                                   |
| 🧩 Funções com parâmetros e `return` | ex.: `classificar_risco(chuva_mm, nivel_cm)`, `calcular_estatisticas(valores)`, `registrar_missao(moradores)` e `ordenar_ranking(itens)`                                           |
| ✨ f-strings e PEP 8                 | todas as saídas usam f-string, e o arquivo passa no `pycodestyle`                                                                                                                  |

---

## 🏗️ Organização do código

O arquivo `cidade_resiliente.py` é dividido em seções:

| Seção                             | Conteúdo                                                                                                                                                                           |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️ Constantes do sistema          | níveis de risco, limiares, bairros, abrigos, ruas, dias e missões                                                                                                                  |
| 🗃️ Criação dos dados iniciais     | `criar_matriz_chuvas()` e `criar_moradores()`                                                                                                                                      |
| 🛡️ Funções de entrada (validação) | `ler_inteiro()`, `ler_texto()`, `ler_sim_nao()` e `pausar()`                                                                                                                       |
| 🔧 Funções auxiliares             | `escolher_bairro()`, `contar_moradores_bairro()`, `calcular_estatisticas()`, `buscar_morador()`, `escolher_morador()`, `ordenar_ranking()` e `bairros_em_alerta()`                 |
| ⚖️ Regras de negócio              | `classificar_risco()`, `obter_orientacao()` e `exibir_cartao_alerta()`                                                                                                             |
| 🧭 Funcionalidades do menu        | `registrar_leitura()`, `relatorio_chuvas()`, `consultar_abrigo()`, `cadastrar_morador()`, `registrar_missao()`, `exibir_ranking()`, `confirmar_seguranca()` e `painel_evacuacao()` |
| 🏠 Menu principal                 | `exibir_menu()` e `main()`                                                                                                                                                         |

### 🧱 Estrutura dos dados

- **Listas paralelas de bairros:** a posição `i` de `BAIRROS`, `ABRIGOS`, `DISTANCIAS_ABRIGO_M` e `RUAS_EVITAR` se refere ao mesmo bairro.
- **Matriz de chuvas:** `chuvas[bairro][dia]`.
- **Moradores:** lista de listas no formato `[nome, índice do bairro, pontos, tem celular, confirmou segurança]`. As constantes `NOME`, `BAIRRO`, `PONTOS`, `TEM_CELULAR` e `CONFIRMOU` dão nome a cada posição, para o código ficar legível.
- **Missões:** lista de listas no formato `[nome, pontos, motivo]`.

---

## 🧪 Roteiro sugerido para testar

1. 🏆 **Opção 6:** veja o ranking inicial, com a Fernanda em 1º e o Parque Burnier como bairro destaque.
2. 🚨 **Opção 1:** Parque Burnier, dia 7 (Dom), 120 mm e 150 cm. O resultado é 🔴 EMERGÊNCIA, com os passos, o abrigo e a rua a evitar.
3. 📊 **Opção 8:** o painel mostra o Parque Burnier com `0/3` confirmados e o Joaquim marcado para o vigia de bairro.
4. ✅ **Opção 7:** confirme a Cláudia. Depois volte à opção 8 e veja `1/3`.
5. 🌧️ **Opção 2:** o domingo do Parque Burnier aparece com 120 mm, o total do bairro vai para 242 mm e ele entra na lista de solo encharcado.
6. 🎯 **Opção 5:** registre uma missão e veja a mudança no ranking da opção 6.
7. 🛡️ **Entradas inválidas:** teste letras, `-1`, `12.5` e a opção 9. O programa pede de novo e não fecha.

---

## 🔭 Limitações e próximas sprints

- 💾 Os dados ficam só na memória: ao fechar o programa, tudo volta ao estado inicial.
- 📡 Não há sensores nem APIs. Na disciplina de Edge Computing, as leituras virão de pluviômetros e sensores de nível.
- 📅 A classificação usa a chuva de 24 h. O acumulado da semana aparece apenas como aviso no relatório.

---

## 🤖 Uso de IA

Usamos IA generativa (Claude, da Anthropic) como apoio na construção do código e da documentação. Todos os prompts estão no arquivo [`PROMPTS.md`](PROMPTS.md), junto com as decisões que o grupo tomou a partir das respostas.

---

<div align="center">

_"Juiz de Fora provou que saber que a chuva vem não salva ninguém. Salva quem age."_

**Digital Nomads · 2026** 🌱

</div>
