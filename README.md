# Automação MacroDroid (Python + Pytest + Appium + UiAutomator2)

Projeto base de automação mobile (Android) 100% em Python usando:
- **Pytest**
- **Appium-Python-Client**
- **Appium Server 3.x**
- **Driver UiAutomator2**

O primeiro objetivo (MVP) deste repositório é ter um teste “hello world” que:
1) abre o app **MacroDroid**
2) valida que o app ficou em foco (foreground)
3) encerra o app no final

---

## Requisitos

### Sistema / Ferramentas
- macOS
- Python 3 (usando `python3 -m venv`)
- Git + GitHub
- VS Code (opcional)

### Android
- Android SDK instalado (ex: `~/Library/Android/sdk`)
- `adb` funcionando (`adb devices`)
- Emulador Android ligado (ex: `emulator-5554`)

### Appium
- Node + npm
- Appium instalado globalmente (`appium -v`)
- Driver UiAutomator2 instalado no Appium (`appium driver list`)

### Observação sobre warning do urllib3 (LibreSSL)
Ao rodar os testes, pode aparecer um warning:
`NotOpenSSLWarning ... LibreSSL`
Isso ocorre com o Python do macOS (3.9.6) e **não impede** a execução do Appium local (127.0.0.1).
Mais adiante, podemos estabilizar isso migrando para Python via `pyenv`/Homebrew com OpenSSL.

---

## Setup do projeto (primeira vez)

### 1) Clonar o repositório
```bash
git clone git@github.com:Lucaspsp2/automacao-macrodroid.git
cd automacao-macrodroid

