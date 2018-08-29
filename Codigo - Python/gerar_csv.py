import csv


def cria_planilha():

    nome = input("Nome da planilha:")

    with open(nome, 'w') as new_file:
        writer = csv.writer(new_file, delimiter=";")

        writer.writerow(["DATA", "QRU", "ATENDIMENTO", "PLACA", "SERVIÇO"])

        new_file.close()

def preenche_planilha():

    with open('teste.csv', 'a',newline="") as new_file:
        writer = csv.writer(new_file, delimiter=';')

        data = input("Digite a data do atendimento:")
        qru = input("QRU:")
        atend = input("Tipo de atendimento:")
        placa = input("Placa:")
        serv = input("Serviço:")

        writer.writerow([data,qru,atend,placa,serv])
            
        new_file.close()

def le_planilha():
    total = -1

    with open('teste.csv', 'r') as new_file:
        csv_reader = csv.reader(new_file, delimiter=";")

        for line in csv_reader:
            total += 1
        
        print("Total de Serviços: {}" .format(total))


def main():

    menu = True

    while menu == True:

        lista = ['1', '2','3']
        seletor = input("1 - Adiciona Servico | 2 - Total de Serviços | 3 - Sair ")
        while seletor not in lista:
            seletor = input("Selecione uma opção correta")

        if seletor == '1':
            preenche_planilha()

        elif seletor == '2':
            le_planilha()

        elif seletor == '3':
            menu = False


    
if __name__ == '__main__':
    main()