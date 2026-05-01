from pathlib import Path

import pandas as pd

BASE_DIR = Path("CSVTables")

filepath = BASE_DIR / "SALES_FLAT_ORDER_ADDRESS.csv"
filepath2 = BASE_DIR / "CATALOG_PRODUCT_ENTITY.csv"
filepath3 = BASE_DIR / "CATALOG_PRODUCT_ENTITY_VARCHAR.csv"
filepath4 = BASE_DIR / "CATALOG_PRODUCT_ENTITY_INT.csv"
filepath5 = BASE_DIR / "EAV_ATTRIBUTE_OPTION_VALUE.csv"
filepath6 = BASE_DIR / "SALES_FLAT_ORDER.csv"

if __name__ == "__main__":

    sfo_address = pd.read_csv(
        filepath,
        delimiter=",",
        dtype=str,
    )

    columnstoselect = [
        "entity_id",  # para fazer merge
        "region",
        "city",
        "email",
        "address_type",  # será 100% shipping se tiver tudo bem quando se fizer o merge
        "country_id",
    ]

    sfo_address = sfo_address[columnstoselect]
    sfo_address.to_csv(BASE_DIR / "SALES_FLAT_ORDER_ADDRESS_CLEAN.csv", index=False)

    catalog_product_entity = pd.read_csv(
        filepath2,
        delimiter=",",
        dtype=str,
    )

    columnstoselect = [
        "ENTITY_ID",  # para fazer merge
        "TYPE_ID",
        "SKU",
    ]

    catalog_product_entity = catalog_product_entity[columnstoselect]
    catalog_product_entity.to_csv(BASE_DIR / "CATALOG_PRODUCT_ENTITY_CLEAN.csv", index=False)

    catalog_product_entity_varchar = pd.read_csv(
        filepath3,
        delimiter=",",
        dtype=str,
    )

    columnstoselect = [
        "ATTRIBUTE_ID",
        "STORE_ID",
        "ENTITY_ID",  # para fazer merge
        "VALUE",
    ]

    catalog_product_entity_varchar = catalog_product_entity_varchar[columnstoselect]
    catalog_product_entity_varchar.to_csv(BASE_DIR / "CATALOG_PRODUCT_ENTITY__VARCHAR_CLEAN.csv", index=False)

    catalog_product_entity_int = pd.read_csv(
        filepath4,
        delimiter=",",
        dtype=str,
        )

    columnstoselect = [
        "ENTITY_ID",
        "ATTRIBUTE_ID",
        "STORE_ID",
        "VALUE",  # para fazer merge
    ]

    catalog_product_entity_int = catalog_product_entity_int[columnstoselect]
    catalog_product_entity_int.to_csv(BASE_DIR / "CATALOG_PRODUCT_ENTITY_INT_CLEAN.csv", index=False)

    eav_attribute_option_value = pd.read_csv(
        filepath5,
        delimiter=",",
        dtype=str,
    )

    columnstoselect = [
        "option_id",
        "store_id",
        "value",
    ]

    eav_attribute_option_value = eav_attribute_option_value[columnstoselect]
    eav_attribute_option_value.to_csv(BASE_DIR / "EAV_ATTRIBUTE_OPTION_VALUE_CLEAN.csv", index=False)

    sfo = pd.read_csv(
        filepath6,
        delimiter=",",
        dtype=str,
    )
    # Colunas a incluir na consulta (deixe vazio [] para selecionar todas)
    columns_to_select = [
        # Descomentar e adicionar as colunas desejadas:
        'ENTITY_ID', # ID
        'STATE', # ESTADO
        'COUPON_CODE', 
        'STORE_ID', # PAIS LOJA
        'CUSTOMER_ID', 
        'BASE_DISCOUNT_INVOICED', # DESCONTO BASE FATURADO
        'BASE_DISCOUNT_REFUNDED', # DESCONTO BASE DEVOLVIDO
        'BASE_GRAND_TOTAL', # TOTAL BASE PRODUTOS 
        'BASE_SHIPPING_INVOICED', # FRETE BASE FATURADO
        'BASE_SUBTOTAL_INVOICED', # GRANDTOTAL + SHIPPING - SE STATUS == "closed" foi refunded
        'BASE_TO_ORDER_RATE', # COTACAO MOEDA = ao STORE_TO_ORDER_RATE
        'BASE_TOTAL_INVOICED_COST', # CUSTO TOTAL BASE FATURADO
        'TOTAL_QTY_ORDERED', # QTD TOTAL PEDIDA
        'CUSTOMER_IS_GUEST',
        'CUSTOMER_GROUP_ID', # EXCEL:  1- "Registered Client",   7 - "Team",  9 - "Friends" ,2 - "", 8-"", os restantes "Not Registered"
        'SHIPPING_ADDRESS_ID',
        'WEIGHT',
        'INCREMENT_ID', # EXCEL: campo usado para excluir marketplaces
        'ORDER_CURRENCY_CODE', # MOEDA DO PEDIDO
        'STORE_NAME', # NOME DA LOJA
        'CREATED_AT',
        'UPDATED_AT', 
        'CUSTOMER_GENDER', # so existem 135 com valor 1 ou 2, o resto é null
        'TOTAL_ITEM_COUNT', # VER SE É IGUAL AO TOTAL_QTY_ORDERED
        'COUPON_RULE_NAME',
        'BASE_SUBTOTAL_WITH_DISCOUNT', # ver se é igual a BASE_SUBTOTAL_INVOICED
        'ANALYTICS', # DÁ PARA EXTRAIR O DEVICE DAQUI MOBILE VS WEB
        # 'UPDATED_AT',
    ]


    sfo = sfo[columnstoselect]
    sfo.to_csv(BASE_DIR / "SALES_FLAT_ORDER_CLEAN.csv", index=False)