# Test Cases - FAQ (Perguntas Frequentes)

## CT015 - Exibir resposta ao clicar na primeira pergunta do FAQ

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar funcionamento do accordion do FAQ

### Pré-condições
- Estar na página inicial
- Navegar até a seção FAQ

### Passos
1. Navegar até a seção FAQ (`/#faq`)
2. Clicar no botão "Como funciona o clube de assinatura?"
3. Aguardar a animação de abertura

### Resultados Esperados
- Accordion expande mostrando a resposta
- Resposta fica visível: "Você escolhe um de nossos planos, define a frequência de entrega e nós cuidamos do resto! As fraldas e produtos chegam na sua casa, no conforto do seu lar."
- Botão fica marcado como "expanded"
- Ícone do botão muda (indicando estado expandido)

### Localizadores Sugeridos
- `page.get_by_role("button", name="Como funciona o clube de assinatura?")`
- `page.get_by_role("region", name="Como funciona o clube de assinatura?")`

---

## CT016 - Fechar accordion do FAQ ao clicar novamente

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar que o accordion pode ser fechado

### Pré-condições
- Estar na seção FAQ
- Primeira pergunta já está expandida (após CT015)

### Passos
1. Clicar novamente no botão "Como funciona o clube de assinatura?"
2. Aguardar a animação de fechamento

### Resultados Esperados
- Accordion fecha
- Resposta não fica mais visível
- Botão volta ao estado normal (não expanded)

### Localizadores Sugeridos
- `page.get_by_role("button", name="Como funciona o clube de assinatura?")`

---

## CT017 - Exibir resposta "Posso alterar meu plano ou a frequência?"

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar exibição da segunda pergunta do FAQ

### Pré-condições
- Estar na seção FAQ

### Passos
1. Clicar no botão "Posso alterar meu plano ou a frequência?"
2. Aguardar a animação

### Resultados Esperados
- Accordion expande
- Resposta fica visível (conteúdo específico da resposta)
- Outros accordions podem estar fechados ou abertos (independente)

### Localizadores Sugeridos
- `page.get_by_role("button", name="Posso alterar meu plano ou a frequência?")`

---

## CT018 - Exibir resposta "Quais são as formas de pagamento?"

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar exibição da terceira pergunta do FAQ

### Pré-condições
- Estar na seção FAQ

### Passos
1. Clicar no botão "Quais são as formas de pagamento?"
2. Aguardar a animação

### Resultados Esperados
- Accordion expande
- Resposta fica visível com informações sobre formas de pagamento

### Localizadores Sugeridos
- `page.get_by_role("button", name="Quais são as formas de pagamento?")`

---

## CT019 - Exibir resposta "Como funciona a entrega?"

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar exibição da quarta pergunta do FAQ

### Pré-condições
- Estar na seção FAQ

### Passos
1. Clicar no botão "Como funciona a entrega?"
2. Aguardar a animação

### Resultados Esperados
- Accordion expande
- Resposta fica visível com informações sobre entrega

### Localizadores Sugeridos
- `page.get_by_role("button", name="Como funciona a entrega?")`

---

## CT020 - Exibir resposta "E se eu quiser cancelar?"

**Prioridade:** Média  
**Tipo:** Functional Test  
**Objetivo:** Validar exibição da quinta pergunta do FAQ

### Pré-condições
- Estar na seção FAQ

### Passos
1. Clicar no botão "E se eu quiser cancelar?"
2. Aguardar a animação

### Resultados Esperados
- Accordion expande
- Resposta fica visível com informações sobre cancelamento

### Localizadores Sugeridos
- `page.get_by_role("button", name="E se eu quiser cancelar?")`

---

## CT021 - Múltiplos accordions abertos simultaneamente

**Prioridade:** Baixa  
**Tipo:** Functional Test  
**Objetivo:** Validar que múltiplos accordions podem estar abertos ao mesmo tempo

### Pré-condições
- Estar na seção FAQ

### Passos
1. Clicar no botão da primeira pergunta
2. Aguardar expansão
3. Clicar no botão da segunda pergunta
4. Aguardar expansão
5. Verificar estado de ambos

### Resultados Esperados
- Ambas as perguntas ficam expandidas
- Ambas as respostas estão visíveis
- Não há conflito visual ou funcional

### Localizadores Sugeridos
- `page.get_by_role("button", name="Como funciona o clube de assinatura?")`
- `page.get_by_role("button", name="Posso alterar meu plano ou a frequência?")`

---

## CT022 - Todas as perguntas do FAQ estão visíveis

**Prioridade:** Baixa  
**Tipo:** Visual Test  
**Objetivo:** Validar que todas as 5 perguntas estão visíveis na página

### Pré-condições
- Estar na seção FAQ

### Passos
1. Verificar visibilidade de todas as perguntas

### Resultados Esperados
- 5 botões de perguntas estão visíveis:
  1. "Como funciona o clube de assinatura?"
  2. "Posso alterar meu plano ou a frequência?"
  3. "Quais são as formas de pagamento?"
  4. "Como funciona a entrega?"
  5. "E se eu quiser cancelar?"
- Heading "Perguntas Frequentes" está visível
- Descrição "Respostas rápidas para as dúvidas mais comuns." está visível

### Localizadores Sugeridos
- `page.get_by_role("heading", name="Perguntas Frequentes")`
- `page.get_by_text("Respostas rápidas para as dúvidas mais comuns.")`





