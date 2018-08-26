import csv

def cria_planilha():

    nome = input("Nome da planilha:")
    nome = ("{}.csv".format(nome))

    with open("csv/{}" .format(nome), 'w', newline="") as new_file:
        writer = csv.writer(new_file, delimiter=";")

        writer.writerow(["DATA", "QRU", "ATENDIMENTO", "PLACA", "SERVIÇO"])

        new_file.close()
    
    return nome

def preenche_planilha():

    planilha = input("1 - Nova | 2 - Continua uma existente ") 

    if planilha == '1':
        nome = cria_planilha()
    
    elif planilha == '2':
        nome = input("Nome da planilha ")
        nome = ("{}.csv".format(nome))

    preenche = True
    
    while preenche == True:
        with open("csv/{}" .format(nome), 'a',newline="") as new_file:
            writer = csv.writer(new_file, delimiter=';')

            print("A planilha aberta é {}" .format(nome.upper()))
            data = input("Digite a data do atendimento: ")
            qru = input("QRU: ")
            atend = input("Tipo de atendimento: ")
            placa = input("Placa: ")
            serv = input("Serviço: ")

            cancel = input("Deseja gravar os dados? S/N ")
            cancel = cancel.lower()
            while cancel not in 'sn':
                cancel = input("Deseja gravar os dados? S/N ")

            if cancel == 's':
                writer.writerow([data,qru,atend,placa,serv])
                continua = input("Deseja continuar preenchendo esta planilha? S/N ")
                continua = continua.lower()
                while continua not in 'sn':
                    continua = input("Deseja continuar preenchendo esta planilha? S/N ")

                if continua == 's':
                    preenche = True
                
                elif continua == 'n':
                    preenche = False
            
            if cancel == 'n':
                continua = input("Deseja continuar preenchendo esta planilha? S/N ")
                continua = continua.lower()
                while continua not in 'sn':
                    continua = input("Deseja continuar preenchendo esta planilha? S/N ")

                if continua == 's':
                    preenche = True
                
                elif continua == 'n':
                    preenche = False


            new_file.close()

           



def le_planilha():

    nome = input("Nome da planilha: ")
    nome = ("{}.csv".format(nome))

    total = -1

    with open("csv/{}" .format(nome), 'r') as new_file:
        csv_reader = csv.reader(new_file, delimiter=";")

        for line in csv_reader:
            total += 1
        
        print("Total de Serviços: {}" .format(total))


def main():

    menu = True

    lista = ['1', '2', '3']

    while menu == True:

        seletor = input("1 - Adiciona Servico | 2 - Total de Serviços | 3 - Sair ")
        while seletor not in lista:
            seletor = input("Selecione uma opção correta ")

        if seletor == '1':
            preenche_planilha()

        elif seletor == '2':
            le_planilha()

        elif seletor == '3':
            menu = False


    
if __name__ == '__main__':
    main()