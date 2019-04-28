#!/usr/bin/env python3
#coding: utf-8

#import os
import re
from email.utils import parsedate


class TratadorDeDados():

    # Não está mais em uso durante os testes
    def converter_mes_para_numerico(self, mes_alfanumerico):
        switcher = {
                'Jan': '01',
                'Feb': '02',
                'Mar': '03',
                'Apr': '04',
                'May': '05',
                'Jun': '06',
                'Jul': '07',
                'Aug': '08',
                'Sep': '09',
                'Oct': '10',
                'Nov': '11',
                'Dec': '12',
                }
        mes_numerico = switcher.get(mes_alfanumerico)
        return mes_numerico


    # Não está mais em uso durante os testes
    def verificar_padrao_de_data_do_windows(self, data_de_criacao_do_arquivo):
        padrao_de_data_no_windows = re.compile(r'^(\D+)\s(\D+)\s(\d\d?)\s\d\d:\d\d:\d\d\s(\d+)$')
        return padrao_de_data_no_windows.search(data_de_criacao_do_arquivo)


    def formatar_data_para_renomear_arquivo(self, data):
        try:
            padrao_de_data_de_entrada = re.compile(r'(\d\d)\/(\d\d)\/(\d\d\d\d)')
            dia, mes, ano = self.retirar_dia_mes_ano_de_string(data, padrao_de_data_de_entrada)
            data_em_tupla = (int(ano), int(mes), int(dia))
            data_criacao_formatada = "%04d%02d%02d"%data_em_tupla

        except:
            data_criacao_formatada = ''

        return data_criacao_formatada


    def formatar_data(self, data):
        try:
            padrao_de_data_de_entrada = re.compile(r'^(\d\d?)/(\d\d?)/(\d\d\d\d)$')
            dia, mes, ano = self.retirar_dia_mes_ano_de_string(data, padrao_de_data_de_entrada)
            data_em_tupla = (int(dia), int(mes), int(ano))
            data_formatada = "%02d/%02d/%04d"%data_em_tupla

        except:
            data_formatada = ''
            
        return data_formatada
    

    def formatar_data_criacao_imagem(self, data_criacao):
        data_criacao_com_parse = parsedate(data_criacao)[:3]
        data_criacao_com_parse_trocado = (data_criacao_com_parse[2],data_criacao_com_parse[1],data_criacao_com_parse[0])
        data_criacao_formatada = "%02d/%02d/%04d"%data_criacao_com_parse_trocado
        return data_criacao_formatada


    def formatar_hora_criacao_imagem(self, data_criacao):
        data_criacao_com_parse = parsedate(data_criacao)[:4]
        hora_criacao_com_parse = (data_criacao_com_parse[3])
        hora_criacao_formatada = "%02d"%hora_criacao_com_parse
        return hora_criacao_formatada


    def formatar_data_da_clicagem_foto(self, data_criacao):
        try:
            print('passo 4')
            
            padrao_de_data_de_entrada = re.compile(r'^(\d\d\d\d):(\d\d?):(\d\d?)\s(\d\d?):(\d\d?):(\d\d?)$')
            resultado = padrao_de_data_de_entrada.search(data_criacao)
            
            ano = resultado.group(1).strip()
            mes = resultado.group(2).strip()
            dia = resultado.group(3).strip()
            data_em_tupla = (int(dia), int(mes), int(ano))
            
            data_formatada = "%02d/%02d/%04d"%data_em_tupla

        except:
            print('passo 5')
            
            data_formatada = ''
            
        return data_formatada
        

    def formatar_hora_da_clicagem_foto(self, data_criacao):
        try:
            padrao_de_data_de_entrada = re.compile(r'^(\d\d\d\d):(\d\d?):(\d\d?)\s(\d\d?):(\d\d?):(\d\d?)$')
            resultado = padrao_de_data_de_entrada.search(data_criacao)
            
            hora = resultado.group(4).strip()
            hora_inteiro = int(hora)
            
            hora_formatada = "%02d"%hora_inteiro

        except:
            hora_formatada = ''
            
        return hora_formatada


    def retirar_dia_mes_ano_de_string(self, data_em_string, padrao_de_expressao_regular):
        try:
            resultado = padrao_de_expressao_regular.search(data_em_string)
            dia = resultado.group(1).strip()
            mes = resultado.group(2).strip()
            ano = resultado.group(3).strip()

        except:
            dia, mes, ano = '', '', ''
            
        return dia, mes, ano
    

    def validar_fotos_e_videos(self, arquivo):
        extensao_do_arquivo = arquivo.get_extensao_do_arquivo()
        if extensao_do_arquivo == '.jpg' or extensao_do_arquivo == '.jpeg' or extensao_do_arquivo == '.png' or extensao_do_arquivo == '.gif' or extensao_do_arquivo == '.mov' or extensao_do_arquivo == '.JPG' or extensao_do_arquivo == '.JPEG' or extensao_do_arquivo == '.PNG' or extensao_do_arquivo == '.GIF' or extensao_do_arquivo == '.avi' or extensao_do_arquivo == '.mp4' or extensao_do_arquivo == '.AVI' or extensao_do_arquivo == '.MP4' or extensao_do_arquivo == '.MOV':
            return True
        return False

    
    def verificar_padrao_de_fotos_e_videos(self, arquivo):
        padrao_do_nome1 = re.compile(r'^(\D+)(\d+)(\.\D\D[0-9a-zA-Z]+)$')
        #padrao_do_nome2 = re.compile(r'^(\d\d\d\d)_(\d\d)_(\d\d)_([0-9a-zA-Z])+_(\d\d\d\d)(\.\D\D[0-9a-zA-Z])$') - sem o _ no local
        padrao_do_nome2 = re.compile(r'^(\d\d\d\d)_(\d\d)_(\d\d)_([0-9a-zA-Z_])+_(\d\d\d\d)(\.\D\D[0-9a-zA-Z])$')

        nome_do_arquivo_sem_extensao1 = padrao_do_nome1.search(arquivo.get_nome_arquivo())
        nome_do_arquivo_sem_extensao2 = padrao_do_nome2.search(arquivo.get_nome_arquivo())

        try:
            if self.validar_fotos_e_videos(arquivo) == True:
                if nome_do_arquivo_sem_extensao1 != None:
                    nome_parte_numerica = nome_do_arquivo_sem_extensao1.group(2)
                else:
                    nome_parte_numerica = nome_do_arquivo_sem_extensao2.group(5)
            else:
                nome_parte_numerica = ''
                print('O arquivo ' + arquivo.get_nome_arquivo() + ' não foi renomeado! Ele não é imagem ou video!')

        except AttributeError:
            nome_parte_numerica = ''
            print('O arquivo ' + arquivo.get_nome_arquivo() + ' não foi renomeado! O nome do arquivo está fora do padrão!')
            
        return nome_parte_numerica


    def separar_data_e_hora_digitadas(self, data_hora):
        data, hora = data_hora.split('-')
        return data, hora
