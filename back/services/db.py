import yaml, sys, mysql.connector

from exception.exception import SQLError

class Config:
    @staticmethod
    def get_config() -> dict:
        """Lê arquivo de configuração

        Returns:
            dict: dicionario com as configurações
        """
        with open("config.yaml", "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            return data
        

class SQL:
    """
        Classe responsável por realizar a consulta ou inserções no banco de dados
    """
    def __init__(self) -> None:
        config = Config.get_config()['db']
        __host = config['host']
        __port= config['port']
        __user= config['user']
        __password= config['password']
        __database= config['database']


        self.conexao = mysql.connector.connect(
            host=__host,
            port=__port,
            user=__user,
            password=__password,
            database=__database,
        )

        self.cursor = self.conexao.cursor()


    def post(self, sql:str) -> dict:
        """ Função responsável por realizar comandos de update/create/delete no banco de dados

        Args:
            sql (str): recebe o comando sql

        Raises:
            SQLError: caso tenha algum erro relacionado a consulta

        Returns:
            dict: retorna um dict com ok na requisição
        """
        try:

            self.cursor.execute(sql)
            self.conexao.commit()
            self.cursor.fetchall() 

            return {"status": "ok"}
        except Exception as e:
            raise SQLError(f"[{sys.exc_info()[-1].tb_lineno}] -> {e}")
        
    def read(self, sql:str) -> list:
        """Função responsável por realizar comandos de read/get no banco de dados

        Args:
             sql (str): recebe o comando sql

        Raises:
            SQLError: caso tenha algum erro relacionado a consulta

        Returns:
            list: retorna os dados obtidos no banco
        """
        try:

            self.cursor.execute(sql) 
            result = self.cursor.fetchall()
        
            return result
        except Exception as e:
            raise SQLError(f"[{sys.exc_info()[-1].tb_lineno}] -> {e}")
        