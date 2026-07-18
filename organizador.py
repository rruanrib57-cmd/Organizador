from pathlib import Path

# Define a pasta padrão de downloads
pasta_padrao = Path.home() / "Downloads"
pasta_digitada = input(f"Digite o caminho da pasta para organizar (pressione Enter para usar {pasta_padrao}): ").strip()

# Define e resolve o caminho alvo
pasta_alvo = Path(pasta_digitada).expanduser() if pasta_digitada else pasta_padrao
pasta_alvo = pasta_alvo.resolve()

# Validações de segurança do diretório
if not pasta_alvo.exists():
    raise SystemExit(f"A pasta '{pasta_alvo}' não existe.")

if not pasta_alvo.is_dir():
    raise SystemExit(f"O caminho '{pasta_alvo}' não é uma pasta.")

# Mapeamento de categorias
categorias = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif", ".webp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Musica": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z", ".tar.gz"]
}

categoria_padrao = "Outras"

# Inverte o dicionário para busca rápida O(1)
extensao_a_categoria = {ext.lower(): cat for cat, exts in categorias.items() for ext in exts}

# Executa a organização
for arquivo in pasta_alvo.iterdir():
    # Ignora pastas e arquivos ocultos/sistema (começam com ponto)
    if not arquivo.is_file() or arquivo.name.startswith('.'):
        continue

    # Ignora arquivos de sistema específicos do Windows
    if arquivo.name.lower() == 'desktop.ini':
        continue

    # Define a categoria e a pasta de destino
    ext = arquivo.suffix.lower()
    categoria = extensao_a_categoria.get(ext, categoria_padrao)
    
    pasta_destino = pasta_alvo / categoria
    pasta_destino.mkdir(exist_ok=True)

    # Move o arquivo com segurança
    try:
        arquivo.rename(pasta_destino / arquivo.name)
        print(f"Movido: {arquivo.name} ➡️  {categoria}/")
    except Exception as e:
        print(f"Erro ao mover {arquivo.name}: {e}")

print("\nOrganização concluída com sucesso!")
