#!/usr/bin/env python3
#coding: utf-8


import os
import arquivo3
from   datetime import datetime
from   tratador_de_dados3 import TratadorDeDados


# 'C:\\Users\\marcus_31161\\python\\pictures' - TRT
# '/home/mcrocha/Pictures' - Linux
# C:\Users\Marcus\Pictures\103_FUJI - Dell


# Ver como usar atributos ou métodos privados
# Ver também os padrões para dar nome às classes, funções e variáveis


def main():

    v_pasta_de_trabalho = input('Informe o caminho completo da pasta onde os arquivos serao renomeados: ')

    os.chdir(v_pasta_de_trabalho)
    print('Pasta de Trabalho: ' + os.getcwd())
    v_ocasiao = input('Informe a ocasião ou local das fotos: ')
    v_proprietario = input('Informe a inicial do proprietário (M/N/L): ')

    v_data_tem_formato_errado = True
    v_hora_tem_formato_errado = True
    v_data_criacao = ''
    

    while v_data_tem_formato_errado or v_hora_tem_formato_errado:

        v_data_hora_criacao = input('Informe, se desejar, a data e hora de criacao dos arquivos a serem renomeados no formato DD/MM/YYYY-HH: ')

        if v_data_hora_criacao == '':
            break
        
        v_data_criacao, v_hora_criacao = TratadorDeDados().separar_data_e_hora_digitadas(v_data_hora_criacao)

        if v_data_criacao == '':
            break

        if v_hora_criacao == '':
            break

        try:
            v_verificacao_da_data = datetime.strptime(v_data_criacao, '%d/%m/%Y')
            v_data_tem_formato_errado = False

        except:
            v_data_criacao = ''
            print('Data com formato invalido!!')

        if isInt(v_hora_criacao):
            v_hora_tem_formato_errado = False
        else:
            v_hora_criacao = ''
            print('A Hora nao eh Inteira!!')

        
    v_ocasiao = v_ocasiao.replace(" ","_")
    v_ocasiao_formatada = '_' + v_ocasiao + '_'

    arquivo_obj = arquivo3.Arquivo()

    
    for f in os.listdir(v_pasta_de_trabalho):
        nome_completo_do_arquivo = os.path.basename(f)
        nome_do_arquivo, extensao = os.path.splitext(nome_completo_do_arquivo)
        arquivo_obj.set_nome_arquivo(nome_completo_do_arquivo)
        arquivo_obj.set_extensao_do_arquivo(extensao) 

        if v_data_criacao == '':
            arquivo_obj.set_data_criacao(arquivo_obj.buscar_data_de_criacao())
            arquivo_obj.set_hora_criacao(arquivo_obj.buscar_hora_de_criacao())
        else:
            arquivo_obj.set_data_criacao(v_data_criacao)
            arquivo_obj.set_hora_criacao(v_hora_criacao)

        novo_nome_do_arquivo = arquivo_obj.montar_novo_nome(arquivo_obj, v_ocasiao_formatada, v_proprietario)

        if novo_nome_do_arquivo == '':
            continue

        arquivo_obj.renomear(arquivo_obj, novo_nome_do_arquivo)
        print('Arquivo ' + nome_completo_do_arquivo + ' foi renomeado para ' + arquivo_obj.get_nome_arquivo())
        
    print('O processo para renomear fotos e videos foi concluido com sucesso!')    


def isInt(value):
    try:
        int(value)
        return True
    except:
        return False


if __name__ == '__main__':
    main()
