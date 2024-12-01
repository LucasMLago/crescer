import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from dotenv import load_dotenv
import os
import app.Pesquisa

st.set_page_config(
        page_title='Revista Crescer',
        page_icon='📰',
        # layout='wide'
    )

# Carregar variáveis de ambiente
load_dotenv()

# Função para validar variáveis de ambiente
def get_env_var(var_name):
    value = os.getenv(var_name)
    if not value:
        st.error(f"Variável de ambiente {var_name} não encontrada.")
        st.stop()
    return value

RONI_PASSWORD = get_env_var('RONI_PASSWORD')
LLAGO_PASSWORD = get_env_var('LLAGO_PASSWORD')

# Função para carregar configurações do arquivo YAML
def load_config(file_path='config.yml'):
    try:
        with open(file_path, 'r') as file:
            config = yaml.load(file, Loader=SafeLoader)
        return config
    except FileNotFoundError:
        st.error("Arquivo de configuração 'config.yml' não encontrado.")
        st.stop()

config = load_config()

# Atualizar senhas do arquivo de configuração
config['credentials']['usernames']['roni']['password'] = RONI_PASSWORD
config['credentials']['usernames']['llago']['password'] = LLAGO_PASSWORD

# Atualizar hashes de senhas (se necessário)
stauth.Hasher.hash_passwords(config['credentials'])

# Configurar autenticação
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Realizar login
try:
    authenticator.login()
except Exception as e:
    st.error("Erro ao realizar login. Por favor, tente novamente mais tarde.")
    st.stop()

# Lidar com status de autenticação
if st.session_state["authentication_status"]:
    app.Pesquisa.run()  # Certifique-se de que o app suporta execução modular
    authenticator.logout("Logout", "sidebar")
elif st.session_state["authentication_status"] == False:
    st.error('Usuário e/ou senha incorreto(s) 🤥')
elif st.session_state["authentication_status"] is None:
    st.warning('Entre com o seu login e senha 🧐')
