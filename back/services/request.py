from http.server import BaseHTTPRequestHandler
from services.db import SQL
from exception.exception import RequestError
import re,sys,json

class JSONResponse:
    @staticmethod
    def send_json_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode('utf-8'))

def json_format(dados):
    return [{
        "id": i[0],
        "nome": i[1],
        "rg": i[2],
        "cpf": i[3],
        "data_nascimento": str(i[4]),
        "data_admissao": str(i[5]),
        "cargo": i[6]
    } for i in dados]

def aux_sql(dados=list) -> str:
    rq = dados.decode('utf-8')  
    rq = json.loads(rq)

    nome = rq.get('nome')
    rg = rq.get('rg')
    cpf = rq.get('cpf')
    data_nascimento = rq.get('data_nascimento')
    data_admissao = rq.get('data_admissao')
    funcao = rq.get('funcao')

    sql = f"""INSERT INTO `pessoas` (`nome`, `rg`, `cpf`, `data_nascimento`, `data_admissao`, `funcao`) 
                        VALUES ('{nome}', '{rg}', '{cpf}', '{data_nascimento}', '{data_admissao}', '{funcao}')"""
    
    return sql

def aux_update(dados=list, id=str) -> str:
    rq = dados.decode('utf-8')  
    rq = json.loads(rq)

    fields = [("nome", rq.get("nome")), ("rg", rq.get("rg")), 
              ("cpf", rq.get("cpf")), ("data_nascimento", rq.get("data_nascimento")), 
              ("data_admissao", rq.get("data_admissao")), ("funcao", rq.get("funcao"))]

    aux = [f"{campo}='{valor}'" for campo, valor in fields if valor]
    valores = ", ".join(aux)

    sql = f"UPDATE `pessoas` SET {valores} WHERE `id_pessoa` = '{id}'"
    
    return sql


class Requests(BaseHTTPRequestHandler):
    def setup(self):
        self.db = SQL()
        return super().setup()
    
    def do_OPTIONS(self):
        print("Recebida solicitação OPTIONS")
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

        self.end_headers()

    def do_GET(self):
        try:
            
            match = re.search(r'pessoas(\?id=(\d+))?', self.path)
            if match:
                id = match.group(2)
                if id:
                    sql = f"""SELECT * FROM `pessoas` WHERE `id_pessoa` = '{id}'"""
                else:
                    sql = "SELECT * FROM `pessoas`"
                result = self.db.read(sql=sql)
                
                json_data = json_format(result)
                JSONResponse.send_json_response(self, 200, json_data)
                
            else:
                raise RequestError("Rota não cadastrada.")
        except RequestError as e:
            error = f"[{sys.exc_info()[-1].tb_lineno}] -> {e}"
            JSONResponse.send_json_response(self, 400, {'error': error})
    
    def do_POST(self):
        try:
            if re.search(r'pessoas', self.path):
                content_length = int(self.headers.get('Content-Length'))
                rq = self.rfile.read(content_length)

                sql = aux_sql(dados=rq)
                result = self.db.post(sql=sql)

                if result:
                    JSONResponse.send_json_response(self, 200, {"status": "ok"})
                else:
                    raise RequestError("Erro ao inserir dados")
            else:
                raise RequestError("Rota não cadastrada")
        except RequestError as e:
            error = f"[{sys.exc_info()[-1].tb_lineno}] -> {e}"
            JSONResponse.send_json_response(self, 400, {'error': error})

    def do_PUT(self):
        try:

            match = re.search(r'pessoas(\?id=(\d+))?', self.path)
            if match:
                id = match.group(2)
                if id:
                    content_length = int(self.headers.get('Content-Length'))
                    rq = self.rfile.read(content_length)

                    sql = aux_update(dados=rq, id=id)
                    result = self.db.post(sql=sql)

                if result:
                    JSONResponse.send_json_response(self, 200, result)
                else:
                    raise RequestError("Erro ao atualizar os dados")
            else:
                raise RequestError("Rota não cadastrada")
        except RequestError as e:
            error = f"[{sys.exc_info()[-1].tb_lineno}] -> {e}"
            JSONResponse.send_json_response(self, 400, {'error': error})

    def do_DELETE(self):
        try:

            match = re.search(r'pessoas(\?id=(\d+))?', self.path)
            if match:
                id = match.group(2)
                if id:
                    sql = f"DELETE FROM `pessoas` WHERE `id_pessoa` = '{id}'"
                    result = self.db.post(sql=sql)
                    JSONResponse.send_json_response(self, 200, result)
                else:
                    raise RequestError("User inválido")
            else:
                raise RequestError("Rota não cadastrada")
        except RequestError as e:
            error = f"[{sys.exc_info()[-1].tb_lineno}] -> {e}"
            JSONResponse.send_json_response(self, 400, {'error': error})

