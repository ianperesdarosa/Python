file = int(input("Digite o tamanho do arquivo que você deseja baixar: "))
net = int(input("Digite a velocidade de sua internet: "))

resSeg = (file / net ) * 8
resMin = resSeg / 60

print(f"O tempo de espera em Segundos: {resSeg} \nTempo de espera em Minutus: {resMin}")