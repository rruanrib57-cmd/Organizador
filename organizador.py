from pathlib import Path

pasta_alvo = Path.home() / "Downloads"

categorias = {
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"],
}

categoria_padrao = "Outras"

extensao_a_categoria = {}
for categoria, exts in categorias.items():
    for ext in exts:
        extensao_a_categoria[ext.lower()] = categoria

for arquivo in pasta_alvo.iterdir():
    if not arquivo.is_file():
        continue

    ext = arquivo.suffix.lower()
    categoria = extensao_a_categoria.get(ext, categoria_padrao)

    pasta_destino = pasta_alvo / categoria
    pasta_destino.mkdir(exist_ok=True)

    arquivo.rename(pasta_destino / arquivo.name)
    print(f"Movido {arquivo.name} para {categoria}/")
