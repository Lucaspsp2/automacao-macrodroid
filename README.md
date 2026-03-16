# MacroDroid Mobile Automation

Framework de automação mobile desenvolvido em **Python + Appium + Pytest** para validar funcionalidades do aplicativo **MacroDroid** em Android.

O projeto implementa boas práticas de automação como **Page Object Model, relatórios Allure, screenshots automáticas em falha e CI com GitHub Actions**.

---

# Objetivo

Criar uma suíte de automação mobile simples, porém estruturada, para validar fluxos principais do aplicativo MacroDroid, servindo como:

* exemplo de arquitetura de automação
* base para expansão de testes
* projeto de portfólio de QA Automation

---

# Tecnologias utilizadas

* Python
* Pytest
* Appium
* UiAutomator2
* Allure Reports
* GitHub Actions
* Android Emulator / Device

---

# Arquitetura do projeto

```
automacao-macrodroid
│
├── .github/workflows
│   └── python_checks.yml
│
├── core
│   └── logger.py
│
├── pages
│   └── macrodroid_page.py
│
├── tests
│   ├── conftest.py
│   ├── test_hello_macrodroid.py
│   ├── test_macrodroid_dark_mode.py
│   ├── test_macrodroid_logs_navigation.py
│   └── test_macrodroid_smoke.py
│
├── screenshots
├── allure-results
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Estratégia de automação

O projeto utiliza **Page Object Model (POM)** para separar responsabilidades:

### pages/

Contém a lógica de interação com o aplicativo.

Exemplo:

```
MacroDroidPage
```

Responsável por:

* navegação no app
* interações com elementos
* validações de estado

---

### tests/

Contém os testes automatizados.

Cada arquivo valida um fluxo específico do aplicativo.

Exemplo:

```
test_macrodroid_dark_mode.py
```

Valida:

* navegação até Settings
* ativação do Dark Mode
* retorno para Home
* restauração do estado original

---

# Suíte de testes

A suíte atual valida os seguintes fluxos:

### Smoke tests

* abertura do aplicativo
* validação de activity
* verificação de foreground

### Settings

* ativação e desativação de Dark Mode

### Navigation

* acesso ao System Log
* acesso ao User Log
* navegação entre telas

---

# Pytest markers

Os testes estão organizados usando markers:

```
smoke
settings
navigation
regression
```

Executar apenas smoke tests:

```
pytest -m smoke
```

Executar apenas navegação:

```
pytest -m navigation
```

---

# Screenshots automáticas

Quando um teste falha:

* screenshot é capturada automaticamente
* imagem é salva em:

```
screenshots/
```

* imagem também é anexada ao **Allure Report**

---

# Relatórios Allure

Executar testes gerando relatório:

```
pytest --alluredir=allure-results
```

Abrir relatório:

```
allure serve allure-results
```

O relatório inclui:

* passos do teste
* logs
* screenshots em falha
* duração dos testes

---

# CI / GitHub Actions

O projeto possui um pipeline simples configurado em:

```
.github/workflows/python_checks.yml
```

O pipeline executa:

* checkout do repositório
* instalação das dependências
* validação da coleta de testes

Executado automaticamente em:

* push
* pull request

---

# Como executar o projeto

### 1. Clonar repositório

```
git clone https://github.com/Lucaspsp2/automacao-macrodroid.git
```

---

### 2. Criar ambiente virtual

```
python -m venv .macro
source .macro/bin/activate
```

---

### 3. Instalar dependências

```
pip install -r requirements.txt
```

---

### 4. Iniciar Appium

```
appium
```

---

### 5. Executar testes

```
pytest
```

---

# Boas práticas implementadas

* Page Object Model
* Waits customizados
* Logs estruturados
* Screenshot automática em falha
* Relatórios Allure
* Organização com markers
* CI com GitHub Actions

---

# Autor

Lucas Pontes e Pedro Victor

