from this import d
from docxtpl import DocxTemplate
import pandas as pd 
import os

data = pd.read_csv('DATA_PRINCEPS.csv', encoding='utf-8')

months = ['','Enero', 'Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

for dt in data.index:
    #CONTRACT_PRINCEPS      =   DocxTemplate("layouts/CONTRATO_PRINCEPS_1.docx")
    CONTRACT_PRINCEPS      =   DocxTemplate("layouts/PLANTILLA_FINAL.docx")

    date_credit_fs = data['FECHA CREDITO FS'][dt].split('/')
    date_text_credit_fs = date_credit_fs[0] + ' de ' + months[int(date_credit_fs[1])] + ' de ' + date_credit_fs[2]

    date_pay = data['FECHA PAGARE'][dt].split('/')
    date_text_pay = date_pay[0] + ' de ' + months[int(date_pay[1])] + ' de ' + date_pay[2]

    date_validity = data['FECHA VIGENCIA'][dt].split('/')
    date_text_validity = date_validity[0] + ' de ' + months[int(date_validity[1])] + ' de ' + date_validity[2]

    date_signature = data['FECHA FIRMA'][dt].split('/')
    date_text_signature = date_signature[0] + ' de ' + months[int(date_signature[1])] + ' de ' + date_signature[2]
    


   
    


    context = {
        'NOMBRE_COMPLETO'   :   data['NOMBRE'][dt],
        'DOMICILIO'         :   data['DIRECCION COMPLETA'][dt],
        'CLIENTE'           :   data['CLIENTE'][dt],
        'REFERENCIA'        :   data['REFERENCIA'][dt],
        'CREDITO_FS'        :   data['CREDITO FS'][dt],
        'FECHA_CREDITO_FS'  :   date_text_credit_fs,       
        'MONTO_FS_NUM'      :   data['MONTO FS NUMERO'][dt],
        'MONTO_FS_LETRA'    :   data['MONTO FS LETRA'][dt],

        'CREDITO_PRINCEPS'  :   data['CREDITO PRINCEPS'][dt],
        'ADEUDO'            :   data['ADEUDO'][dt],
        'ADEUDO_LETRA'      :   data['ADEUDO LETRA'][dt],
        'INTERESES'         :   data['INTERESES'][dt],
        'INTERESES_LETRA'   :   data['INTERESES LETRA'][dt],
        'TASA_ANUAL'        :   data['TASA ANUAL'][dt],
        'TASA_ANUAL_LETRA'  :   data['TASA ANUAL LETRA'][dt],
        'MENSUALIDAD'       :   data['MENSUALIDAD'][dt],
        'ADEUDO_MAS_INTERESES'   :   data['ADEUDO MAS INTERESES'][dt],
        'FECHA_PAGARE'      :   date_text_pay,
        'FECHA_VIGENCIA'    :   date_text_validity,
        'FECHA_FIRMA'       :   date_text_signature,

        'VIN'               :   data['VIN'][dt],
        'MOTOR'             :   data['MOTOR'][dt],
        'MARCA'             :   data['MARCA'][dt],
        'MODELO'            :   data['MODELO'][dt],
        'COLOR'             :   data['COLOR'][dt],

        'REP_PRINCEPS'      :   data['REPRESENTANTE DE PRINCEPS'][dt],
        'REP_OSER'          :   data['REPRESENTANTE DE PRINCEPS'][dt],
        'REP_FINSUS'        :   data['REPRESENTANTE DE PRINCEPS'][dt],
        'NO_CUENTA'         :   data['NO DE CUENTA'][dt],
        'CLABE_BANCARIA'    :   data['CLABE BANCARIA'][dt],
        'INST_FINANCIERA'   :   data['INSTITUCION FINANCIERA'][dt]
    }   

    fileDir = 'contratos/'


    CONTRACT_PRINCEPS.render(context)
    CONTRACT_PRINCEPS.save(fileDir + '/' + str(data['NOMBRE'][dt]) + "_" + str(data['CREDITO FS'][dt]) + "_" + str(data['MENSUALIDAD'][dt]) + ".docx")



