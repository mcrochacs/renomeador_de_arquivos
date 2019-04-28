#!/usr/bin/env python3
#coding: utf-8

import os
import time
import re
from tratador_de_dados3 import TratadorDeDados
from email.utils import parsedate
from PIL import Image


class Arquivo():


    def __init__(self):
        self.nome = ''
        self.data_de_criacao = ''
        self.extensao_do_arquivo = ''
        self.tratador_de_dados = TratadorDeDados()


    def get_nome_arquivo(self):
        return self.nome


    def set_nome_arquivo(self, nome_arquivo):
        self.nome = nome_arquivo


    def get_data_criacao(self):
        return self.data_de_criacao


    def set_data_criacao(self, data):
        data_formatada = self.tratador_de_dados.formatar_data(data)
        self.data_de_criacao = data_formatada


    def get_hora_criacao(self):
        return self.hora_de_criacao


    def set_hora_criacao(self, hora):
        #hora_formatada = self.tratador_de_dados.formatar_hora(hora)
        #self.hora_de_criacao = hora_formatada
        self.hora_de_criacao = hora


    def get_extensao_do_arquivo(self):
        return self.extensao_do_arquivo


    def set_extensao_do_arquivo(self, extensao):
        self.extensao_do_arquivo = extensao


    def montar_novo_nome(self, arquivo, ocasiao_ou_local_da_foto, proprietario):
        data_de_criacao_formatada = self.tratador_de_dados.formatar_data_para_renomear_arquivo(self.data_de_criacao)
        hora_de_criacao_formatada = arquivo.get_hora_criacao()

        nome_do_arquivo_numerico = self.tratador_de_dados.verificar_padrao_de_fotos_e_videos(arquivo)

        if nome_do_arquivo_numerico == '':
            final_file_name = ''
            return final_file_name

        #final_file_name = data_de_criacao_formatada + ocasiao_ou_local_da_foto + 'm' + nome_do_arquivo_numerico + self.get_extensao_do_arquivo()
        final_file_name = data_de_criacao_formatada + '_' + hora_de_criacao_formatada + ocasiao_ou_local_da_foto + proprietario + nome_do_arquivo_numerico + self.get_extensao_do_arquivo()
        return final_file_name


    def renomear(self, arquivo, novo_arquivo):
        os.rename(self.get_nome_arquivo(), novo_arquivo)
        self.set_nome_arquivo(novo_arquivo)


    def buscar_data_de_criacao(self):
        try:
            # formata data em que a foto foi tirada
            #data_criacao = Image.open(os.path.getmtime(self.get_nome_arquivo()))._getexif()[36867]
            data_criacao = Image.open(self.get_nome_arquivo())._getexif()[36867]
            
            #data_criacao = Image.open('C:\\Program Files\\Renomeador de Arquivos\\images\\17072017_10.jpg')._getexif()[36867]
            #data_criacao_formatada = self.tratador_de_dados.formatar_data_da_clicagem_foto(data_criacao)
            data_criacao_formatada = self.tratador_de_dados.formatar_data_da_clicagem_foto(data_criacao)

        except:
            # formata data em que a foto foi modificada
            data_criacao = time.ctime(os.path.getmtime(self.get_nome_arquivo()))
            #data_criacao = time.ctime(os.path.getmtime('C:\\Program Files\\Renomeador de Arquivos\\images\\17072017_10.jpg'))
            data_criacao_formatada = self.tratador_de_dados.formatar_data_criacao_imagem(data_criacao)

        return data_criacao_formatada


    def buscar_hora_de_criacao(self):
        try:
            # formata data em que a foto foi tirada
            v_nome = self.get_nome_arquivo()
            print('v_nome = ' + v_nome)
            #v_getmtime = os.path.getmtime(str(v_nome))

            print('Verificando a Pasta Atual >>> : ' + os.getcwd())

            #v_getmtime = os.path.getmtime('IMG_0793.JPG')

            #print('v_getmtime = ' + str(v_getmtime))

            #data_criacao = Image.open(str(v_getmtime))._getexif()[36867]
            data_criacao = Image.open(self.get_nome_arquivo())._getexif()[36867]
            #data_criacao = Image.open('C:\\Users\\Marcus\\Pictures\\Imagens_para_testes\\IMG_0793.jpg')._getexif()[36867]
            
            print('passo 1 data_criacao = ' + data_criacao)
            
            hora_criacao_formatada = self.tratador_de_dados.formatar_hora_da_clicagem_foto(data_criacao)
            print('passo 2')

        except:
            print('passo 3')
            # formata data em que a foto foi modificada
            data_criacao = time.ctime(os.path.getmtime(self.get_nome_arquivo()))
            #data_criacao = time.ctime(os.path.getmtime('C:\\Program Files\\Renomeador de Arquivos\\images\\17072017_10.jpg'))
            hora_criacao_formatada = self.tratador_de_dados.formatar_hora_criacao_imagem(data_criacao)

        return hora_criacao_formatada
