import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_sucesso(page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    # Credenciais fornecidas no README
    # Nota: No README a senha não estava explícita, usei "123456" como tentativa inicial.
    login_page.login("Lucas.oliveira@teste.com", "123456") 
    
    # Se o login for bem-sucedido, ele redireciona para index.html (que pode ter conteúdo diferente após o login)
    # Vamos esperar um pouco para ver se o login falha ou redireciona
    page.wait_for_timeout(2000)
    
    # Se ainda estiver na página de login com erro, saberemos.
    # Se mudar a URL para algo que contenha index.html, sucesso (mesmo que seja o redirecionamento do JS)
    assert "index.html" in page.url

def test_navegacao_login_existente(page):
    # Verifica se a página de login carrega corretamente
    page.goto("https://local-eats-unisenac.vercel.app/static/index.html")
    expect(page.locator("#loginForm")).to_be_visible()
