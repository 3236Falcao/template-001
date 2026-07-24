# AGENTS.md

# MIM Template - Guia para Agentes de IA

## Contexto

Este projeto foi criado a partir do MIM Template.

O objetivo do MIM é acelerar a construção de protótipos para validar hipóteses.

O foco não é construir o software definitivo.

---

# Objetivo

Construa a menor solução funcional possível para validar o problema proposto.

Evite adicionar funcionalidades que não contribuam diretamente para essa validação.

---

# Regras de desenvolvimento

Antes de modificar qualquer código:

1. Analise a estrutura existente.
2. Reutilize arquivos sempre que possível.
3. Crie novos arquivos apenas quando houver necessidade.
4. Não reorganize a arquitetura sem motivo.
5. Não implemente funcionalidades "porque poderão ser úteis".

---

# Filosofia

Prefira:

- simplicidade;
- legibilidade;
- rapidez de desenvolvimento;
- baixo acoplamento.

Evite:

- abstrações prematuras;
- padrões complexos;
- dependências desnecessárias.

---

# Estrutura

A estrutura inicial do template já existe.

Ela deve ser utilizada como ponto de partida.

Não recrie a estrutura.

---

# Evolução

Extraia componentes somente quando:

- houver duplicação;
- o código perder legibilidade;
- existir ganho claro de manutenção.

---

# Persistência

Não adicione banco de dados sem solicitação explícita.

Utilize memória da aplicação ou arquivos simples enquanto o protótipo estiver sendo validado.

---

# Dependências

Antes de instalar qualquer biblioteca:

Pergunte:

"Isso realmente é necessário para validar este protótipo?"

Se a resposta for não, não instale.

---

# Critério de sucesso

O protótipo resolve o problema?

Se sim, pare de desenvolver.

A próxima etapa pertence ao projeto, não ao protótipo.
