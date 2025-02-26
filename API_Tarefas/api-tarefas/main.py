from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Configuração do Swagger UI
SWAGGER_URL = '/api/docs'  # URL para acessar a documentação
API_URL = '/static/swagger.json'  # Caminho para o arquivo de especificação OpenAPI/Swagger

# Cria o blueprint do Swagger UI
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Configurações personalizadas
        'app_name': "API de Tarefas"
    }
)

# Registra o blueprint no Flask
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Dados de exemplo
tarefas = [
    {
        "id": 1,
        "titulo": "Estudar Js",
        "descricao": "Estudar Js para aprender a construir eventos nas páginas web",
        "status": "Em andamento",
        "dt_inicio": "21/02/2025",
        "comentarios": "Essa tarefa é importante para fazer bons sites no futuro",
        "dificuldade": "média"
    },
    {
        "id": 2,
        "titulo": "Estudar Flask",
        "descricao": "Estudar Flask para aprender sobre Web Services",
        "status": "Não iniciada",
        "dt_inicio": "20/02/2025",
        "comentarios": "Essa tarefa é importante para fazer bons sites no futuro",
        "dificuldade": "alta"
    },
    {
        "id": 3,
        "titulo": "Iceberg",
        "descricao": "Continuar a fazer o Iceberg de Undertale",
        "status": "Em andamento",
        "dt_inicio": "20/09/2024",
        "comentarios": "Essa tarefa é um importante projeto pessoal",
        "dificuldade": "baixa"
    }
]

@app.route('/')
def index():
    return "haljkshalkhskjah"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Lista todas as tarefas
    ---
    responses:
      200:
        description: Retorna a lista de tarefas
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/Tarefa'
    """
    return jsonify(tarefas)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    """
    Busca uma tarefa pelo ID
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa
    responses:
      200:
        description: Retorna a tarefa encontrada
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Tarefa'
      404:
        description: Tarefa não encontrada
    """
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return jsonify(tarefa)
    return jsonify({"message": "Tarefa não encontrada"}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Cria uma nova tarefa
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Tarefa'
    responses:
      201:
        description: Tarefa criada com sucesso
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Tarefa'
    """
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Atualiza uma tarefa existente
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Tarefa'
    responses:
      200:
        description: Tarefa atualizada com sucesso
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Tarefa'
      404:
        description: Tarefa não encontrada
    """
    task_search = None
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa
    if not task_search:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    task_body = request.json
    task_search.update(task_body)
    return jsonify(task_search)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Remove uma tarefa pelo ID
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa
    responses:
      200:
        description: Tarefa removida com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
      404:
        description: Tarefa não encontrada
    """
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            tarefas.remove(tarefa)
            return jsonify({"message": f"Tarefa com id {task_id} foi removida com sucesso."})
    return jsonify({"message": f"Tarefa com id {task_id} não encontrada."}), 404

# Rota para servir o arquivo swagger.json
@app.route('/static/swagger.json')
def swagger():
    return app.send_static_file('swagger.json')

if __name__ == '__main__':
    app.run(debug=True)