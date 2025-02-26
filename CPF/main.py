from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import re

app = FastAPI()

templates = Jinja2Templates(directory="templates")


# Função para validar CPF
def validar_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)  # Remove caracteres não numéricos
    if len(cpf) != 11 or cpf == cpf[0] * 11:  # Impede CPFs com todos os dígitos iguais
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])


# Rota principal (com a URL exibindo a instrução de digitar o CPF)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Rota para verificar o CPF diretamente na URL
@app.get("/{cpf}", response_class=HTMLResponse)
async def verificar_cpf(request: Request, cpf: str):
    resultado = validar_cpf(cpf)
    status = "válido" if resultado else "inválido"

    return f"""
    <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Validação de CPF</title>
            <link rel="stylesheet" href="/static/style.css">
        </head>
        <body>
            <div class="container">
                <h1>Resultado da Validação</h1>
                <p><strong>CPF:</strong> {cpf}</p>
                <p><strong>Status:</strong> {status}</p>
                <p>Volte para a <a href="/">página inicial</a> para validar outro CPF.</p>
            </div>
        </body>
    </html>
    """
