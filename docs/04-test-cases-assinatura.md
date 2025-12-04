# Test Cases - Fluxo de Assinatura Completo

## CT033 - Acessar página de assinatura

**Prioridade:** Alta  
**Tipo:** Navigation Test  
**Objetivo:** Validar acesso à página de assinatura

### Pré-condições
- Navegador aberto

### Passos
1. Acessar URL: `https://babyrefil.vercel.app/subscribe`

### Resultados Esperados
- Página de assinatura carrega
- Indicador de progresso está visível mostrando 4 etapas:
  - 1. Plano
  - 2. Recorrência
  - 3. Dados
  - 4. Pagamento
- Etapa 1 (Plano) está ativa
- Seção de seleção de planos está visível

### Localizadores Sugeridos
- `page.get_by_role("heading", name="Escolha o seu plano")`
- `page.get_by_text("1")` (indicador de progresso)

---

## CT034 - Validar indicador de progresso na etapa 1

**Prioridade:** Média  
**Tipo:** Visual Test  
**Objetivo:** Validar estado inicial do indicador de progresso

### Pré-condições
- Estar na página de assinatura
- Etapa 1 (Plano) está ativa

### Passos
1. Verificar indicador de progresso

### Resultados Esperados
- 4 etapas estão visíveis numeradas (1, 2, 3, 4)
- Etapa 1 marcada como ativa/concluída (ícone ou visual diferente)
- Etapas 2, 3 e 4 estão desabilitadas/inativas
- Labels das etapas estão visíveis: "Plano", "Recorrência", "Dados", "Pagamento"

### Localizadores Sugeridos
- `page.get_by_text("Plano")`
- `page.get_by_text("Recorrência")`
- `page.get_by_text("Dados")`
- `page.get_by_text("Pagamento")`

---

## CT035 - Etapa 2: Selecionar frequência Quinzenal

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar seleção da frequência quinzenal de entrega

### Pré-condições
- Ter selecionado um plano na etapa 1
- Estar na etapa 2 (Frequência da Entrega)

### Passos
1. Verificar que a seção "Frequência da Entrega" está visível
2. Clicar no radio button "Quinzenal A cada 15 dias"
3. Verificar seleção

### Resultados Esperados
- Heading "Frequência da Entrega" está visível
- Descrição "Com que frequência você quer receber seus produtos?" está visível
- Radio button "Quinzenal" está selecionado
- Descrição "A cada 15 dias" está visível
- Radio button "Mensal" não está selecionado
- Botões "Voltar" e "Avançar" estão visíveis

### Localizadores Sugeridos
- `page.get_by_role("heading", name="Frequência da Entrega")`
- `page.get_by_role("radio", name="Quinzenal A cada 15 dias")`
- `page.get_by_role("button", name="Avançar")`

---

## CT036 - Etapa 2: Selecionar frequência Mensal

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar seleção da frequência mensal de entrega

### Pré-condições
- Ter selecionado um plano na etapa 1
- Estar na etapa 2 (Frequência da Entrega)

### Passos
1. Verificar opções de frequência
2. Clicar no radio button "Mensal A cada 30 dias"
3. Verificar seleção

### Resultados Esperados
- Radio button "Mensal" está selecionado
- Descrição "A cada 30 dias" está visível
- Radio button "Quinzenal" não está selecionado

### Localizadores Sugeridos
- `page.get_by_role("radio", name="Mensal A cada 30 dias")`

---

## CT037 - Etapa 2: Alternar entre frequências

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar que é possível alterar a frequência selecionada

### Pré-condições
- Estar na etapa 2 com uma frequência selecionada

### Passos
1. Selecionar frequência "Quinzenal"
2. Selecionar frequência "Mensal"
3. Selecionar novamente "Quinzenal"

### Resultados Esperados
- É possível alternar entre as frequências
- Apenas uma frequência fica selecionada por vez
- Não há erros ou conflitos

### Localizadores Sugeridos
- `page.get_by_role("radiogroup")`

---

## CT038 - Etapa 2: Botão Voltar retorna para etapa 1

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar navegação para trás na etapa 2

### Pré-condições
- Estar na etapa 2 (Frequência)

### Passos
1. Clicar no botão "Voltar"
2. Verificar transição

### Resultados Esperados
- Retorna para etapa 1 (Plano)
- Indicador de progresso mostra etapa 1 como ativa
- Seção de seleção de planos está visível
- Plano selecionado anteriormente permanece selecionado (se aplicável)

### Localizadores Sugeridos
- `page.get_by_role("button", name="Voltar")`
- `page.get_by_role("heading", name="Escolha o seu plano")`

---

## CT039 - Etapa 2: Avançar para etapa 3 sem selecionar frequência

**Prioridade:** Alta  
**Tipo:** Validation Test  
**Objetivo:** Validar validação de campo obrigatório

### Pré-condições
- Estar na etapa 2
- Nenhuma frequência selecionada (se possível)

### Passos
1. Tentar clicar em "Avançar" sem selecionar frequência

### Resultados Esperados
- Botão "Avançar" está desabilitado OU
- Mensagem de validação aparece solicitando seleção OU
- Não avança para próxima etapa

### Localizadores Sugeridos
- `page.get_by_role("button", name="Avançar")`

---

## CT040 - Etapa 3: Validar campos de Dados Pessoais

**Prioridade:** Alta  
**Tipo:** Visual Test  
**Objetivo:** Validar exibição dos campos de dados pessoais

### Pré-condições
- Ter selecionado plano e frequência
- Estar na etapa 3 (Dados)

### Passos
1. Verificar seção "Seus Dados"
2. Verificar campos de Dados Pessoais

### Resultados Esperados
- Heading "Seus Dados" está visível
- Descrição "Precisamos de algumas informações para criar sua assinatura." está visível
- Sub-heading "Dados Pessoais" está visível
- Campo "Nome Completo" está visível e habilitado
- Campo "E-mail" está visível e habilitado
- Campo "Telefone" está visível e habilitado

### Localizadores Sugeridos
- `page.get_by_role("heading", name="Seus Dados")`
- `page.get_by_role("heading", name="Dados Pessoais")`
- `page.get_by_label("Nome Completo")`
- `page.get_by_label("E-mail")`
- `page.get_by_label("Telefone")`

---

## CT041 - Etapa 3: Validar campos de Dados do Bebê

**Prioridade:** Alta  
**Tipo:** Visual Test  
**Objetivo:** Validar exibição dos campos de dados do bebê

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Verificar seção "Dados do Bebê"

### Resultados Esperados
- Sub-heading "Dados do Bebê" está visível
- Campo "Nome do Bebê" está visível e habilitado
- Campo "Idade do Bebê" (combobox) está visível e habilitado
- Placeholder "Selecione a faixa etária" está visível

### Localizadores Sugeridos
- `page.get_by_role("heading", name="Dados do Bebê")`
- `page.get_by_label("Nome do Bebê")`
- `page.get_by_label("Idade do Bebê")`

---

## CT042 - Etapa 3: Validar campos de Endereço de Entrega

**Prioridade:** Alta  
**Tipo:** Visual Test  
**Objetivo:** Validar exibição dos campos de endereço

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Verificar seção "Endereço de Entrega"

### Resultados Esperados
- Sub-heading "Endereço de Entrega" está visível
- Campo "CEP" está visível e habilitado
- Botão "Buscar" ao lado do CEP está visível
- Campo "Rua" está visível (inicialmente desabilitado)
- Campo "Número" está visível e habilitado
- Campo "Complemento (Opcional)" está visível e habilitado
- Campo "Bairro" está visível (inicialmente desabilitado)
- Campo "Cidade" está visível (inicialmente desabilitado)
- Campo "Estado" está visível (inicialmente desabilitado)

### Localizadores Sugeridos
- `page.get_by_role("heading", name="Endereço de Entrega")`
- `page.get_by_label("CEP")`
- `page.get_by_role("button", name="Buscar")`
- `page.get_by_label("Rua")`
- `page.get_by_label("Número")`
- `page.get_by_label("Complemento (Opcional)")`
- `page.get_by_label("Bairro")`
- `page.get_by_label("Cidade")`
- `page.get_by_label("Estado")`

---

## CT043 - Etapa 3: Preencher campo Nome Completo

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar preenchimento do campo Nome Completo

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Localizar campo "Nome Completo"
2. Preencher com um nome válido (ex: "Maria Silva")

### Resultados Esperados
- Campo aceita texto
- Valor digitado aparece no campo
- Campo permanece habilitado

### Localizadores Sugeridos
- `page.get_by_label("Nome Completo")`

---

## CT044 - Etapa 3: Preencher campo E-mail

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar preenchimento do campo E-mail

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Localizar campo "E-mail"
2. Preencher com um e-mail válido (ex: "maria.silva@email.com")

### Resultados Esperados
- Campo aceita texto
- Valor digitado aparece no campo
- Se houver validação em tempo real, aceita formato de e-mail válido

### Localizadores Sugeridos
- `page.get_by_label("E-mail")`

---

## CT045 - Etapa 3: Validar formato de e-mail inválido

**Prioridade:** Média  
**Tipo:** Validation Test  
**Objetivo:** Validar mensagem de erro para e-mail inválido

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Preencher campo "E-mail" com valor inválido (ex: "email-invalido")
2. Clicar fora do campo ou tentar avançar
3. Verificar mensagem de erro

### Resultados Esperados
- Mensagem de erro aparece indicando formato inválido OU
- Campo não aceita o valor OU
- Botão "Avançar" permanece desabilitado

### Localizadores Sugeridos
- `page.get_by_label("E-mail")`
- Mensagem de erro (se houver)

---

## CT046 - Etapa 3: Preencher campo Telefone

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar preenchimento do campo Telefone

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Localizar campo "Telefone"
2. Preencher com um telefone (ex: "(11) 98765-4321")

### Resultados Esperados
- Campo aceita texto
- Valor digitado aparece no campo
- Máscara de telefone pode ser aplicada automaticamente

### Localizadores Sugeridos
- `page.get_by_label("Telefone")`

---

## CT047 - Etapa 3: Preencher campo Nome do Bebê

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar preenchimento do campo Nome do Bebê

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Localizar campo "Nome do Bebê"
2. Preencher com um nome (ex: "João")

### Resultados Esperados
- Campo aceita texto
- Valor digitado aparece no campo

### Localizadores Sugeridos
- `page.get_by_label("Nome do Bebê")`

---

## CT048 - Etapa 3: Selecionar Idade do Bebê no combobox

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar seleção da idade do bebê

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Localizar combobox "Idade do Bebê"
2. Clicar no combobox
3. Verificar opções disponíveis
4. Selecionar uma opção

### Resultados Esperados
- Combobox é clicável
- Dropdown abre mostrando opções de faixa etária
- Opção selecionada aparece no combobox
- Placeholder desaparece após seleção

### Localizadores Sugeridos
- `page.get_by_label("Idade do Bebê")`

---

## CT049 - Etapa 3: Buscar endereço por CEP

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar funcionalidade de busca de endereço por CEP

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Preencher campo "CEP" com um CEP válido (ex: "01310-100")
2. Clicar no botão "Buscar"
3. Aguardar busca

### Resultados Esperados
- Botão "Buscar" está habilitado
- Ao buscar, campos de endereço são preenchidos automaticamente:
  - Rua é preenchida e habilitada
  - Bairro é preenchido e habilitado
  - Cidade é preenchida e habilitada
  - Estado é preenchido e habilitado
- Campos de endereço não ficam mais desabilitados

### Localizadores Sugeridos
- `page.get_by_label("CEP")`
- `page.get_by_role("button", name="Buscar")`
- `page.get_by_label("Rua")`

---

## CT050 - Etapa 3: Validar CEP inválido

**Prioridade:** Média  
**Tipo:** Validation Test  
**Objetivo:** Validar tratamento de CEP inválido

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Preencher campo "CEP" com valor inválido (ex: "00000-000" ou "123")
2. Clicar no botão "Buscar"
3. Verificar comportamento

### Resultados Esperados
- Mensagem de erro aparece indicando CEP inválido OU
- Campos de endereço não são preenchidos
- Mensagem informativa sobre CEP não encontrado

### Localizadores Sugeridos
- `page.get_by_label("CEP")`
- `page.get_by_role("button", name="Buscar")`

---

## CT051 - Etapa 3: Preencher campo Número do endereço

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar preenchimento do campo Número

### Pré-condições
- Estar na etapa 3 (Dados)
- CEP já buscado (endereço preenchido)

### Passos
1. Localizar campo "Número"
2. Preencher com um número (ex: "123")

### Resultados Esperados
- Campo aceita texto/números
- Valor digitado aparece no campo

### Localizadores Sugeridos
- `page.get_by_label("Número")`

---

## CT052 - Etapa 3: Preencher campo Complemento (opcional)

**Prioridade:** Baixa  
**Tipo:** Functional Test  
**Objetivo:** Validar preenchimento do campo Complemento (opcional)

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Localizar campo "Complemento (Opcional)"
2. Preencher com um complemento (ex: "Apto 45")

### Resultados Esperados
- Campo aceita texto
- Valor digitado aparece no campo
- Campo é realmente opcional (não bloqueia avanço)

### Localizadores Sugeridos
- `page.get_by_label("Complemento (Opcional)")`

---

## CT053 - Etapa 3: Botão Voltar retorna para etapa 2

**Prioridade:** Média  
**Tipo:** Navigation Test  
**Objetivo:** Validar navegação para trás na etapa 3

### Pré-condições
- Estar na etapa 3 (Dados)

### Passos
1. Clicar no botão "Voltar"
2. Verificar transição

### Resultados Esperados
- Retorna para etapa 2 (Recorrência)
- Indicador de progresso mostra etapa 2 como ativa
- Frequência selecionada anteriormente permanece selecionada
- Dados preenchidos são mantidos (se aplicável)

### Localizadores Sugeridos
- `page.get_by_role("button", name="Voltar")`
- `page.get_by_role("heading", name="Frequência da Entrega")`

---

## CT054 - Etapa 3: Validação de campos obrigatórios

**Prioridade:** Alta  
**Tipo:** Validation Test  
**Objetivo:** Validar que campos obrigatórios são validados antes de avançar

### Pré-condições
- Estar na etapa 3 (Dados)
- Campos não preenchidos ou parcialmente preenchidos

### Passos
1. Tentar clicar em "Avançar" sem preencher todos os campos obrigatórios

### Resultados Esperados
- Botão "Avançar" está desabilitado OU
- Mensagens de validação aparecem para campos obrigatórios:
  - Nome Completo (obrigatório)
  - E-mail (obrigatório)
  - Telefone (obrigatório)
  - Nome do Bebê (obrigatório)
  - Idade do Bebê (obrigatório)
  - CEP (obrigatório)
  - Número (obrigatório)
- Não avança para próxima etapa

### Localizadores Sugeridos
- `page.get_by_role("button", name="Avançar")`
- Mensagens de validação

---

## CT055 - Etapa 3: Avançar para etapa 4 com todos os dados preenchidos

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar avanço para etapa final (Pagamento)

### Pré-condições
- Estar na etapa 3 (Dados)
- Todos os campos obrigatórios preenchidos corretamente

### Passos
1. Preencher todos os campos obrigatórios:
   - Nome Completo
   - E-mail válido
   - Telefone
   - Nome do Bebê
   - Idade do Bebê
   - CEP (com busca realizada)
   - Número
2. Clicar no botão "Avançar"

### Resultados Esperados
- Avança para etapa 4 (Pagamento)
- Indicador de progresso mostra etapa 4 como ativa
- Etapas 1, 2 e 3 ficam marcadas como concluídas
- Formulário de pagamento é exibido

### Localizadores Sugeridos
- `page.get_by_role("button", name="Avançar")`
- Indicador de progresso mostrando "4"

---

## CT056 - Etapa 4: Validar exibição da etapa de Pagamento

**Prioridade:** Alta  
**Tipo:** Visual Test  
**Objetivo:** Validar que a etapa de pagamento está disponível

### Pré-condições
- Ter concluído etapas 1, 2 e 3
- Estar na etapa 4 (Pagamento)

### Passos
1. Verificar elementos da etapa de pagamento

### Resultados Esperados
- Indicador de progresso mostra etapa 4 como ativa
- Formulário ou seção de pagamento está visível
- Informações do plano selecionado estão visíveis (resumo)
- Valor total está visível
- Campos ou opções de pagamento estão disponíveis

### Localizadores Sugeridos
- Indicador de progresso mostrando etapa "4"
- Campos relacionados a pagamento

---

## CT057 - Fluxo completo: Assinatura do Plano Essencial

**Prioridade:** Alta  
**Tipo:** End-to-End Test  
**Objetivo:** Validar fluxo completo de assinatura do Plano Essencial

### Pré-condições
- Navegador aberto

### Passos
1. Acessar página de assinatura (`/subscribe`)
2. Selecionar "Plano Essencial"
3. Selecionar frequência "Mensal"
4. Preencher todos os dados:
   - Nome Completo: "Maria Silva"
   - E-mail: "maria.silva@email.com"
   - Telefone: "(11) 98765-4321"
   - Nome do Bebê: "João"
   - Idade do Bebê: Selecionar uma opção
   - CEP: "01310-100" → Buscar
   - Número: "123"
   - Complemento: "Apto 45" (opcional)
5. Avançar para etapa de pagamento

### Resultados Esperados
- Todas as etapas são concluídas com sucesso
- Dados são mantidos entre as etapas
- Indicador de progresso reflete o estado atual
- Etapa de pagamento é alcançada

### Localizadores Sugeridos
- Todos os elementos mencionados nas etapas anteriores

---

## CT058 - Fluxo completo: Assinatura do Plano Conforto (Quinzenal)

**Prioridade:** Alta  
**Tipo:** End-to-End Test  
**Objetivo:** Validar fluxo completo de assinatura do Plano Conforto com frequência quinzenal

### Pré-condições
- Navegador aberto

### Passos
1. Acessar página de assinatura
2. Selecionar "Plano Conforto"
3. Selecionar frequência "Quinzenal"
4. Preencher todos os dados obrigatórios
5. Avançar para etapa de pagamento

### Resultados Esperados
- Fluxo completo funciona corretamente
- Plano Conforto é mantido selecionado
- Frequência quinzenal é mantida
- Etapa de pagamento é alcançada

### Localizadores Sugeridos
- Elementos do fluxo completo

---

## CT059 - Fluxo completo: Assinatura do Plano Completo

**Prioridade:** Alta  
**Tipo:** End-to-End Test  
**Objetivo:** Validar fluxo completo de assinatura do Plano Completo

### Pré-condições
- Navegador aberto

### Passos
1. Acessar página de assinatura
2. Selecionar "Plano Completo"
3. Selecionar frequência "Mensal"
4. Preencher todos os dados obrigatórios
5. Avançar para etapa de pagamento

### Resultados Esperados
- Fluxo completo funciona corretamente
- Plano Completo é mantido selecionado
- Benefícios do Plano Completo estão visíveis (se aplicável)
- Etapa de pagamento é alcançada

### Localizadores Sugeridos
- Elementos do fluxo completo

---

## CT060 - Validar persistência de dados ao navegar entre etapas

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar que dados preenchidos são mantidos ao voltar e avançar

### Pré-condições
- Estar na etapa 3 (Dados)
- Alguns campos já preenchidos

### Passos
1. Preencher alguns campos (ex: Nome Completo, E-mail)
2. Clicar em "Voltar" para etapa 2
3. Clicar em "Avançar" novamente para etapa 3
4. Verificar se os dados foram mantidos

### Resultados Esperados
- Dados preenchidos são mantidos ao voltar
- Campos não são limpos ao navegar entre etapas
- Valores preenchidos permanecem visíveis

### Localizadores Sugeridos
- Campos de formulário da etapa 3





