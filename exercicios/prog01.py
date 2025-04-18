import sys


preco_cenoura = 4.5
preco_oleo = 12
preco_fermento = 15
preco_leite = 5
preco_acucar = 6
preco_ovos = 12

def soma_ingredientes (tem_cenoura, tem_oleo, tem_fermento, tem_leite, tem_acucar, tem_ovos):
    total_compra = 0
    if tem_cenoura:
        total_compra += preco_cenoura
    if tem_oleo:
        total_compra += preco_oleo
    if tem_fermento:
        total_compra += preco_fermento
    if tem_leite:
        total_compra += preco_leite
    if tem_acucar:
        total_compra += preco_acucar
    if tem_ovos:
        total_compra += preco_ovos
    return total_compra

if __name__ == "__main__":
    
    terminal_tem_cenoura = sys.argv[1].lower() == "sim"
    terminal_tem_acucar = sys.argv[2].lower() == "sim"
    terminal_tem_ovos = sys.argv[3].lower() == "sim"
    terminal_tem_oleo = sys.argv[4].lower() == "sim"
    terminal_tem_fermento = sys.argv[5].lower() == "sim"
    terminal_tem_leite = sys.argv[6].lower() == "sim"
    
    total = soma_ingredientes(terminal_tem_cenoura, terminal_tem_oleo, terminal_tem_fermento, terminal_tem_leite, terminal_tem_acucar, terminal_tem_ovos)
    print("O total da compra é: R$", total)