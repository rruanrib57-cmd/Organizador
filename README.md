# Organizador de Pasta de Downloads 

Este é um script em Python simples e eficiente para resolver a bagunça da sua pasta de `Downloads`. Ele varre a pasta, identifica os arquivos pelas suas extensões e os move automaticamente para pastas categorizadas (Imagens, Documentos, Vídeos, Músicas, etc.).

##  Funcionalidades

- **Organização Automática:** Cria as pastas de categorias apenas se houver arquivos para colocar nelas.
- **Categorização Inteligente:** Agrupa arquivos comuns (PDF, JPG, MP4, etc.).
- **Pasta de Escape ("Outras"):** Qualquer arquivo com extensão não mapeada vai para uma pasta geral, garantindo que nada fique solto.
- **Seguro:** Ignora pastas já existentes para não mover o que já está organizado.

##  Como Funciona

O script mapeia as seguintes extensões por padrão:

| Categoria | Extensões Suportadas |
| :--- | :--- |
| **Imagens** | `.png`, `.jpg`, `.jpeg`, `.gif` |
| **Documentos** | `.pdf`, `.docx`, `.txt`, `.xlsx` |
| **Vídeos** | `.mp4`, `.avi`, `.mkv` |
| **Música** | `.mp3`, `.wav` |
| **Outras** | Qualquer outra extensão não listada acima |

## Modo de uso

### 1. Pré-requisitos
Você só precisa do **Python 3.x** instalado na sua máquina. O script utiliza a biblioteca nativa `pathlib`, então não é necessário instalar nenhuma dependência externa.

### 2. Configuração (Opcional)
Por padrão, o script está configurado para organizar a pasta **Downloads** do usuário atual (`Path.home() / "Downloads"`). 

Se quiser organizar outra pasta, mude a variável `pasta_alvo` no código:
```python
pasta_alvo = Path("C:/Caminho/Da/Sua/Pasta")
