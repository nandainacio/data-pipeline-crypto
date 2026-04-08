def load_data(df):
    print("Salvando arquivo...")
    df.to_csv("data/crypto_data.csv", index=False)
    print("Arquivo salvo!")()