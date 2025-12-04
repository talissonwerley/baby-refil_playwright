# Test Cases - Planos de Assinatura

## CT023 - Visualizar detalhes do Plano Essencial na página inicial

**Prioridade:** Alta  
**Tipo:** Visual Test  
**Objetivo:** Validar exibição correta dos detalhes do Plano Essencial

### Pré-condições
- Estar na página inicial
- Navegar até a seção de planos

### Passos
1. Navegar até a seção de planos (`/#plans`)
2. Verificar elementos do Plano Essencial

### Resultados Esperados
- Nome "Plano Essencial" está visível
- Preço "R$ 119,90/entrega" está visível
- Lista de itens está visível:
  - ✓ 2 pacotes de fralda premium
  - ✓ 4 pacotes de lenço umedecido
  - ✓ 1 pomada para assaduras
- Não possui badge "Popular"

### Localizadores Sugeridos
- `page.get_by_text("Plano Essencial")`
- `page.get_by_text("R$ 119")`
- `page.get_by_text("2 pacotes de fralda premium")`
- `page.get_by_text("4 pacotes de lenço umedecido")`
- `page.get_by_text("1 pomada para assaduras")`

---

## CT024 - Visualizar detalhes do Plano Conforto na página inicial

**Prioridade:** Alta  
**Tipo:** Visual Test  
**Objetivo:** Validar exibição correta dos detalhes do Plano Conforto (Plano Popular)

### Pré-condições
- Estar na página inicial
- Navegar até a seção de planos

### Passos
1. Navegar até a seção de planos (`/#plans`)
2. Verificar elementos do Plano Conforto

### Resultados Esperados
- Badge "Popular" está visível
- Nome "Plano Conforto" está visível
- Preço "R$ 219,90/entrega" está visível
- Lista de itens está visível:
  - ✓ 4 pacotes de fralda premium
  - ✓ 6 pacotes de lenço umedecido hipoalergênico
  - ✓ 2 pomadas para assaduras premium
  - ✓ Mimos e amostras de parceiros

### Localizadores Sugeridos
- `page.get_by_text("Popular")`
- `page.get_by_text("Plano Conforto")`
- `page.get_by_text("R$ 219")`
- `page.get_by_text("4 pacotes de fralda premium")`
- `page.get_by_text("6 pacotes de lenço umedecido hipoalergênico")`
- `page.get_by_text("2 pomadas para assaduras premium")`
- `page.get_by_text("Mimos e amostras de parceiros")`

---

## CT025 - Visualizar detalhes do Plano Completo na página inicial

**Prioridade:** Alta  
**Tipo:** Visual Test  
**Objetivo:** Validar exibição correta dos detalhes do Plano Completo

### Pré-condições
- Estar na página inicial
- Navegar até a seção de planos

### Passos
1. Navegar até a seção de planos (`/#plans`)
2. Verificar elementos do Plano Completo

### Resultados Esperados
- Nome "Plano Completo" está visível
- Preço "R$ 319,90/entrega" está visível
- Lista de itens está visível:
  - ✓ 6 pacotes de fralda premium ultra macia
  - ✓ 8 pacotes de lenço umedecido hipoalergênico
  - ✓ 3 pomadas para assaduras premium
  - ✓ Kit de cuidados diários para o bebê
  - ✓ Brinde especial e frete grátis em todas as entregas
- Não possui badge "Popular"

### Localizadores Sugeridos
- `page.get_by_text("Plano Completo")`
- `page.get_by_text("R$ 319")`
- `page.get_by_text("6 pacotes de fralda premium ultra macia")`
- `page.get_by_text("8 pacotes de lenço umedecido hipoalergênico")`
- `page.get_by_text("3 pomadas para assaduras premium")`
- `page.get_by_text("Kit de cuidados diários para o bebê")`
- `page.get_by_text("Brinde especial e frete grátis em todas as entregas")`

---

## CT026 - Visualizar todos os três planos na página inicial

**Prioridade:** Alta  
**Tipo:** Visual Test  
**Objetivo:** Validar que todos os três planos estão exibidos

### Pré-condições
- Estar na seção de planos da página inicial

### Passos
1. Verificar que todos os planos estão visíveis

### Resultados Esperados
- Três cards de planos estão visíveis
- Ordem: Plano Essencial, Plano Conforto (Popular), Plano Completo
- Todos os planos têm informações completas
- Botão "Assinar agora" está visível ao final da seção

### Localizadores Sugeridos
- `page.get_by_text("Plano Essencial")`
- `page.get_by_text("Plano Conforto")`
- `page.get_by_text("Plano Completo")`

---

## CT027 - Visualizar planos na página de assinatura

**Prioridade:** Alta  
**Tipo:** Visual Test  
**Objetivo:** Validar exibição dos planos na página de assinatura (/subscribe)

### Pré-condições
- Estar na página de assinatura (`/subscribe`)

### Passos
1. Verificar seção de seleção de planos

### Resultados Esperados
- Indicador de progresso mostra etapa "1" - Plano
- Heading "Escolha o seu plano" está visível
- Descrição "Selecione o plano ideal para as necessidades do seu bebê e da sua família." está visível
- Três planos estão disponíveis para seleção
- Botões "Selecionar Plano" estão visíveis em cada card

### Localizadores Sugeridos
- `page.get_by_role("heading", name="Escolha o seu plano")`
- `page.get_by_text("Selecione o plano ideal")`
- `page.get_by_role("button", name="Selecionar Plano")`

---

## CT028 - Selecionar Plano Essencial na página de assinatura

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar seleção do Plano Essencial

### Pré-condições
- Estar na página de assinatura (`/subscribe`)
- Etapa 1 (Plano) está ativa

### Passos
1. Verificar que o Plano Essencial está visível
2. Clicar no botão "Selecionar Plano" do Plano Essencial
3. Aguardar transição

### Resultados Esperados
- Plano Essencial é selecionado
- Indicador de progresso atualiza (marca etapa 1 como concluída)
- Próxima etapa (Frequência) é exibida
- Botão do plano selecionado muda para "Plano Selecionado" (ou similar)

### Localizadores Sugeridos
- `page.get_by_role("button", name="Selecionar Plano").first()`
- `page.get_by_text("Frequência da Entrega")`

---

## CT029 - Selecionar Plano Conforto na página de assinatura

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar seleção do Plano Conforto

### Pré-condições
- Estar na página de assinatura (`/subscribe`)
- Etapa 1 (Plano) está ativa

### Passos
1. Verificar que o Plano Conforto está visível
2. Clicar no botão "Selecionar Plano" do Plano Conforto
3. Aguardar transição

### Resultados Esperados
- Plano Conforto é selecionado
- Indicador de progresso atualiza
- Próxima etapa (Frequência) é exibida

### Localizadores Sugeridos
- `page.get_by_role("button", name="Selecionar Plano")` (segundo botão, Plano Conforto)

---

## CT030 - Selecionar Plano Completo na página de assinatura

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar seleção do Plano Completo

### Pré-condições
- Estar na página de assinatura (`/subscribe`)
- Etapa 1 (Plano) está ativa

### Passos
1. Verificar que o Plano Completo está visível
2. Clicar no botão "Selecionar Plano" do Plano Completo
3. Aguardar transição

### Resultados Esperados
- Plano Completo é selecionado
- Indicador de progresso atualiza
- Próxima etapa (Frequência) é exibida

### Localizadores Sugeridos
- `page.get_by_role("button", name="Selecionar Plano").last()` (terceiro botão)

---

## CT031 - Alterar seleção de plano (trocar de plano selecionado)

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar que é possível alterar o plano selecionado

### Pré-condições
- Estar na página de assinatura
- Ter selecionado um plano (ex: Plano Essencial)
- Estar na etapa 2 (Frequência)

### Passos
1. Clicar no botão "Voltar" na etapa 2
2. Selecionar outro plano (ex: Plano Conforto)
3. Verificar transição

### Resultados Esperados
- Retorna para etapa 1
- Novo plano é selecionado
- Pode avançar novamente para etapa 2
- Plano anterior é desselecionado

### Localizadores Sugeridos
- `page.get_by_role("button", name="Voltar")`

---

## CT032 - Comparar preços e benefícios dos planos

**Prioridade:** Baixa  
**Tipo:** Visual/Functional Test  
**Objetivo:** Validar que os planos têm informações corretas e comparáveis

### Pré-condições
- Estar na seção de planos

### Passos
1. Verificar preços de todos os planos
2. Verificar benefícios de cada plano
3. Comparar valores

### Resultados Esperados
- Plano Essencial: R$ 119,90/entrega - Menos itens
- Plano Conforto: R$ 219,90/entrega - Badge Popular, mais itens
- Plano Completo: R$ 319,90/entrega - Mais itens, frete grátis
- Preços estão em ordem crescente
- Benefícios aumentam conforme o preço

### Localizadores Sugeridos
- `page.get_by_text("R$ 119")`
- `page.get_by_text("R$ 219")`
- `page.get_by_text("R$ 319")`



