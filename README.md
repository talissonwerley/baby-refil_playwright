# Baby Refil - Projeto de Testes E2E com Playwright

Projeto de automação de testes end-to-end utilizando Playwright e PyTest, seguindo as melhores práticas de SDET.

## 🎯 Objetivo

Automação de testes E2E com foco em qualidade, mantendo os testes independentes, estáveis e utilizando localizadores acessíveis.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Node.js 16 ou superior (para Playwright)
- pip (gerenciador de pacotes Python)

## 🚀 Configuração do Ambiente

### 1. Instalar Dependências Python

```bash
pip install -r requirements.txt
```

### 2. Instalar Navegadores do Playwright

Após instalar as dependências Python, execute:

```bash
playwright install chromium
```

Ou para instalar todos os navegadores:

```bash
playwright install
```

### 3. Verificar Instalação

Execute um teste simples para verificar se tudo está funcionando:

```bash
pytest e2e/ --headed
```

## 📁 Estrutura do Projeto

```
baby-refil_playwright/
├── e2e/                    # Testes E2E
├── pages/                  # Page Objects (POM)
├── utils/                  # Utilitários e helpers
├── reports/                # Relatórios de testes
├── prompts/                # Prompts e documentação
├── conftest.py            # Configurações compartilhadas PyTest
├── pytest.ini             # Configuração do PyTest
├── playwright.config.ts   # Configuração do Playwright
├── requirements.txt       # Dependências Python
└── README.md             # Este arquivo
```

## 🧪 Executando Testes

### Executar todos os testes

```bash
pytest e2e/
```

### Executar testes com visualização (headed)

```bash
pytest e2e/ --headed
```

### Executar teste específico

```bash
pytest e2e/test_exemplo.py
```

### Executar com relatório HTML

```bash
pytest e2e/ --html=reports/report.html
```

### Executar em modo verbose

```bash
pytest e2e/ -v
```

## 📝 Padrões e Convenções

### Localizadores (Hierarquia de Preferência)

1. **`get_by_role()`** - Sempre que possível
2. **`get_by_label()`** - Para inputs
3. **`get_by_placeholder()`** - Quando label não disponível
4. **`get_by_text()`** - Para texto visível e estável
5. **`get_by_test_id()`** - Apenas como último recurso

### Asserções

- Use apenas asserções nativas do Playwright com auto-retry
- `expect(locator).to_be_visible()`
- `expect(locator).to_have_text()`
- `expect(locator).to_be_enabled()`
- `expect(page).to_have_url()`
- **NUNCA** use `assert` do Python diretamente

### Nomenclatura

- Arquivos de teste: `test_<funcionalidade>.py`
- Classes de teste: `Test<NomeDoTeste>`
- Funções de teste: `test_<descricao_do_teste>`

## 🔍 Workflow de Desenvolvimento

1. **Exploração Manual**: Execute manualmente via MCP antes de codificar
2. **Análise HTML**: Analise a estrutura HTML completa da página
3. **Implementação**: Crie o teste usando Page Object Model (POM)
4. **Execução**: Execute e itere até o teste passar

## 📚 Documentação Adicional

Consulte `prompts/sdet-automator.prompt.md` para as regras completas de desenvolvimento de testes.

## 🤝 Contribuindo

Ao adicionar novos testes, certifique-se de:

- Seguir a hierarquia de localizadores
- Usar Page Object Model
- Manter testes independentes
- Adicionar checkpoints em pontos críticos
- Não usar timeouts desnecessários
- Executar testes em Chrome Headed para debug





