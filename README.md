# Monitoramento do Sistema ♥️ Flask

Este projeto é uma aplicação web desenvolvida com Flask que exibe informações em tempo real sobre o sistema, como uso de CPU, memória RAM, disco, tempo ligado e processos ativos. Os dados são coletados utilizando a biblioteca `psutil` e apresentados de forma didática e moderna com Bootstrap 5.

## Funcionalidades

- **Monitoramento do CPU:** Exibe o uso percentual do processador.
- **Monitoramento da Memória RAM:** Mostra o uso percentual da memória RAM.
- **Monitoramento do Disco:** Indica o uso percentual do disco principal.
- **Tempo de Atividade:** Mostra há quanto tempo o sistema está ligado.
- **Processos Ativos:** Quantidade de processos em execução.
- **Interface moderna:** Utiliza Bootstrap 5, ícones modernos e fontes Google Fonts.

## Como executar localmente

1. **Clone o repositório (se aplicável):**
   ```bash
   git clone <url-do-repositorio>
   cd codespaces-flask
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação Flask:**
   ```bash
   flask --debug run
   ```
   Acesse em [http://localhost:5000](http://localhost:5000)

## Como executar com Docker

1. **Build da imagem:**
   ```bash
   docker build -t flask-monitor .
   ```

2. **Execute o container:**
   ```bash
   docker run -p 5000:5000 flask-monitor
   ```

   Ou utilize a imagem pronta disponível no Docker Hub:
   ```bash
   docker run -p 5000:5000 edutronicos/docker-flask:1.0
   ```

## Estrutura do Projeto

- `app.py` — Código principal Flask, coleta e envia dados do sistema ao template.
- `templates/index.html` — Página HTML estilizada com Bootstrap 5.
- `static/` — Arquivos estáticos (CSS, imagens, etc).
- `requirements.txt` — Dependências Python.
- `Dockerfile` — Para conteinerização da aplicação.

## Dependências Principais

- Flask
- psutil
- Bootstrap 5 (CDN)
- Bootstrap Icons (CDN)

## Créditos

Desenvolvido por Douglas Eduardo Guimarães Pereira - RA 2320841

---

Imagem Docker disponível em:  
**edutronicos/docker-flask:1.0**

---