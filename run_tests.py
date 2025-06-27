import pytest

if __name__ == "__main__":
    print("Executando testes de segurança...")
    pytest.main(["-s", "--tb=short", "--html=report.html", "--self-contained-html", "tests/"])
    print("\nTestes concluídos. Relatório gerado em 'report.html'")