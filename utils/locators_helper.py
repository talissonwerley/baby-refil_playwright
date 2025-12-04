"""
Helper com exemplos de uso de localizadores do Playwright
Seguindo a hierarquia de preferência especificada no prompt

Hierarquia de Preferência:
1º: get_by_role() com nomes acessíveis
2º: get_by_label() para inputs
3º: get_by_placeholder() quando label não estiver disponível
4º: get_by_text() para texto visível e estável
5º: get_by_test_id() apenas como último recurso
"""
from playwright.sync_api import Page, Locator


class LocatorsHelper:
    """
    Helper com exemplos práticos de uso de localizadores
    """
    
    def __init__(self, page: Page):
        """
        Inicializa o helper com a página
        
        Args:
            page: Instância da página do Playwright
        """
        self.page = page
    
    # PRIORIDADE 1: get_by_role()
    def get_button(self, name: str, exact: bool = False) -> Locator:
        """
        Obtém um botão usando get_by_role()
        
        Args:
            name: Nome acessível do botão
            exact: Se True, busca correspondência exata
        
        Returns:
            Locator do botão
        """
        return self.page.get_by_role("button", name=name, exact=exact)
    
    def get_heading(self, name: str, level: int = None) -> Locator:
        """
        Obtém um cabeçalho usando get_by_role()
        
        Args:
            name: Texto do cabeçalho
            level: Nível do cabeçalho (1-6), opcional
        
        Returns:
            Locator do cabeçalho
        """
        if level:
            return self.page.get_by_role("heading", name=name, level=level)
        return self.page.get_by_role("heading", name=name)
    
    def get_link(self, name: str, exact: bool = False) -> Locator:
        """
        Obtém um link usando get_by_role()
        
        Args:
            name: Texto do link
            exact: Se True, busca correspondência exata
        
        Returns:
            Locator do link
        """
        return self.page.get_by_role("link", name=name, exact=exact)
    
    # PRIORIDADE 2: get_by_label()
    def get_input_by_label(self, label: str, exact: bool = False) -> Locator:
        """
        Obtém um input usando get_by_label()
        
        Args:
            label: Texto do label associado ao input
            exact: Se True, busca correspondência exata
        
        Returns:
            Locator do input
        """
        return self.page.get_by_label(label, exact=exact)
    
    # PRIORIDADE 3: get_by_placeholder()
    def get_input_by_placeholder(self, placeholder: str, exact: bool = False) -> Locator:
        """
        Obtém um input usando get_by_placeholder()
        Usar quando label não estiver disponível
        
        Args:
            placeholder: Texto do placeholder
            exact: Se True, busca correspondência exata
        
        Returns:
            Locator do input
        """
        return self.page.get_by_placeholder(placeholder, exact=exact)
    
    # PRIORIDADE 4: get_by_text()
    def get_by_text(self, text: str, exact: bool = False) -> Locator:
        """
        Obtém elemento usando get_by_text()
        Usar para texto visível e estável
        
        Args:
            text: Texto a ser buscado
            exact: Se True, busca correspondência exata
        
        Returns:
            Locator do elemento
        """
        return self.page.get_by_text(text, exact=exact)
    
    # PRIORIDADE 5: get_by_test_id() - Último recurso
    def get_by_test_id(self, test_id: str) -> Locator:
        """
        Obtém elemento usando get_by_test_id()
        Usar APENAS como último recurso
        
        Args:
            test_id: Valor do atributo data-testid
        
        Returns:
            Locator do elemento
        """
        return self.page.get_by_test_id(test_id)





