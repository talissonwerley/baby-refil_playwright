"""
Teste de exemplo
Este arquivo serve como template para criação de novos testes

Convenções:
- Nomenclatura: test_<funcionalidade>.py
- Usar Page Object Model (POM)
- Localizadores prioritários: get_by_role(), get_by_label(), etc.
- Asserções nativas do Playwright com auto-retry
"""
import pytest
from playwright.sync_api import Page, expect


class TestExemplo:
    """
    Classe de teste de exemplo
    """
    
    def test_exemplo_basico(self, page: Page):
        """
        Teste básico de exemplo
        
        Este teste demonstra:
        - Navegação para uma página
        - Validação de estado inicial
        - Uso de localizadores prioritários
        - Asserções com auto-retry
        """
        # Checkpoint: Validar estado inicial (antes de navegar)
        assert page.url == "about:blank"
        
        # Navegar para a página (ajustar URL conforme necessário)
        page.goto("https://example.com")
        
        # Checkpoint: Validar URL após navegação
        expect(page).to_have_url("https://example.com")
        
        # Checkpoint: Validar que o título está presente
        expect(page).to_have_title(/Example Domain/)
        
        # Exemplo de uso de get_by_role() (prioridade 1)
        heading = page.get_by_role("heading", name="Example Domain")
        expect(heading).to_be_visible()
        
        # Exemplo de uso de get_by_text() (prioridade 4)
        link_text = page.get_by_text("More information...")
        expect(link_text).to_be_visible()
        
        # Checkpoint: Validar estado final
        expect(page.locator("body")).to_contain_text("Example Domain")



