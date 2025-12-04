"""
Configuração compartilhada para todos os testes PyTest
Com suporte para CI/CD (headless) e desenvolvimento local (headed)
"""
import pytest
import os
from playwright.sync_api import Page, Browser, BrowserContext, Playwright


def is_running_in_ci():
    """Detecta se está rodando em ambiente de CI/CD"""
    # GitHub Actions, GitLab CI, Jenkins, etc.
    return os.getenv("CI") == "true" or os.getenv("GITHUB_ACTIONS") == "true"


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
    Headless no CI/CD, Headed no desenvolvimento local
    """
    
    # Configurações baseadas no ambiente
    launch_options = {
        "headless": is_running_in_ci(),  # Headless no CI, Headed local
    }
    
    # Adiciona argumentos específicos para CI
    if is_running_in_ci():
        launch_options["args"] = [
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--disable-setuid-sandbox",
            "--disable-web-security",
            "--disable-features=VizDisplayCompositor",
        ]
    else:
        # Configurações para desenvolvimento local
        launch_options["slow_mo"] = 100  # Desacelera execução para ver melhor
        launch_options["args"] = [
            "--start-maximized",
            "--disable-notifications",
        ]
    
    # Log para debug (aparece com pytest -s)
    print(f"\n🔧 Ambiente: {'CI/CD' if is_running_in_ci() else 'Local'}")
    print(f"🔧 Modo browser: {'headless' if launch_options['headless'] else 'headed'}")
    
    # Lança o browser
    browser = playwright_instance.chromium.launch(**launch_options)
    
    yield browser
    
    # Cleanup
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser):
    """
    Fixture de função que cria um novo contexto para cada teste
    Garante isolamento completo entre testes (conforme regra do prompt)
    """
    context_options = {
        "viewport": {'width': 1280, 'height': 720},
        "ignore_https_errors": True,
    }
    
    # Configurações extras para CI
    if is_running_in_ci():
        context_options.update({
            "record_video_dir": "videos/" if os.getenv("RECORD_VIDEO") else None,
            "record_har_path": "network.har" if os.getenv("RECORD_HAR") else None,
        })
    
    context = browser.new_context(**context_options)
    
    yield context
    
    # Fecha contexto e salva recursos se configurado
    if is_running_in_ci() and os.getenv("RECORD_VIDEO"):
        context.close()
    else:
        context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext):
    """
    Fixture de função que cria uma nova página para cada teste
    Cada teste cria seu próprio estado inicial (isolamento completo)
    """
    page = context.new_page()
    
    # Configura timeout padrão (30 segundos)
    page.set_default_timeout(30000)
    
    yield page
    
    # Fecha a página
    page.close()


# Fixture opcional para URL base (se seu projeto usar)
@pytest.fixture(scope="session")
def base_url():
    """Retorna a URL base para os testes"""
    # Pode ser configurada por variável de ambiente
    return os.getenv("BASE_URL", "https://babyrefil.com.br")