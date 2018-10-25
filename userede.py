#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep, strftime
from io import open
import os
import json


# remove os arquivos ANTES de salvá-lo dnv
if os.path.isfile('tabelaResumo.json'):
    os.remove("tabelaResumo.json")
if os.path.isfile('consultarExtratos.json'):
    os.remove("consultarExtratos.json")


def write(data,file):
    # BASE_DIR = os.path.dirname(__file__)
    # with open(os.path.join(BASE_DIR, 'data.json'), 'w') as outfile:
    with open(file, 'a', encoding='utf8') as outfile:
        str_ = json.dumps(data,
                            indent=4, sort_keys=True,
                            separators=(',', ': '), ensure_ascii=False)
        outfile.write(str_)


def main(driver, datas):
    url = 'http://www.userede.com.br/login/'
    driver.get(url)

    login = driver.find_element_by_name('usuario')
    senha = driver.find_element_by_name('senha')
    botao = driver.find_element_by_xpath('//*[@id="frmLogin"]/button')

    login.send_keys()
    senha.send_keys()
    botao.send_keys(Keys.ENTER)

    wait = WebDriverWait(driver, 15)

    wait.until(EC.title_contains("Portal - Home"))

    url = 'https://www.userede.com.br/sites/fechado/extrato/Paginas/pn_relatorios.aspx'
    driver.get(url)

    wait.until(EC.element_to_be_clickable((
        By.ID, 'ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_filtroControl_ddlRelatorioSelectBoxItContainer')
    ))

    driver.find_element_by_xpath(
        '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_filtroControl_ddlRelatorioSelectBoxItArrowContainer"]'
    ).click()

    driver.find_element_by_xpath(
        '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_filtroControl_ddlRelatorioSelectBoxItOptions"]/li[1]/a/span'
    ).click()

    sleep(1)

    driver.find_element_by_xpath(
        '// *[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_filtroControl_consultaPV_ddlTipoAssociacaoSelectBoxItArrowContainer"]'
    ).click()

    driver.find_element_by_xpath(
        '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_filtroControl_consultaPV_ddlTipoAssociacaoSelectBoxItOptions"]/li[1]/a/span'
    ).click()

    sleep(1)

    dt_inicio = driver.find_element_by_xpath(
        '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_filtroControl_txtDataInicial"]'
    )
    dt_inicio.click()
    dt_inicio.send_keys(datas[0]['dia_inicial'])
    dt_inicio.send_keys(datas[1]['mes_inicial'])
    dt_inicio.send_keys(datas[2]['ano_inicial'])
    dt_fim = driver.find_element_by_xpath(
        '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_filtroControl_txtDataFinal"]'
    )
    dt_fim.send_keys(datas[3]['dia_final'])
    dt_fim.send_keys(datas[4]['mes_final'])
    dt_fim.send_keys(datas[5]['ano_final'])

    sleep(1)

    driver.find_element_by_xpath(
        '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_filtroControl_btnBuscar"]'
    ).click()

    try:
        total_no_período_valor_bruto = driver.find_elements_by_xpath(
            '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_RelatorioCredito_rcTotalizadores_qiValoresConsolidados"]/div[2]/div/div[1]/div[2]'
        )[0]
    except:
        print('Não há movimento para o período informado!')
        # write(u'Não há movimento para o período informado!'.upper())
        return
        
    total_no_período_valor_bruto = total_no_período_valor_bruto.text
    
    total_no_periodo_valor_liquido = driver.find_elements_by_xpath(
        '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_RelatorioCredito_rcTotalizadores_qiValoresConsolidados"]/div[2]/div/div[2]/div[2]'
    )[0]
    total_no_periodo_valor_liquido = total_no_periodo_valor_liquido.text

    valores_consolidados = {
        'total_no_período_valor_bruto': total_no_período_valor_bruto,
        'total_no_periodo_valor_liquido': total_no_periodo_valor_liquido
    }
    total_por_bandeira = []
    total_bandeiras = driver.find_elements_by_xpath(
        '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_RelatorioCredito_rcTotalizadores_pnlTotaisBandeira"]/div[2]/div[1]'
    )
    for row in total_bandeiras:
        for cont in range(1,10):
            try:
                nome_bandeira = row.find_elements_by_xpath(
                    u'//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_RelatorioCredito_rcTotalizadores_pnlTotaisBandeira"]/div[2]/div[{}]/div[2]/div[1]'
                    .format(cont)
                )[0]
                nome_bandeira  = nome_bandeira.text
                valor_bandeira = row.find_elements_by_xpath(
                    u'//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_RelatorioCredito_rcTotalizadores_pnlTotaisBandeira"]/div[2]/div[{}]/div[2]/div[2]'
                    .format(cont)
                )[0]
                valor_bandeira = valor_bandeira.text
                bandeira = {
                    nome_bandeira: valor_bandeira
                }
                total_por_bandeira.append(bandeira)
            except:
                break
        break
    
    tbody = '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_RelatorioCredito_dvRelatorio"]/table/tbody/tr'
    '''
    cont = 1
    actions = ActionChains(driver)
    for row in driver.find_elements_by_xpath(tbody):
        cell = row.find_element_by_xpath(
            u'//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_RelatorioCredito_dvRelatorio"]/table/tbody/tr[{}]/td[5]/a'
            .format(cont)
        )
        print(u'{}  -  {}'.format(cell.text, cont))
        # cell.click()

        # abre a aba
        actions.key_down(Keys.CONTROL).click(cell).key_up(Keys.CONTROL).perform()

        # alterna para aba aberta
        driver.switch_to.window(driver.window_handles[-1])
        
        # element_present = EC.presence_of_element_located(
        #     (By.XPATH,
        #      '//*[@id="ctl00_m_g_319a4cca_3fcc_42ba_97b4_c15b0874c184_ctl00_lblTitulo"]'
        #      )
        # )
        # WebDriverWait(driver, 10).until(element_present)
        
        pagina_final(driver)
        
        cont+=1
    '''
    '''
    # Tempo que o Selenium vai ficar verificando a página.
    driver.implicitly_wait(30)
    try:
        # Buscando elemento pela id.
        elemento = driver.find_element_by_id('id_2')
    except Exception as e:
        print('Nao foi dessa vez :(', e)
    else:
        print('Elememento encontrado:')
        print(elemento)
    finally:
        # Fechando a janela do navegador
        driver.quit()
    '''
    
    relatórioVendas = {}
    dados = 0
    for row in driver.find_elements_by_xpath(tbody):
        nro_estabelecimento = row.find_elements_by_tag_name("td")[0].text
        data_d_venda = row.find_elements_by_tag_name("td")[1].text
        data_de_recebimento = row.find_elements_by_tag_name("td")[2].text
        prazo_de_recebimento = row.find_elements_by_tag_name("td")[3].text
        resumo_vendas = row.find_elements_by_tag_name("td")[4].text
        qt_vendas = row.find_elements_by_tag_name("td")[5].text
        modalidade = row.find_elements_by_tag_name("td")[6].text
        bandeira = row.find_elements_by_tag_name("td")[7].text
        valor_bruto = row.find_elements_by_tag_name("td")[8].text
        valor_descontado = row.find_elements_by_tag_name("td")[9].text
        correcoes = row.find_elements_by_tag_name("td")[10].text
        valor_liquido = row.find_elements_by_tag_name("td")[11].text
        itens = {
            'nro_do_estabelec.': nro_estabelecimento,
            'data_da_venda': data_d_venda,
            'data_de_receb': data_de_recebimento,
            'prazo_de_receb': prazo_de_recebimento,
            'resumo_de_vendas': resumo_vendas,
            'qtde_de_vendas': qt_vendas,
            'modalidade': modalidade,
            'bandeira': bandeira,
            'valor_bruto': valor_bruto,
            'valor_descontado': valor_descontado,
            'correcoes': correcoes,
            'valor_liquido': valor_liquido,
        }
        relatórioVendas[dados] = itens
        dados += 1

    tfoot = '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_RelatorioCredito_dvRelatorio"]/table/tfoot'
    for row in driver.find_elements_by_xpath(tfoot):
        total_coluna_valor_bruto = row.find_elements_by_tag_name("td")[1].text
        total_coluna_valor_descontado = row.find_elements_by_tag_name("td")[2].text
        total_coluna_correcoes = row.find_elements_by_tag_name("td")[3].text
        total_coluna_valor_liquido = row.find_elements_by_tag_name("td")[4].text
        total_no_periodo = {
            'total_coluna_valor_bruto': total_coluna_valor_bruto,
            'total_coluna_valor_descontado': total_coluna_valor_descontado,
            'total_coluna_correcoes': total_coluna_correcoes,
            'total_coluna_valor_liquido': total_coluna_valor_liquido,
        }

    data = {
        'relatorio_de_vendas_credito': relatórioVendas,
        'total_no_periodo': total_no_periodo,
        'valores_consolidados': valores_consolidados,
        'total_por_bandeira': total_por_bandeira,
    }
    write(data, "consultarExtratos.json")


def pagina_final(driver):
    print(u'PÁGINA FINAL')
    driver.switch_to_window(driver.window_handles[0])
    return

    data_da_venda = driver.find_elements_by_xpath(
        '//*[@id="ctl00_m_g_319a4cca_3fcc_42ba_97b4_c15b0874c184_ctl00_resumoCreditoControl_sumario"]/div/div[1]/div/div/div[1]'
    )[0]
    data_da_venda = data_da_venda.text

    data_do_processamento = driver.find_elements_by_xpath(
        '//*[@id="ctl00_m_g_319a4cca_3fcc_42ba_97b4_c15b0874c184_ctl00_resumoCreditoControl_sumario"]/div/div[1]/div/div/div[2]/div[2]'
    )[0]
    data_do_processamento = data_do_processamento.text

    resumo_vendas = driver.find_elements_by_xpath(
        '//*[@id="ctl00_m_g_319a4cca_3fcc_42ba_97b4_c15b0874c184_ctl00_resumoCreditoControl_sumario"]/div/div[1]/div/div/div[3]/div[2]'
    )[0]
    resumo_vendas = resumo_vendas.text

    bandeira = driver.find_elements_by_xpath(
        '//*[@id="ctl00_m_g_319a4cca_3fcc_42ba_97b4_c15b0874c184_ctl00_resumoCreditoControl_sumario"]/div/div[2]/div/div/div[1]/div[2]'
    )[0]
    bandeira = bandeira.text

    qtde_de_vendas = driver.find_elements_by_xpath(
        '//*[@id="ctl00_m_g_319a4cca_3fcc_42ba_97b4_c15b0874c184_ctl00_resumoCreditoControl_sumario"]/div/div[2]/div/div/div[2]/div[2]'
    )[0]
    qtde_de_vendas = qtde_de_vendas.text

    valor_bruto = driver.find_elements_by_xpath(
        '//*[@id="ctl00_m_g_319a4cca_3fcc_42ba_97b4_c15b0874c184_ctl00_resumoCreditoControl_sumario"]/div/div[2]/div/div/div[3]/div[2]'
    )[0]
    valor_bruto = valor_bruto.text

    valor_descontado = driver.find_elements_by_xpath(
        '//*[@id="ctl00_m_g_319a4cca_3fcc_42ba_97b4_c15b0874c184_ctl00_resumoCreditoControl_sumario"]/div/div[3]/div/div/div[1]/div[2]'
    )[0]
    valor_descontado = valor_descontado.text

    valor_liquido = driver.find_elements_by_xpath(
        '//*[@id="ctl00_m_g_319a4cca_3fcc_42ba_97b4_c15b0874c184_ctl00_resumoCreditoControl_sumario"]/div/div[3]/div/div/div[2]/div[2]'
    )[0]
    valor_liquido = valor_liquido.text

    taxa_de_embarque = driver.find_elements_by_xpath(
        '//*[@id="ctl00_m_g_319a4cca_3fcc_42ba_97b4_c15b0874c184_ctl00_resumoCreditoControl_sumario"]/div/div[3]/div/div/div[3]/div[2]'
    )[0]
    taxa_de_embarque = taxa_de_embarque.text

    resumo = {
        'data_da_venda': data_da_venda,
        'data_do_processamento': data_do_processamento,
        'resumo_vendas': resumo_vendas,
        'bandeira': bandeira,
        'qtde_de_vendas': qtde_de_vendas,
        'valor_bruto': valor_bruto,
        'valor_descontado': valor_descontado,
        'valor_liquido': valor_liquido,
        'taxa_de_embarque': taxa_de_embarque
    }
    
    itens_vencimetos = {}    
    tbody = '//*[@id="tbVencimento"]/tbody/tr'
    dados = 0
    for row in driver.find_elements_by_xpath(tbody):
        data_recebimento = row.find_elements_by_tag_name("td")[0].text
        numero_estabelecimento = row.find_elements_by_tag_name("td")[1].text
        ordem_credito = row.find_elements_by_tag_name("td")[2].text
        status_do_resumo = row.find_elements_by_tag_name("td")[3].text
        data_da_antecipacao = row.find_elements_by_tag_name("td")[4].text
        valor_liquido = row.find_elements_by_tag_name("td")[5].text
        vencimento = {
            'data_de_recebimento': data_recebimento,
            'numero_do_estabelecimento': numero_estabelecimento,
            'ordem_de_credito': ordem_credito,
            'status_do_resumo': status_do_resumo,
            'data_da_antecipacao': data_da_antecipacao,
            'valor_liquido': valor_liquido
        }
        itens_vencimetos[dados] = vencimento
        dados += 1
    
    itens_vendas = {}
    tbody = '//*[@id="tbVendasAceitas"]/tbody/tr'
    dados = 0
    for row in driver.find_elements_by_xpath(tbody):
        comprovante = row.find_elements_by_tag_name("td")[1].text
        nro_cartao = row.find_elements_by_tag_name("td")[2].text
        cartao = row.find_elements_by_tag_name("td")[3].text
        pais = row.find_elements_by_tag_name("td")[4].text
        dt_venda = row.find_elements_by_tag_name("td")[5].text
        hora = row.find_elements_by_tag_name("td")[6].text
        valor_bruto = row.find_elements_by_tag_name("td")[7].text
        parcelas = row.find_elements_by_tag_name("td")[8].text
        nro_estabelecimento = row.find_elements_by_tag_name("td")[9].text
        tipo_de_captura = row.find_elements_by_tag_name("td")[10].text
        venda_cancelada = row.find_elements_by_tag_name("td")[11].text
        venda = {
            'nro_do_comprovante_de_venda_(NSU)': comprovante,
            'nro_cartao_ou_ID_carteira_digital': nro_cartao,
            'cartao_virtual(tokenizacao)': cartao,
            'pais_de_origem': pais,
            'data_da_venda': dt_venda,
            'hora': hora,
            'valor_bruto': valor_bruto,
            'qtde_de_parcelas': parcelas,
            'nro_estabelec': nro_estabelecimento,
            'tipo_de_captura': tipo_de_captura,
            'venda_cancelada': venda_cancelada 
        }
        itens_vendas[dados] = venda
        dados+=1


    # Write JSON file
    data = {
        'resumo_de_vendas-cartoes_de_credito': resumo,
        'vencimentos': itens_vencimetos,
        'comprovantes_de_vendas_aceitos': itens_vendas,
    }
    
    write(data, "tabelaResumo.json")
    return 

    
    # element_present = EC.presence_of_element_located(
    #     (By.XPATH,
    #         '//*[@id="ctl00_m_g_99009a3a_150b_4bb6_8338_75cdeaf73726_ctl00_RelatorioCredito_dvRelatorio"]/table/tbody/tr[1]/td[5]/a'
    #         )
    # )
    # WebDriverWait(driver, 10).until(element_present)
    # driver.implicitly_wait(30)
    # driver.close()

def number_or_empty(texto):
    while True:
        try:
            dados = ''
            dados = input(u'Digite {}:'.format(texto))
            if dados == '':
                break
            # print(u'Dados.: {}'.format(dados))
            dados = int(dados)
            break
        except:
            print("Digite só NÚMEROS")
    return dados

def colocar_zero_inicio(dados):
    # print(u'colocar_zero_inicio.: {}'.format(dados))
    if len(str(dados)) < 2 and not dados == '':
        dados = '0' + str(dados)
    return dados


if __name__ == "__main__":
    print()
    print("DIGITE AS DATAS PARA CONSULTA")  
    print()
    dia_inicial = colocar_zero_inicio(number_or_empty('DIA INICIAL'))
    mes_inicial = colocar_zero_inicio(number_or_empty('MÊS INICIAL'))
    ano_inicial = number_or_empty('ANO INICIAL')
    dia_final = colocar_zero_inicio(number_or_empty('DIA FINAL'))
    mes_final = colocar_zero_inicio(number_or_empty('MÊS FINAL'))
    ano_final = number_or_empty('ANO FINAL')
    if (dia_inicial == '') or (dia_inicial is None):
        dia_inicial = colocar_zero_inicio(int(strftime('%d')))
    if (mes_inicial == '') or (mes_inicial is None):
        mes_inicial = colocar_zero_inicio(int(strftime('%m')))
    if (ano_inicial == '') or (ano_inicial is None):
        ano_inicial = int(strftime('%Y'))
    if (dia_final == '') or (dia_final is None):
        dia_final = colocar_zero_inicio(int(strftime('%d')))
    if (mes_final == '') or (mes_final is None):
        mes_final = colocar_zero_inicio(int(strftime('%m')))
    if (ano_final == '') or (ano_final is None):
        ano_final = int(strftime('%Y'))
    datas = [ 
        {'dia_inicial' : dia_inicial},
        {'mes_inicial' : mes_inicial},
        {'ano_inicial' : ano_inicial},
        {'dia_final' : dia_final},
        {'mes_final' : mes_final},
        {'ano_final': ano_final}
    ]
    driver = webdriver.Chrome()
    main(driver,datas)
