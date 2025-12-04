"""
Script de configuração do ambiente de testes
Execute: python setup.py
"""
import subprocess
import sys
import os


def run_command(command, description):
    """
    Executa um comando e trata erros
    
    Args:
        command: Comando a ser executado
        description: Descrição do comando
    """
    print(f"\n{'='*60}")
    print(f"📦 {description}")
    print(f"{'='*60}")
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        if result.stdout:
            print(result.stdout)
        print(f"✅ {description} - Concluído com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar: {description}")
        print(f"Erro: {e.stderr}")
        return False
    return True


def main():
    """
    Função principal de setup
    """
    print("\n" + "="*60)
    print("🚀 Configurando ambiente de testes Playwright + PyTest")
    print("="*60)
    
    # Verificar Python
    python_version = sys.version_info
    print(f"\n✓ Python {python_version.major}.{python_version.minor}.{python_version.micro} detectado")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8 ou superior é necessário!")
        sys.exit(1)
    
    # Instalar dependências Python
    if not run_command(
        f"{sys.executable} -m pip install --upgrade pip",
        "Atualizando pip"
    ):
        print("\n⚠️  Aviso: Falha ao atualizar pip. Continuando...")
    
    if not run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Instalando dependências Python (pytest, playwright, etc.)"
    ):
        print("\n❌ Falha ao instalar dependências Python!")
        sys.exit(1)
    
    # Instalar navegadores do Playwright
    if not run_command(
        "playwright install chromium",
        "Instalando navegador Chromium do Playwright"
    ):
        print("\n❌ Falha ao instalar navegador Chromium!")
        print("💡 Tente executar manualmente: playwright install chromium")
        sys.exit(1)
    
    # Criar diretórios necessários
    directories = ['reports', 'test-results']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✓ Diretório '{directory}' criado")
    
    print("\n" + "="*60)
    print("✅ Configuração concluída com sucesso!")
    print("="*60)
    print("\n📝 Próximos passos:")
    print("   1. Execute os testes: pytest e2e/")
    print("   2. Execute com visualização: pytest e2e/ --headed")
    print("   3. Veja o README.md para mais informações")
    print("\n")


if __name__ == "__main__":
    main()




