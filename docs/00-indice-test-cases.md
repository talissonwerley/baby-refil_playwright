# Índice de Test Cases - BabyRefil E2E

Este documento contém o índice completo de todos os test cases mapeados para cobertura E2E do site BabyRefil.

## 📊 Resumo Geral

- **Total de Test Cases:** 60
- **Testes de Navegação:** 14 test cases
- **Testes de FAQ:** 8 test cases
- **Testes de Planos:** 10 test cases
- **Testes de Assinatura (Fluxo Completo):** 28 test cases

---

## 📁 Organização dos Test Cases

### 1. Navegação e Interface
**Arquivo:** `01-test-cases-navegacao.md`

Cobre navegação pela página inicial, menu, seções e elementos visuais básicos.

**Test Cases:**
- CT001 - Acessar página inicial do BabyRefil
- CT002 - Navegação pelo menu: Como Funciona
- CT003 - Navegação pelo menu: Planos
- CT004 - Navegação pelo menu: FAQ
- CT005 - Navegação pelo logo para página inicial
- CT006 - Navegação pelo botão "Assinar Agora" do header
- CT007 - Navegação pelo botão "Assinar Agora" do hero
- CT008 - Navegação pelo botão "Ver Planos" do hero
- CT009 - Navegação pelo botão "Assinar agora" da seção de planos
- CT010 - Validação de elementos da seção Hero
- CT011 - Validação de elementos da seção "Como Funciona"
- CT012 - Validação de elementos da seção de Marcas
- CT013 - Validação do Footer
- CT014 - Responsividade do menu de navegação

---

### 2. FAQ (Perguntas Frequentes)
**Arquivo:** `02-test-cases-faq.md`

Cobre funcionalidades do accordion do FAQ, expansão/colapso e exibição de respostas.

**Test Cases:**
- CT015 - Exibir resposta ao clicar na primeira pergunta do FAQ
- CT016 - Fechar accordion do FAQ ao clicar novamente
- CT017 - Exibir resposta "Posso alterar meu plano ou a frequência?"
- CT018 - Exibir resposta "Quais são as formas de pagamento?"
- CT019 - Exibir resposta "Como funciona a entrega?"
- CT020 - Exibir resposta "E se eu quiser cancelar?"
- CT021 - Múltiplos accordions abertos simultaneamente
- CT022 - Todas as perguntas do FAQ estão visíveis

---

### 3. Planos de Assinatura
**Arquivo:** `03-test-cases-planos.md`

Cobre visualização, comparação e seleção dos três planos disponíveis.

**Test Cases:**
- CT023 - Visualizar detalhes do Plano Essencial na página inicial
- CT024 - Visualizar detalhes do Plano Conforto na página inicial
- CT025 - Visualizar detalhes do Plano Completo na página inicial
- CT026 - Visualizar todos os três planos na página inicial
- CT027 - Visualizar planos na página de assinatura
- CT028 - Selecionar Plano Essencial na página de assinatura
- CT029 - Selecionar Plano Conforto na página de assinatura
- CT030 - Selecionar Plano Completo na página de assinatura
- CT031 - Alterar seleção de plano (trocar de plano selecionado)
- CT032 - Comparar preços e benefícios dos planos

---

### 4. Fluxo de Assinatura Completo
**Arquivo:** `04-test-cases-assinatura.md`

Cobre todo o fluxo de assinatura desde a seleção do plano até a etapa de pagamento, incluindo todas as validações.

**Test Cases:**

#### Etapa 1: Seleção de Plano
- CT033 - Acessar página de assinatura
- CT034 - Validar indicador de progresso na etapa 1

#### Etapa 2: Frequência de Entrega
- CT035 - Selecionar frequência Quinzenal
- CT036 - Selecionar frequência Mensal
- CT037 - Alternar entre frequências
- CT038 - Botão Voltar retorna para etapa 1
- CT039 - Avançar para etapa 3 sem selecionar frequência

#### Etapa 3: Dados Pessoais e Endereço
- CT040 - Validar campos de Dados Pessoais
- CT041 - Validar campos de Dados do Bebê
- CT042 - Validar campos de Endereço de Entrega
- CT043 - Preencher campo Nome Completo
- CT044 - Preencher campo E-mail
- CT045 - Validar formato de e-mail inválido
- CT046 - Preencher campo Telefone
- CT047 - Preencher campo Nome do Bebê
- CT048 - Selecionar Idade do Bebê no combobox
- CT049 - Buscar endereço por CEP
- CT050 - Validar CEP inválido
- CT051 - Preencher campo Número do endereço
- CT052 - Preencher campo Complemento (opcional)
- CT053 - Botão Voltar retorna para etapa 2
- CT054 - Validação de campos obrigatórios
- CT055 - Avançar para etapa 4 com todos os dados preenchidos

#### Etapa 4: Pagamento
- CT056 - Validar exibição da etapa de Pagamento

#### Fluxos Completos E2E
- CT057 - Fluxo completo: Assinatura do Plano Essencial
- CT058 - Fluxo completo: Assinatura do Plano Conforto (Quinzenal)
- CT059 - Fluxo completo: Assinatura do Plano Completo
- CT060 - Validar persistência de dados ao navegar entre etapas

---

## 🎯 Priorização de Testes

### Alta Prioridade (Smoke Tests / Critical Path)
Testes essenciais que validam o fluxo principal:

- CT001, CT006, CT007, CT009, CT027, CT028, CT029, CT030
- CT033, CT035, CT036, CT040, CT041, CT042
- CT057, CT058, CT059

### Média Prioridade (Functional Tests)
Testes que validam funcionalidades importantes:

- CT002, CT003, CT004, CT005, CT008, CT010, CT011
- CT015, CT016, CT017, CT018, CT019, CT020
- CT031, CT034, CT037, CT038, CT043, CT044, CT048, CT049
- CT053, CT060

### Baixa Prioridade (Visual/Edge Cases)
Testes de elementos visuais e casos extremos:

- CT012, CT013, CT014, CT021, CT022
- CT032, CT052

---

## 📝 Notas de Implementação

### Estrutura de Páginas Mapeadas

1. **Página Inicial (`/`)**
   - Hero section
   - Seção "Como Funciona"
   - Seção de Planos
   - Seção de Marcas
   - FAQ
   - Footer

2. **Página de Assinatura (`/subscribe`)**
   - Etapa 1: Seleção de Plano
   - Etapa 2: Frequência de Entrega
   - Etapa 3: Dados (Pessoais, Bebê, Endereço)
   - Etapa 4: Pagamento

### Localizadores Prioritários

Conforme especificado no prompt, usar a seguinte hierarquia:

1. `get_by_role()` - Sempre que possível
2. `get_by_label()` - Para inputs
3. `get_by_placeholder()` - Quando label não disponível
4. `get_by_text()` - Para texto visível e estável
5. `get_by_test_id()` - Apenas como último recurso

### Padrões de Teste

- Cada teste deve ser independente
- Usar fixtures do `conftest.py` para página isolada
- Adicionar checkpoints em pontos críticos
- Usar asserções nativas do Playwright com auto-retry
- Não usar timeouts desnecessários

---

## 🔄 Próximos Passos

1. Implementar testes de navegação (CT001-CT014)
2. Implementar testes de FAQ (CT015-CT022)
3. Implementar testes de planos (CT023-CT032)
4. Implementar testes de assinatura (CT033-CT060)
5. Criar Page Objects para reutilização
6. Executar suite completa e validar cobertura

---

## 📚 Documentação Adicional

- Ver `prompts/sdet-automator.prompt.md` para regras de desenvolvimento
- Ver `README.md` para configuração do projeto
- Ver `conftest.py` para configuração de fixtures



