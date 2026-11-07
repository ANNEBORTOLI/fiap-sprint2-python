# Prompts de IA utilizados

Projeto: **Guardiões JF – Motor Lógico (Sprint 2)** · Grupo Digital Nomads  
Ferramenta: Claude (Anthropic), via claude.ai.

Contexto enviado no início: materiais da Sprint 1 (Storytelling, Front-End Design,
Canvas da Proposta de Valor) e as regras do Challenge 2026.

## Como usamos a IA

Usamos a IA como apoio para organizar a lógica, tirar dúvidas de estrutura e validar decisões.
O grupo sempre decidia o que manter, o que simplificar e a ordem dos commits.
Pedimos explicações e adaptamos cada parte antes de avançar.

---

## Prompt 1 – Levantamento inicial dos dados

> Com base na nossa entrega da Sprint 1, faça uma lista dos bairros mais afetados pelas chuvas de fevereiro de 2026.

**Resultado:** a IA sugeriu bairros. O grupo escolheu e manteve: Parque Burnier, Três Moinhos, Santa Rita, Costa Carvalho e Industrial.

---

## Prompt 2 – Abrigos

> Agora crie uma lista com nomes aleatórios de possíveis abrigos para cada bairro.

**Resultado:** a IA gerou nomes. O grupo adaptou para locais reais do município (escolas e ginásios).

---

## Prompt 3 – Classificação de risco

> Com base em dados públicos de chuvas, crie um ranking para níveis de atenção, alerta e emergência.

**Resultado:** a IA sugeriu faixas. O grupo ajustou os valores (50 / 100 / 150 mm e cm) e registrou que os limites ainda precisam ser validados com a Defesa Civil.

---

## Prompt 4 – Ruas a evitar

> Crie uma lista com nomes de ruas que tenha 8 posições.

**Resultado:** a IA gerou 8 nomes. O grupo reduziu para 5 (um por bairro) e deixou descrições mais realistas (encosta, córrego, viaduto etc.).

---

## Prompt 5 – Validação de entrada

> Como posso garantir que apenas inteiros sejam digitados? Me mostre todas as possibilidades além do `isdigit()`.

**Resultado:** a IA mostrou várias abordagens (`try/except`, `str.isdigit()`, checagem de faixa etc.). O grupo optou por `isdigit()` + laço de repetição, por ser mais simples.

---

## Prompt 6 – Organização do código

> Meu código está ficando muito desorganizado. Me ajude a organizar criando comentários.  
> Não crie outros arquivos. Apenas observe o que está no `main.py` e me diga como posso organizar melhor.

**Resultado:** a IA sugeriu seções com comentários de cabeçalho (constantes, dados, funções de apoio, regras de negócio, opções do menu e main). O grupo aplicou essa organização.

---

## Prompt 7 – Formatação da tabela do painel

> Preciso criar uma tabela a partir da função abaixo que faz a leitura de matrizes.  
> Me ajude a deixar visivelmente atraente para o leitor.

**Resultado:** a IA mostrou formatação com f-string e alinhamento (`:<` e `:>`). O grupo adotou o formato atual do painel da Defesa Civil.

---

## Prompt 8 – Espaçamento do menu

> Onde posso modificar meu código para que o menu não fique colado com os retornos do `match`?

**Resultado:** a IA indicou o uso de `input("\nPressione ENTER para voltar ao menu...")` após cada opção. O grupo incluiu essa pausa.

---

## Demais prompts (dúvidas de lógica e decisões)

| Nº  | Prompt (resumo)                                                                                                                                           | O que o grupo decidiu / aprendeu                                  |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 9   | “Explique a diferença entre `break` e `continue` com um exemplo do nosso contexto (fila de check-in).”                                                    | Usamos `continue` para pular quem já confirmou.                   |
| 10  | “Como montar a função que classifica o risco? A regra é: o pior critério entre chuva e nível vale.”                                                       | Implementamos `classificar_risco` com if/elif.                    |
| 11  | “Não quero símbolo de risco, só o nome do nível.”                                                                                                         | Removemos os símbolos.                                            |
| 12  | “Como calcular total, média, maior e menor chuva de um bairro usando a matriz?”                                                                           | Criamos as funções de estatística.                                |
| 13  | “A busca por nome do bairro está complicando. Não é melhor o usuário escolher por número? Evita erros já conseguimos usar funções auxiliares já criadas.” | Trocamos pela função `escolher_bairro`.                           |
| 14  | “Na confirmação de segurança, faz sentido dar pontos? Estamos em emergência. Creio que a gamificação deve parar.”                                         | Decidimos **não** pontuar o check-in (RN03).                      |
| 15  | “Como impedir que a mesma missão seja pontuada duas vezes na semana?”                                                                                     | Criamos a lista `missoes_cumpridas` e a verificação.              |
| 16  | “Mostre só a parte do ranking: como ordenar os moradores por pontos e calcular a média por bairro.”                                                       | Implementamos o ranking com `sorted` e a média por morador ativo. |
| 17  | “O menu com `match-case` está correto? O programa volta ao menu depois de cada opção?”                                                                    | Ajustamos o `main` e a pausa.                                     |

---

## Observações finais do grupo

- A IA nunca entregou o programa final de uma vez. Cada funcionalidade foi pedida, explicada e adaptada.
- Várias ideias da IA foram rejeitadas ou simplificadas (lista de 8 ruas, pontos no check-in, símbolos de risco, pontuação em emergência etc.).
- O código final reflete as regras de negócio definidas pelo grupo na Sprint 1 e as decisões tomadas ao longo dos commits.
