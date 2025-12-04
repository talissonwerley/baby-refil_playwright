"""
Classe base para Page Objects
Seguindo o padrão Page Object Model (POM)
"""
from playwright.sync_api import Page, Locator, expect


class BasePage:
    """
    Classe base para todas as páginas
    Contém métodos comuns que podem ser utilizados por todas as páginas
    """
    
    def __init__(self, page: Page):
        """
        Inicializa a página base
        
        Args:
            page: Instância da página do Playwright
        """
        self.page = page
    
    def navigate_to(self, url: str):
        """
        Navega para uma URL específica
        
        Args:
            url: URL de destino
        """
        self.page.goto(url)
        # Checkpoint: Validar que a navegação foi bem-sucedida
        expect(self.page).to_have_url(url)
    
    def get_title(self) -> str:
        """
        Obtém o título da página
        
        Returns:
            Título da página
        """
        return self.page.title()
    
    def wait_for_load_state(self, state: str = "networkidle"):
        """
        Aguarda o estado de carregamento da página
        
        Args:
            state: Estado desejado (load, domcontentloaded, networkidle)
        """
        self.page.wait_for_load_state(state)
    
    def take_screenshot(self, filename: str):
        """
        Captura screenshot da página
        
        Args:
            filename: Nome do arquivo de screenshot
        """
        self.page.screenshot(path=filename)




