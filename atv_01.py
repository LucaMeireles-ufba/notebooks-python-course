def main():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura em metros: "))

    print(f"Olá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura:.2f} metros.")

if __name__ == "__main__":
    main()