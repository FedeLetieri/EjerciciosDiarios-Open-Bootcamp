import pandas as pd
#Enunciado: Dado un fichero excel con nombres y correos (columna nombre y columna email),
#  realiza un script en Python que devuelva los mails únicos de la columna email.


ARCH_EXCEL = ""

def unic_emails(excel):
    df = pd.read_excel(excel)
    print(df["Email"].unique())
    
    
unic_emails(ARCH_EXCEL)