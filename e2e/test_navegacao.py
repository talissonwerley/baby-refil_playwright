from pages.home_page import HomePage
from playwright.sync_api import expect

def test_CT001_acessar_pagina_inicial(page):
    home = HomePage(page)
    home.goto()

    expect(home.hero_heading).to_be_visible()
    expect(page).to_have_title("BabyRefil - Clube de Assinatura de Fraldas")
    expect(home.logo).to_be_visible()
    expect(home.header_assinar_agora).to_be_visible()

def test_CT002_navegar_para_como_funciona(page):
    home = HomePage(page)
    home.goto()

    home.menu_como_funciona.click()
    expect(page).to_have_url(home.url + "#how-it-works")
    expect(home.sec_como_funciona).to_be_visible()

def test_CT003_navegar_para_planos(page):
    home = HomePage(page)
    home.goto()

    home.menu_planos.click()
    expect(page).to_have_url(home.url + "#plans")
    expect(home.sec_planos).to_be_visible()

def test_CT004_navegar_para_faq(page):
    home = HomePage(page)
    home.goto()

    home.menu_faq.click()
    expect(page).to_have_url(home.url + "#faq")
    expect(home.sec_faq).to_be_visible()

def test_CT005_navegacao_via_logo(page):
    home = HomePage(page)
    home.goto()

    home.menu_planos.click()
    home.logo.click()

    expect(page).to_have_url(home.url)
    expect(home.hero_heading).to_be_visible()

def test_CT006_assinar_agora_header(page):
    home = HomePage(page)
    home.goto()

    home.header_assinar_agora.click()

    expect(page).to_have_url("https://babyrefil.vercel.app/subscribe")
    expect(page.get_by_role("heading", name="Escolha o seu plano")).to_be_visible()

def test_CT007_assinar_agora_hero(page):
    home = HomePage(page)
    home.goto()

    home.hero_btn_assinar_agora.click()

    expect(page).to_have_url("https://babyrefil.vercel.app/subscribe")

def test_CT008_ver_planos_hero(page):
    home = HomePage(page)
    home.goto()

    home.hero_btn_planos.click()
    expect(home.sec_planos).to_be_visible()

def test_CT009_assinar_agora_planos(page):
    home = HomePage(page)
    home.goto()

    page.get_by_role("link", name="Assinar agora").first.click()

    expect(page).to_have_url("https://babyrefil.vercel.app/subscribe")

def test_CT010_validar_hero(page):
    home = HomePage(page)
    home.goto()

    expect(home.hero_heading).to_be_visible()
    expect(home.hero_btn_assinar_agora).to_be_visible()
    expect(home.hero_btn_planos).to_be_visible()
    expect(page.get_by_text("Entregas flexíveis")).to_be_visible()
    expect(page.get_by_text("Cancele quando quiser")).to_be_visible()

def test_CT011_validar_como_funciona(page):
    home = HomePage(page)
    home.goto()

    home.menu_como_funciona.click()

    expect(home.sec_como_funciona).to_be_visible()
    expect(page.get_by_text("Escolha seu plano")).to_be_visible()
    expect(page.get_by_text("Defina a frequência")).to_be_visible()
    expect(page.get_by_text("Cadastre seus dados")).to_be_visible()
    expect(page.get_by_text("Receba em casa")).to_be_visible()

def test_CT012_validar_marcas(page):
    home = HomePage(page)
    home.goto()

    expect(page.get_by_role("heading", name="As melhores marcas para o seu bebê")).to_be_visible()
    expect(page.get_by_role("img", name="Logo da marca Huggies")).to_be_visible()
    expect(page.get_by_role("img", name="Logo da marca MamyPoko")).to_be_visible()
    expect(page.get_by_role("img", name="Logo da marca Pampers")).to_be_visible()

def test_CT013_footer(page):
    home = HomePage(page)
    home.goto()

    expect(home.footer).to_be_visible()
    expect(page.get_by_role("link", name="Facebook")).to_be_visible()
    expect(page.get_by_role("link", name="Instagram")).to_be_visible()
    expect(page.get_by_role("link", name="Twitter")).to_be_visible()

def test_CT014_responsividade_menu(page):
    home = HomePage(page)
    home.goto()

    expect(page.get_by_role("banner")).to_be_visible()

    page.set_viewport_size({"width": 1280, "height": 800})
    expect(page.get_by_role("navigation")).to_be_visible()
