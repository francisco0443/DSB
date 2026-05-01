import os
from pathlib import Path

import oracledb
import pandas as pd

# Parâmetros de conexão via ambiente
username = os.environ.get("ORACLE_USERNAME", "")
password = os.environ.get("ORACLE_PASSWORD", "")
host = os.environ.get("ORACLE_HOST", "")
port = int(os.environ.get("ORACLE_PORT", "1521"))
service_name = os.environ.get("ORACLE_SERVICE_NAME", "CDE")

if not all([username, password, host, service_name]):
    raise ValueError("Set ORACLE_USERNAME, ORACLE_PASSWORD, ORACLE_HOST and ORACLE_SERVICE_NAME before running")

# Criar diretório CSVTables se não existir
csv_dir = Path("CSVTables")
csv_dir.mkdir(parents=True, exist_ok=True)

# Criar conexão
dsn = oracledb.makedsn(host, port, service_name=service_name)
conn = oracledb.connect(user=username, password=password, dsn=dsn)

# Query para obter todos os synonyms
query = """
SELECT synonym_name, table_owner, table_name 
FROM all_synonyms 
WHERE owner = 'GROUP4' 
ORDER BY synonym_name
"""

# Criar cursor e executar query
cursor = conn.cursor()
cursor.execute(query)

# Obter resultados
results = cursor.fetchall()

# Criar DataFrame
df = pd.DataFrame(results, columns=['SYNONYM_NAME', 'TABLE_OWNER', 'TABLE_NAME'])

# Print e exportar cada tabela
print(f"\nTotal de Synonyms: {len(df)}\n")
print("="*80)

for index, row in df.iterrows():
    synonym_name = row['SYNONYM_NAME']
    table_owner = row['TABLE_OWNER']
    table_name = row['TABLE_NAME']
    
    print(f"\nProcessing Synonym: {synonym_name}")
    print(f"  Owner: {table_owner}")
    print(f"  Table: {table_name}")
    
    try:
        # Query para obter dados da tabela
        table_query = f'SELECT * FROM "{table_owner}"."{table_name}"'
        table_df = pd.read_sql(table_query, conn)
        
        # Salvar como CSV
        csv_filename = csv_dir / f"{synonym_name}.csv"
        table_df.to_csv(csv_filename, index=False, encoding='utf-8')
        
        print(f"  ✓ Exported {len(table_df)} rows to {csv_filename}")
    except Exception as e:
        print(f"  ✗ Error exporting {synonym_name}: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
    
    print("-"*80)

print(f"\nExport completed! CSV files saved in '{csv_dir}' directory.")
