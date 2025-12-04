# Documentação de Test Cases - BabyRefil

Esta pasta contém todos os test cases mapeados para cobertura E2E completa do site BabyRefil.

## 📋 Estrutura

```
docs/
├── 00-indice-test-cases.md          # Índice geral e resumo
├── 01-test-cases-navegacao.md       # Testes de navegação e interface
├── 02-test-cases-faq.md             # Testes do FAQ
├── 03-test-cases-planos.md          # Testes de planos de assinatura
├── 04-test-cases-assinatura.md      # Testes do fluxo de assinatura
└── README.md                        # Este arquivo
```

## 🎯 Visão Geral

Foram mapeados **60 test cases** cobrindo todas as funcionalidades principais do site:

- ✅ Navegação e elementos da interface (14 test cases)
- ✅ FAQ com accordion (8 test cases)
- ✅ Visualização e seleção de planos (10 test cases)
- ✅ Fluxo completo de assinatura (28 test cases)

## 📖 Como Usar

### Para Desenvolvedores

1. Consulte o `00-indice-test-cases.md` para visão geral
2. Escolha o módulo que deseja implementar
3. Siga os test cases em ordem de prioridade
4. Use os localizadores sugeridos em cada test case
5. Implemente seguindo as regras em `prompts/sdet-automator.prompt.md`

### Para QA/Testers

1. Use os test cases como checklist de cobertura
2. Execute os testes manualmente para validar
3. Reporte falhas seguindo o formato dos test cases
4. Priorize testes de Alta Prioridade para validação rápida

## 🔍 Formato dos Test Cases

Cada test case segue este formato:

```markdown
## CTXXX - Nome do Test Case

**Prioridade:** Alta/Média/Baixa  
**Tipo:** Smoke Test / Functional Test / Visual Test / etc.  
**Objetivo:** Descrição do objetivo

### Pré-condições
- Condições necessárias antes de executar

### Passos
1. Passo 1
2. Passo 2
3. ...

### Resultados Esperados
- Resultado esperado 1
- Resultado esperado 2
- ...

### Localizadores Sugeridos
- `page.get_by_role(...)`
- `page.get_by_label(...)`
```

## 🎨 Hierarquia de Localizadores

Conforme padrão do projeto, usar sempre:

1. **1º:** `get_by_role()` - Sempre que possível
2. **2º:** `get_by_label()` - Para inputs
3. **3º:** `get_by_placeholder()` - Quando label não disponível
4. **4º:** `get_by_text()` - Para texto visível e estável
5. **5º:** `get_by_test_id()` - Apenas como último recurso

## ✅ Checklist de Implementação

Ao implementar cada test case:

- [ ] Teste executa em Chrome Headed (headless: false)
- [ ] Usa localizadores da hierarquia correta
- [ ] Usa asserções nativas do Playwright com auto-retry
- [ ] Adiciona checkpoints em pontos críticos
- [ ] Não usa timeouts desnecessários
- [ ] Teste é independente (isolamento completo)
- [ ] Segue padrão Page Object Model (quando aplicável)
- [ ] Código está limpo e documentado

## 📊 Status de Implementação

Para rastrear o progresso, marque cada test case conforme implementado:

- ⏳ **Pendente** - Não iniciado
- 🔄 **Em Progresso** - Sendo implementado
- ✅ **Concluído** - Implementado e testado
- ❌ **Bloqueado** - Aguardando dependências

## 🔗 Links Úteis

- [Site BabyRefil](https://babyrefil.vercel.app/)
- [Prompt de Automação](../prompts/sdet-automator.prompt.md)
- [README do Projeto](../README.md)
- [Configuração do PyTest](../pytest.ini)

## 📝 Notas

- Todos os test cases foram mapeados através de exploração manual do site
- Estrutura HTML foi analisada para definir localizadores apropriados
- Test cases seguem as melhores práticas do prompt SDET
- Foco em testes E2E que validam o fluxo completo do usuário



