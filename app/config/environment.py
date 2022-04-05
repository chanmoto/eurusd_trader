import os

class DBConfigurations:
    postgres_username = "user"
    postgres_password = "password"
    postgres_port = 5432
    postgres_db = "model_db"
    postgres_server = "localhost"
    sql_alchemy_database_url = (
        f"postgresql://{postgres_username}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"
    )
    
class APIConfigurations:
    title = os.getenv("API_TITLE", "Model_DB_Service")
    description = os.getenv("API_DESCRIPTION", "machine learning system training patterns")
    version = os.getenv("API_VERSION", "0.1")