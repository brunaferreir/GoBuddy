# Usa uma imagem base oficial do Python.
# Escolha uma versão que seja compatível com suas dependências e com o Streamlit.
# slim-buster é uma boa opção por ser leve.
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do contêiner.
# Tudo que for copiado para o contêiner irá para esta pasta.
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho.
# Isso permite que o Docker use o cache de camadas se as dependências não mudarem.
COPY requirements.txt .

# Instala as dependências Python.
# O --no-cache-dir economiza espaço no contêiner.
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação para o diretório de trabalho.
# O '.' no final indica para copiar tudo do diretório atual do host.
COPY . .

# Expõe a porta que o Streamlit usa (padrão 8501).
# Isso informa ao Docker que esta porta será acessível de fora do contêiner.
EXPOSE 8501

# Define o comando que será executado quando o contêiner iniciar.
# O Streamlit usa 'streamlit run' para iniciar a aplicação.
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false"]