# Test Cases - Navegação e Interface

## CT001 - Acessar página inicial do BabyRefil

**Prioridade:** Alta  
**Tipo:** Smoke Test  
**Objetivo:** Validar que a página inicial carrega corretamente

### Pré-condições
- Navegador aberto
- Acesso à internet

### Passos
1. Acessar a URL: `https://babyrefil.vercel.app/`
2. Aguardar o carregamento completo da página

### Resultados Esperados
- Página inicial carrega com sucesso
- Título da página é "BabyRefil - Clube de Assinatura de Fraldas"
- Hero section está visível com o heading "Fraldas e cuidados na sua porta."
- Menu de navegação está visível (Como Funciona, Planos, FAQ)
- Botão "Assinar Agora" está visível no header
- Logo "BabyRefil" está visível

### Localizadores Sugeridos
- `page.get_by_role("heading", name="Fraldas e cuidados na sua porta.")`
- `page.get_by_role("link", name="BabyRefil")`
- `page.get_by_role("link", name="Assinar Agora")`

---

## CT002 - Navegação pelo menu: Como Funciona

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar navegação para seção "Como Funciona"

### Pré-condições
- Estar na página inicial

### Passos
1. Clicar no link "Como Funciona" no menu de navegação
2. Aguardar a navegação

### Resultados Esperados
- URL muda para `https://babyrefil.vercel.app/#how-it-works`
- Página faz scroll até a seção "Como Funciona?"
- Seção "Como Funciona?" está visível
- Heading "Como Funciona?" está visível
- Descrição dos 4 passos está visível:
  - Escolha seu plano
  - Defina a frequência
  - Cadastre seus dados
  - Receba em casa

### Localizadores Sugeridos
- `page.get_by_role("link", name="Como Funciona")`
- `page.get_by_role("heading", name="Como Funciona?")`

---

## CT003 - Navegação pelo menu: Planos

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar navegação para seção de Planos

### Pré-condições
- Estar na página inicial

### Passos
1. Clicar no link "Planos" no menu de navegação
2. Aguardar a navegação

### Resultados Esperados
- URL muda para `https://babyrefil.vercel.app/#plans`
- Página faz scroll até a seção de Planos
- Seção "Planos para todos os momentos" está visível
- Três planos estão visíveis:
  - Plano Essencial (R$ 119,90/entrega)
  - Plano Conforto - Popular (R$ 219,90/entrega)
  - Plano Completo (R$ 319,90/entrega)
- Botão "Assinar agora" está visível

### Localizadores Sugeridos
- `page.get_by_role("link", name="Planos")`
- `page.get_by_role("heading", name="Planos para todos os momentos")`
- `page.get_by_text("Plano Essencial")`
- `page.get_by_text("Plano Conforto")`
- `page.get_by_text("Plano Completo")`

---

## CT004 - Navegação pelo menu: FAQ

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar navegação para seção FAQ

### Pré-condições
- Estar na página inicial

### Passos
1. Clicar no link "FAQ" no menu de navegação
2. Aguardar a navegação

### Resultados Esperados
- URL muda para `https://babyrefil.vercel.app/#faq`
- Página faz scroll até a seção FAQ
- Seção "Perguntas Frequentes" está visível
- 5 perguntas estão visíveis:
  - Como funciona o clube de assinatura?
  - Posso alterar meu plano ou a frequência?
  - Quais são as formas de pagamento?
  - Como funciona a entrega?
  - E se eu quiser cancelar?

### Localizadores Sugeridos
- `page.get_by_role("link", name="FAQ")`
- `page.get_by_role("heading", name="Perguntas Frequentes")`

---

## CT005 - Navegação pelo logo para página inicial

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar que clicar no logo retorna para a página inicial

### Pré-condições
- Estar em qualquer página do site (ex: /subscribe ou #plans)

### Passos
1. Clicar no logo "BabyRefil" no header
2. Aguardar a navegação

### Resultados Esperados
- URL muda para `https://babyrefil.vercel.app/`
- Página inicial é exibida
- Hero section está visível

### Localizadores Sugeridos
- `page.get_by_role("link", name="BabyRefil")`

---

## CT006 - Navegação pelo botão "Assinar Agora" do header

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar navegação para página de assinatura via header

### Pré-condições
- Estar na página inicial

### Passos
1. Clicar no botão "Assinar Agora" no header
2. Aguardar a navegação

### Resultados Esperados
- URL muda para `https://babyrefil.vercel.app/subscribe`
- Página de assinatura é exibida
- Indicador de progresso mostra etapa 1 (Plano) ativa
- Seção de seleção de planos está visível

### Localizadores Sugeridos
- `page.get_by_role("banner").get_by_role("link", name="Assinar Agora")`

---

## CT007 - Navegação pelo botão "Assinar Agora" do hero

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar navegação para página de assinatura via hero section

### Pré-condições
- Estar na página inicial

### Passos
1. Clicar no botão "Assinar Agora" na hero section
2. Aguardar a navegação

### Resultados Esperados
- URL muda para `https://babyrefil.vercel.app/subscribe`
- Página de assinatura é exibida
- Indicador de progresso mostra etapa 1 (Plano) ativa

### Localizadores Sugeridos
- `page.get_by_role("link", name="Assinar Agora")` (primeira ocorrência na main)

---

## CT008 - Navegação pelo botão "Ver Planos" do hero

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar navegação para seção de planos via botão do hero

### Pré-condições
- Estar na página inicial

### Passos
1. Clicar no botão "Ver Planos" na hero section
2. Aguardar a navegação

### Resultados Esperados
- URL muda para `https://babyrefil.vercel.app/#plans`
- Página faz scroll até a seção de Planos
- Seção de planos está visível

### Localizadores Sugeridos
- `page.get_by_role("button", name="Ver Planos")`

---

## CT009 - Navegação pelo botão "Assinar agora" da seção de planos

**Prioridade:** Alta  
**Tipo:** Functional Test  
**Objetivo:** Validar navegação para página de assinatura via botão da seção de planos

### Pré-condições
- Estar na seção de planos da página inicial

### Passos
1. Scroll até a seção de planos (se necessário)
2. Clicar no botão "Assinar agora" ao final da seção
3. Aguardar a navegação

### Resultados Esperados
- URL muda para `https://babyrefil.vercel.app/subscribe`
- Página de assinatura é exibida
- Indicador de progresso mostra etapa 1 (Plano) ativa

### Localizadores Sugeridos
- `page.get_by_role("link", name="Assinar agora")`

---

## CT010 - Validação de elementos da seção Hero

**Prioridade:** Média  
**Tipo:** Visual/Functional Test  
**Objetivo:** Validar todos os elementos visíveis na hero section

### Pré-condições
- Estar na página inicial

### Passos
1. Verificar elementos da hero section

### Resultados Esperados
- Heading principal "Fraldas e cuidados na sua porta." está visível
- Descrição "Nunca mais se preocupe em comprar fraldas..." está visível
- Botão "Assinar Agora" está visível e habilitado
- Botão "Ver Planos" está visível e habilitado
- Imagem hero está visível
- Badge "Entregas flexíveis" está visível
- Badge "Cancele quando quiser" está visível

### Localizadores Sugeridos
- `page.get_by_role("heading", name="Fraldas e cuidados na sua porta.")`
- `page.get_by_text("Entregas flexíveis")`
- `page.get_by_text("Cancele quando quiser")`

---

## CT011 - Validação de elementos da seção "Como Funciona"

**Prioridade:** Média  
**Tipo:** Visual/Functional Test  
**Objetivo:** Validar todos os elementos da seção "Como Funciona"

### Pré-condições
- Estar na página inicial
- Scroll até a seção "Como Funciona"

### Passos
1. Navegar até a seção "Como Funciona"
2. Verificar todos os elementos

### Resultados Esperados
- Heading "Como Funciona?" está visível
- Descrição dos 4 passos está visível
- 4 cards estão visíveis com:
  1. "Escolha seu plano" - com descrição
  2. "Defina a frequência" - com descrição
  3. "Cadastre seus dados" - com descrição
  4. "Receba em casa" - com descrição
- Ícones estão visíveis em cada card

### Localizadores Sugeridos
- `page.get_by_role("heading", name="Como Funciona?")`
- `page.get_by_text("Escolha seu plano")`
- `page.get_by_text("Defina a frequência")`
- `page.get_by_text("Cadastre seus dados")`
- `page.get_by_text("Receba em casa")`

---

## CT012 - Validação de elementos da seção de Marcas

**Prioridade:** Baixa  
**Tipo:** Visual Test  
**Objetivo:** Validar seção de marcas parceiras

### Pré-condições
- Estar na página inicial
- Scroll até a seção de marcas

### Passos
1. Navegar até a seção de marcas
2. Verificar elementos

### Resultados Esperados
- Heading "As melhores marcas para o seu bebê" está visível
- Logo da marca Huggies está visível
- Logo da marca MamyPoko está visível
- Logo da marca Pampers está visível

### Localizadores Sugeridos
- `page.get_by_role("heading", name="As melhores marcas para o seu bebê")`
- `page.get_by_role("img", name="Logo da marca Huggies")`
- `page.get_by_role("img", name="Logo da marca MamyPoko")`
- `page.get_by_role("img", name="Logo da marca Pampers")`

---

## CT013 - Validação do Footer

**Prioridade:** Baixa  
**Tipo:** Visual Test  
**Objetivo:** Validar elementos do footer

### Pré-condições
- Estar na página inicial
- Scroll até o footer

### Passos
1. Navegar até o footer
2. Verificar elementos

### Resultados Esperados
- Copyright "© 2025 BabyRefil by Papito." está visível
- Link "Facebook" está visível
- Link "Instagram" está visível
- Link "Twitter" está visível
- Todos os links de redes sociais estão habilitados

### Localizadores Sugeridos
- `page.get_by_text("© 2025 BabyRefil by Papito.")`
- `page.get_by_role("link", name="Facebook")`
- `page.get_by_role("link", name="Instagram")`
- `page.get_by_role("link", name="Twitter")`

---

## CT014 - Responsividade do menu de navegação

**Prioridade:** Baixa  
**Tipo:** Responsive Test  
**Objetivo:** Validar que o menu de navegação está sempre visível e acessível

### Pré-condições
- Estar na página inicial

### Passos
1. Verificar que o menu está visível
2. Testar scroll da página
3. Verificar que o menu permanece acessível

### Resultados Esperados
- Menu de navegação está sempre visível no topo
- Todos os links do menu estão acessíveis
- Logo está sempre visível

### Localizadores Sugeridos
- `page.get_by_role("banner")`
- `page.get_by_role("navigation")`




