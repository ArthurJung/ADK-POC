# AI Shopping Assistant - Google ADK POC

Assistente de compras inteligente construido com **Google ADK (Agent Development Kit)** e **Streamlit**. O agente utiliza o modelo Gemini para atender clientes de um e-commerce, respondendo perguntas sobre produtos, rastreando pedidos, explicando especificacoes tecnicas e direcionando o usuario ao suporte humano quando necessario.

## Como executar

### Pre-requisitos

- Python 3.10+
- Uma chave de API do Google Gemini (obtenha em [Google AI Studio](https://aistudio.google.com))

### Passo a passo

1. Clone o repositorio e entre na pasta do projeto:

```bash
git clone <url-do-repositorio>
cd ADK-POC
```

2. Crie e ative um ambiente virtual (recomendado):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

3. Instale as dependencias:

```bash
pip install -r requirements.txt
```

4. Configure a chave de API. Copie o arquivo de exemplo e preencha com sua chave:

```bash
cp .env.example .env
```

Edite o `.env` e substitua o valor de `GOOGLE_API_KEY` pela sua chave real.

5. Execute a aplicacao:

```bash
streamlit run app.py
```

A interface abrira automaticamente no navegador em `http://localhost:8501`.

## Arquitetura do projeto

```
ADK-POC/
  agent.py      -> Fabrica do agente, system prompt e 5 funcoes-ferramenta
  app.py        -> Interface de chat com Streamlit e ponte async/sync para o ADK
  config.py     -> Constantes: nomes, modelo (gemini-2.5-flash), configuracoes de UI
  mock_data.py  -> Dados simulados de produtos, pedidos e departamentos de suporte
  .env.example  -> Template para a chave de API
  requirements.txt
```

**Fluxo de uma requisicao:**
Usuario digita no chat (Streamlit) -> `app.py` cria um `InMemoryRunner` -> o agente ADK decide qual ferramenta chamar -> a ferramenta consulta os dicionarios de `mock_data.py` -> a resposta e transmitida de volta para a UI.

## Processo de pensamento: como cheguei neste agente

### 1. Definicao do problema

O ponto de partida foi uma pergunta pratica: **como seria um assistente de IA util para um e-commerce?** Ao inves de criar um chatbot generico, o objetivo era construir um agente que pudesse realmente executar acoes — buscar produtos, verificar status de pedidos, explicar termos tecnicos e escalar para um humano quando necessario.

### 2. Escolha do framework: Google ADK

O Google ADK foi escolhido por oferecer uma abstracao limpa para agentes com **tool-calling**. O conceito central e simples:

- Voce define um **agente** com um prompt de sistema e uma lista de **ferramentas** (funcoes Python comuns).
- O modelo LLM (Gemini) decide automaticamente **quando e qual ferramenta chamar** com base na mensagem do usuario.
- O ADK gerencia o ciclo de execucao: recebe a mensagem, chama a ferramenta, injeta o resultado de volta no contexto e gera a resposta final.

Isso elimina a necessidade de escrever logica complexa de roteamento — o proprio modelo faz a orquestracao.

### 3. Design das ferramentas (tools)

Cada capacidade do agente foi modelada como uma funcao Python independente:

| Ferramenta | Responsabilidade |
|---|---|
| `search_products` | Busca por palavra-chave no catalogo, com filtro opcional de categoria |
| `get_product_details` | Retorna ficha completa de um produto por ID |
| `check_order_status` | Consulta status e rastreamento de um pedido |
| `redirect_to_human_support` | Direciona para o departamento de suporte correto |
| `redirect_to_product_page` | Gera link para visualizar ou comprar um produto |

**Convencao importante:** todas as ferramentas retornam um `dict` com uma chave `"status"` (`"found"`, `"not_found"`, `"success"`, `"redirected"`). Isso padroniza a comunicacao entre ferramenta e agente, facilitando para o modelo interpretar o resultado.

### 4. System prompt: o comportamento do agente

O prompt de sistema foi escrito para definir tres coisas:

- **O que o agente pode fazer** — buscar produtos, explicar specs, rastrear pedidos, encaminhar ao suporte.
- **Como ele deve responder** — de forma amigavel, concisa, usando analogias para termos tecnicos, nunca inventando dados.
- **Limites rigidos** — o agente so responde sobre compras e produtos. Qualquer pergunta fora de topico (politica, receitas, codigo, etc.) e educadamente recusada. Isso evita que o agente seja usado de formas nao previstas.

A regra de escalacao tambem e explicita: se o cliente estiver frustrado ou pedir um humano, o agente usa a ferramenta `redirect_to_human_support`.

### 5. Dados simulados como camada de dados

Para manter o POC simples e sem dependencias externas (banco de dados, APIs), todos os dados vivem em dicionarios Python dentro de `mock_data.py`. Isso inclui:

- **18 produtos** em 9 categorias (ar-condicionado, TVs, smartphones, notebooks, fones, geladeiras, tablets, cameras, aspiradores-robo, calcados)
- **3 pedidos** em estados diferentes (enviado, processando, entregue)
- **5 departamentos de suporte** com contatos fictcios

Em uma versao de producao, essas funcoes seriam substituidas por chamadas a APIs reais ou consultas a banco de dados, sem alterar a interface das ferramentas.

### 6. Interface com Streamlit

O Streamlit foi escolhido por permitir criar uma interface de chat funcional com poucas linhas de codigo. O `app.py` gerencia:

- **Estado da sessao** — historico de mensagens, instancia do runner e ID da sessao ADK.
- **Ponte async/sync** — o ADK usa `async`, mas o Streamlit e sincrono, entao usamos `asyncio.run()` para fazer a ponte.
- **Streaming de resposta** — o runner itera sobre eventos, concatenando as partes de texto ate formar a resposta completa.

### 7. Decisoes conscientes de escopo

Algumas decisoes foram tomadas para manter o POC focado:

- **Sem banco de dados** — dados em memoria sao suficientes para demonstrar o conceito.
- **Sem autenticacao** — a identidade do usuario e fixa (`"web_user"`).
- **Sem testes automatizados** — o foco foi na arquitetura do agente, nao na cobertura de testes.
- **Modelo unico** — sem multi-agent ou sub-agents. Um unico agente com todas as ferramentas e suficiente para este escopo.

Cada uma dessas simplificacoes pode ser expandida conforme o projeto evolui para producao.

## Tecnologias utilizadas

- **[Google ADK](https://google.github.io/adk-docs/)** — framework para construcao de agentes com tool-calling
- **[Gemini 2.5 Flash](https://ai.google.dev/)** — modelo LLM do Google
- **[Streamlit](https://streamlit.io/)** — framework para interfaces web em Python
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — carregamento de variaveis de ambiente
