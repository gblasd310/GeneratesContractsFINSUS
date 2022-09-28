from this import d
from docxtpl import DocxTemplate
import pandas as pd 
import os

data = pd.read_csv('', encoding='utf-8')

months = ['','Enero', 'Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

for dt in data.index:
    contract_princeps       =   DocxTemplate("layouts/PROPUESTA_CRA_PRINCEPS_VFINAL.docx")
    convenioDacionPago      =   DocxTemplate("layouts/CONVENIO DE DACIÓN EN PAGO_PRINCEPS.docx")
    sesNotifyOSER_FINSUS    =   DocxTemplate("layouts/NOTIFICACIÓN DE CESIÓN OSER_CC FINSUS_VFINAL.docx")
    sesNotifyOSER_FINSUS    =   DocxTemplate("layouts/NOTIFICACIÓN DE CESIÓN OSER_CC FINSUS_VFINAL.docx")
    contrato_princeps       =   DocxTemplate("layouts/CONTRATO_PRINCEPS_1.docx")
    
    date_text = data['fecha_pagare'][dt].split('/')
    date_text_pay = date_text[0] + ' de ' + months[int(date_text[1])] + ' de ' + date_text[2]
    


    creditos_antecs = data['creditos_antecs'][dt].split(',')
    sentence_credits = ''
    # si solo se tiene un credito
    if len(creditos_antecs) < 1:
        sentence_credits = 'quedó includo el credito {}'.format(creditos_antecs[0])
    else:
        sentence_credits = 'quedaron incluidos el'
        for c in creditos_antecs:
            var = ' crédito {},'.format(c)
            sentence_credits += var

    fecha_cred_antecs = data['fecha_cred_antecs'][dt]
    sentence_dates_credits = ''
    if len(fecha_cred_antecs) < 1:
        sentence_dates_credits = 'el pagaré de fecha {}'.format(fecha_cred_antecs[0])
        sentence_dates_credits += 'emitido'
    else:
        sentence_dates_credits = 'los pagarés de fechas'
        for var in fecha_cred_antecs:
            var_vars = var.split('/')
            text = var_vars[0] + ' de ' + months[int(var_vars[1])] + ' de '+ var_vars[2]
            sentence_dates_credits += ' {},'.format(text)
        sentence_dates_credits += 'emitidos'

    


    context = {
        'credito_original'  :   data['credito_original'][dt],
        'fecha_pagare'      :   date_text_pay,
        'fecha_antec'       :   data['fecha_antec'][dt],
        'credito_antec'     :   data['credito_antec'][dt],
        'nombre_acreditado' :   data['nombre_acreditado'][dt],
        'nombre_cliente'    :   data['nombre_cliente'][dt],
        'domicilio'         :   data['domicilio'][dt],
        'rep_princeps'      :   data['rep_princeps'][dt],
        'creditos_antecs'   :   sentence_credits,
        'fecha_cred_antecs' :   sentence_dates_credits,
        'monto_antec_num'   :   data['monto_antec_num'][dt],
        'monto_antec_letra' :   data['monto_antec_letra'][dt],
        'vin'               :   data['vin'][dt],
        'motor'             :   data['motor'][dt],
        'marca'             :   data['marca'][dt],
        'modelo_formato'    :   data['modelo_formato'][dt],
        'color'             :   data['color'][dt],
        'monto_adeudo_num'  :   data['monto_adeudo_num'][dt],
        'monto_adeudo_letra':   data['monto_adeudo_letra'][dt],
        'monto_adeudo_int_num':data['monto_adeudo_int_num'][dt],
        'monto_adeudo_int_letra':data['monto_adeudo_int_letra'][dt],
        'tasa_anual_num'    :   data['tasa_anual_num'][dt],
        'tasa_anual_letra'  :   data['tasa_anual_letra'][dt],
        'referencia_bancaria':  str(data['referencia_bancaria'][dt]).zfill(10),
        'clabe_bancaria'    :   data['clabe_bancaria'][dt],
        'institucion_financiera':data['institucion_financiera'][dt],
        'fecha_rec_adeudo'  :   data['fecha_rec_adeudo'][dt],
        'rep_oser'          :   data['rep_oser'][dt],
        'rep_finsus'        :   data['rep_finsus'][dt],
        'verbo_general'     :   'quedó incluido' if len(creditos_antecs) < 1 else 'quedarón incluidos',
        'sentencia_general' :   'en lo sucesivo el' if len(creditos_antecs) < 1 else 'todos ellos referidos conjuntamente como el',
        'verbo_general_2'   :   'mismo' if len(creditos_antecs) < 1 else 'mismos',
        'verbo_general_3'   :   'Crédito' if len(creditos_antecs) < 1 else 'Créditos',
        'verbo_general_4'   :   'fue incluido' if len(creditos_antecs) < 1 else 'fuerón incluidos',
        'sentencia_general_1':  'mismo que le fue otorgado inicialmente por' if len(creditos_antecs) < 1 else 'mismos que le fueron otorgados por ',
        'sentencia_general_2':  'del Crédito que le fue otorgado' if len(creditos_antecs) < 1 else 'de los Créditos que le fueron otorgados'
    
    }   

    fileDir = 'contratos/'

    try:
        os.stat('contratos/')
    except:
        os.mkdir('contratos/')
  
    try:
        os.stat(fileDir)
    except:
        os.mkdir(fileDir)

    contract_princeps.render(context)
    contract_princeps.save(fileDir + '/' )





