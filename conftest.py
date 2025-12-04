"""
Configuração compartilhada para todos os testes PyTest
"""
import pytest
from playwright.sync_api import Page, Browser, BrowserContext, Playwright


@pytest.fixture(scope="session")
def playwright_instance():
    """
    Fixture de sessão que inicializa o Playwright
    """
    from playwright.sync_api import sync_playwright
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright):
    """
    Fixture de sessão que cria uma instância do navegador
    Chrome Headed conforme especificado no prompt
    """
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser):
    """
    Fixture de função que cria um novo contexto para cada teste
    Garante isolamento completo entre testes (conforme regra do prompt)
    """
    context = browser.new_context(
        viewport={'width': 1280, 'height': 720},
        ignore_https_errors=True,
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext):
    """
    Fixture de função que cria uma nova página para cada teste
    Cada teste cria seu próprio estado inicial (isolamento completo)
    """
    page = context.new_page()
    yield page
    page.close()

