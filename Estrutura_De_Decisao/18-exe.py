import datetime

def validar_data(data):
    try:
        datetime.datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def main():
    data_digitada = input("Digite uma data no formato dd/mm/aaaa: ")

    if validar_data(data_digitada):
        print("A data", data_digitada, "é válida.")
    else:
        print("A data", data_digitada, "é inválida.")

if __name__ == "__main__":
    main()
