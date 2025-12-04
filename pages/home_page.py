from playwright.sync_api import Page, expect

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://babyrefil.vercel.app/"

        # Header
        self.logo = page.get_by_role("link", name="BabyRefil")
        self.menu_como_funciona = page.get_by_role("link", name="Como Funciona")
        self.menu_planos = page.get_by_role("banner").get_by_role("link", name="Planos")
        self.menu_faq = page.get_by_role("link", name="FAQ")
        self.header_assinar_agora = page.get_by_role("banner").get_by_role("link", name="Assinar Agora")
        

        # Hero
        self.hero_heading = page.get_by_role("heading", name="Fraldas e cuidados na sua porta.")
        self.hero_btn_assinar_agora = page.get_by_role("main").get_by_role("link", name="Assinar Agora", exact=True)
        self.hero_btn_planos = page.get_by_role("button", name="Ver Planos")

        # Seções
        self.sec_como_funciona = page.get_by_role("heading", name="Como Funciona?")
        self.sec_planos = page.get_by_role("heading", name="Planos para todos os momentos")
        self.sec_faq = page.get_by_role("heading", name="Perguntas Frequentes")

        # Footer
        self.footer = page.get_by_text("© 2025 BabyRefil by Papito.")

    def goto(self):
        self.page.goto(self.url)
        expect(self.hero_heading).to_be_visible()
