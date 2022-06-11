#Libraries
import pandas as pd
import numpy as np
import datetime as dt
import re

# Generate the table Applicants in DataFrame format to posteriorly submit to GPE DataBase
def transfrom_applicants_table(form_data: str, year: int,table_column_names: dict):
    """
        INPUT
    form_data: excel file from the google form
    year: year of application (only the last two digits, e.g, 20,21,22,...,)
    table_columns_names: Address each column index from the google form excel to each column from the Applicants Table in the database
            E.g, new_column_names = {2:'name', 3:'email', 4:'student_id',.......,}
                                   
    """

    #Generating student code
    #CAUTION! 
    df_full = pd.read_excel(form_data, header = 0)
    df_full['Nome Completo:'] = df_full['Nome Completo:'].str.strip().str.upper()

    names = list(df_full['Nome Completo:'].sort_values().values)
    student_code = {}
    code = 0
    for name in names:
        student_code.setdefault(name,str(code + 1000) + str(year))
        code +=1
    student_code = {'AHRON ROGERIO CANOSSA': '100022',
        'ALESSANDRA BIANCA MASSELLI': '100122',
        'ALISSON SCARPINATTI LEME': '100222',
        'ANA BEATRIZ VIEIRA': '100322',
        'ANA CLARA FARIA KAWAHARA': '100422',
        'ANA CLARA FERREIRA SENA': '100522',
        'ANA JULIA NEVES DA SILVA': '100622',
        'ANA JULIA PEREZ REINA': '100722',
        'ANA LUIZA QUINTANA PINTO': '100822',
        'ANA VITÓRIA FERREIRA DAMACENO': '100922',
        'ANDRESSA AMAYA SOARES SCHELER': '101022',
        'ANDRESSA OLIVEIRA NUNES': '101122',
        'ANDRÉ SANTANA RODRIGUES JUNIOR': '101222',
        'ANGELINE REDÍGOLO CARDOSO': '101322',
        'AUGUSTO SPEDO NEVES': '101422',
        'BEATRIZ ANDRADE VALVERDE': '101522',
        'BEATRIZ MIYUKI ANTUNES': '101622',
        'BEATRIZ VIDAL SCABELO': '101722',
        'BIANCA BONINE DE SOUZA': '101822',
        'BRUNO DE SOUZA': '101922',
        'CAICK BEGATTI DE SOUZA': '102022',
        'CARLA VITÓRIA SIMÕES': '102122',
        'CARLITO GOMES SAMPAIO JÚNIOR': '102222',
        'CARLOS ROBERTO DE MATTOS': '102322',
        'DANIELLE REBECCHI FERREIRA': '102422',
        'DANILO LIMA': '102522',
        'DEREK MATEUS DE OLIVEIRA': '102622',
        'DEYVISON DA SILVA SOUZA': '102722',
        'EDUARDA COELHO CHIQUITELLI': '102822',
        'EMILYM OLIVEIRA': '102922',
        'EVELYN CAROLINA CAMPOS TEIXEIRA': '103022',
        'FERNANDO JOSÉ HELENO DORNELAS': '103122',
        'FERNANDO RODRIGUES DO PRADO': '103222',
        'FRANCIELE DE SOUZA BENEDICTO': '103322',
        'FRANCIELLI CONCEIÇÃO DA SILVA': '103422',
        'GABRIEL DIAS MENDONÇA': '103522',
        'GABRIEL HENRIQUE ESQUETINI': '103622',
        'GABRIELA FERNANDA BENTO ALVES': '103722',
        'GABRIELLY GIACOMINO': '103822',
        'GEOVANA CERASUOLO PADILHA': '103922',
        'GIOVANA AMARAL PERNA': '104022',
        'GIOVANA BENEDINI PINTO': '104122',
        'GIOVANA DE OLIVEIRA SOUZA': '104222',
        'GIOVANA FINCOLO GONÇALVES': '104322',
        'GIOVANE DESTEFANI': '104422',
        'GIOVANNA SERAFIM': '104522',
        'GUSTAVO SANTOS VOLTOLINO': '104622',
        'HELENA FARIAS': '104722',
        'HUGO RODRIGUES DA SILVA': '104822',
        'INDIANARA EDUARDA ARAÚJO DA SILVA': '104922',
        'ISABELA BEATRIZ BRANDÃO GABRIEL': '105022',
        'ISABELA GINES': '105122',
        'ISABELLA FERNANDA DE SOUZA': '105222',
        'ISADORA CRISTINA RODRIGUES': '105322',
        'JEFERSON CRISTIANO DIAS': '105422',
        'JORGE MENDONÇA BORGES': '105522',
        'JOSÉ ARMANDO PEDRO DA SILVA': '105622',
        'JOÃO GABRIEL MENDONÇA CASARINE': '105722',
        'JOÃO PAULO DOS SANTOS NOLI': '105822',
        'JOÃO PEDRO ALVES': '105922',
        'JOÃO PEDRO DE PAULA MARTINS': '106022',
        'JOÃO VICTOR DINIZ CONRADO': '106122',
        'JULIA GONÇALVES NASCIMENTO': '106222',
        'JULYA GABRIELI CHIARENTIN': '106322',
        'JÉSSICA RIBEIRO DE PÁDUA': '106422',
        'JÚLIA GRABER PEREIRA': '106522',
        'JÚLIA MAGALHÃES VAZ DA SILVA': '106622',
        'KAILANE ALVES OLIVEIRA': '106722',
        'KAMILLY CHIQUITELLI': '106822',
        'KAMILY VITÓRIA SIMEÃO': '106922',
        'KAYLANE EDUARDA CUCCO': '107022',
        'KELVYN MOREIRA ROSA': '107122',
        'KENEDY JAISLOM TELES LEITE': '107222',
        'LARISSA DO PRADO GOMES': '107322',
        'LAÍS CRISTINY PEREIRA POSSA': '107422',
        'LETÍCIA BEATRIZ DE BRITO PEREIRA': '107522',
        'LETÍCIA BIANCA DE MEDEIROS': '107622',
        'LETÍCIA DAIANE FURLAN DA SILVA': '107722',
        'LETÍCIA DE CÁSSIA BORTOLANI': '107822',
        'LETÍCIA FERREIRA DA SILVA': '107922',
        'LETÍCIA NATHAMI M. DA COSTA': '108022',
        'LILLIAN GABRIELY DA MOTA FERREIRA': '108122',
        'LUAN IZAC DA SILVA': '108222',
        'LUANA MARTINS SCHWARTZ': '108322',
        'LÉIA MARINHO ROMITTI': '108422',
        'MARCOS DANIEL DOS SANTOS AMARAL': '108522',
        'MARIA CLARA BUSSOLA FERREIRA': '108622',
        'MARIA EDUARDA DE LIMA': '108722',
        'MARIA EDUARDA DE OLIVEIRA MACHADO': '108822',
        'MARIA EDUARDA LOPES': '108922',
        'MARIA EDUARDA MOURA MELETTO': '109022',
        'MARIA EDUARDA RIBEIRO SILVA': '109122',
        'MARIA EDUARDA SCHIAVETTO': '109222',
        'MARIA FERNANDA RODRIGUES': '109322',
        'MARIA LUIZA GONÇALVES': '109422',
        'MARIA VITÓRIA DOS SANTOS': '109522',
        'MARIA VITÓRIA GALIANI': '109622',
        'MARIANA BRANIAK MENDES': '109722',
        'MARIANA CAROLINA CALABREZ': '109822',
        'MARIANA RICCI VERONEZE': '109922',
        'MARINA DA SILVA MOTA': '110022',
        'MATHEUS MONTEIRO': '110122',
        'MATHEUS PEDRO MARTIN': '110222',
        'NAJLA STEFANI LIBORIO': '110322',
        'NARA NAZIRA ALVES ANTUNES GONÇALVES': '110422',
        'NICOLE CASSIANO DE OLIVEIRA': '110522',
        'NICOLE SILVA CARDOSO': '110622',
        'NICOLY KAROLAINY CUSTÓDIO': '110722',
        'PALOMA ELEN LEMOS DE SOUZA': '110822',
        'PAOLA BERTONHA MATOS': '110922',
        'PEDRO ANTÔNIO MEDEIROS BATISTA': '111022',
        'PEDRO HENRIQUE FERREIRA': '111122',
        'PEDRO HENRIQUE ZANINI SANTOS': '111222',
        'PÉROLA MELISSA NUNES DOS SANTOS': '111322',
        'RAFAEL VINICIUS DE LIMA CALERA': '111422',
        'RAFAELA DE SOUZA FALCONI': '111522',
        'RAIANY CRISTINA DOS SANTOS MENDES': '111622',
        'RAUL MIRANDA BENICIO': '111722',
        'RAUL MOREIRA FREITAS': '111822',
        'SAMUEL ZANONI ABERRACHID': '111922',
        'STÉFANI ALVES FERNANDES': '112022',
        'TAINARA CRISTINA BELINI': '112122',
        'THAISSA BIANCA MORATTA': '112222',
        'VALÉRIA CRISTINA DE OLIVEIRA': '112322',
        'VICTORIA CASSIA DA SILVA': '112422',
        'VICTORIA DA SILVA OLIVEIRA': '112522',
        'VICTORIA FERNANDA TASSI': '112622',
        'VICTÓRIA ROTA SOARES': '112722',
        'VITOR MONTREZOR SENTANIN': '112822',
        'VITÓRIA APARECIDA BONILHA MATEUS': '112922',
        'VITÓRIA CAROLINA GREGORIO': '113022',
        'VITÓRIA DAS MERCES BRAZ DOS SANTOS LOPES': '113122',
        'YANINA DA ROCHA LIZEO': '113222',
        'YASMIN ADRIELI DUARTE DE CARVALHO': '113322',
        'AMANDA VICENTE LADEIRA': '113422',
        'JOÃO GABRIEL SELESTRINO ALVES': '113522',
        'JOÃO FRANCISCO BORDINI FERREIRA': '113622',
        'THAÍS BONFIM MALINPENCI': '113722'}


    #Inserting student code into the dataframe
    df_full['code'] = df_full["Nome Completo:"].apply(lambda name: student_code[name] if name in list(student_code.keys()) else np.nan)
    df_full.dropna(subset = ['code'], axis = 0, how = 'any', inplace = True)
    df_full = df_full.sort_values(by ='code', ascending = True)

    #Reordering columns
    columns = list(df_full.columns.values)
    new_order = columns[-1:] + columns[:-1]
    df_full = df_full[new_order]

    #Tranforming dataframe into the sql table designed
    old_column_names = dict(zip(new_order, range(len(new_order))))
    table_column_names.setdefault(0,'student_code')
    df_full = df_full.rename(columns = old_column_names).rename(columns = table_column_names)[list(table_column_names.values())]
    df_full['study_room'] = df_full['study_room'].apply(lambda x: 1 if x.strip() == 'Sim' else 0) #Only accepts boolean values
    return df_full[list(df_full.columns[-1:].values) + list(df_full.columns[:-1].values)].astype({'student_id': str})





# Generate the table Students in DataFrame format to posteriorly submit to GPE DataBase
def transform_students_table(excel_data: str):
    """
    INPUT
    
    excel_data: the proper excel file generated by the selection process algorithm, e.g.,'resultado_vest2022.xlsx'
    """
    df_student = pd.read_excel(excel_data)
    df_ranked_vest = df_student.nlargest(columns = ['final_score'], n = 60, keep= 'all')[['Code', 'NSE']]
    
    #assigning start date
    year = '20' + list(set(df_ranked_vest.Code.apply(lambda x: str(x)[-2:])))[0]
    start_date = dt.date(int(year),3,1)
    
    return df_ranked_vest.assign(start_date= start_date, end_date = None, volunteer_id = None).rename(columns ={'Code': 'student_code'})


#Generate the table Exams in DataFrame format to posteriorly submit to GPE DataBase
def transform_exams_table(file_name: str, answer_key: str, exame_number: 1):
    """
    INPUT
        file_name: excel file of students answers in GPE exams (
        answer_key: correct answers (.txt format)
        exame_number: number of the exame. (wW apply 3 exams over the year)
        
    """
    ###-----------------------loading raw data-----------------------------------------------###
    df_ans = pd.read_excel(file_name)
    df_key = pd.read_fwf(answer_key, widths = [1,2], header = None)

    ###--------------------------Data preparattion---------------------------------------------------###
    df_key = pd.read_fwf("GABARITO SIM 1 2022.txt", header = None)
    df_key['questions'] = df_key[0].apply(lambda x: (re.compile(r'\d+').search(x).group()).strip())
    df_key['answers'] = df_key[0].apply(lambda x: (re.compile(r'\D+').search(x).group()).strip())
    df_key = df_key[['questions', 'answers']]
    df_ans = df_ans.dropna(how = 'all', subset = df_ans.columns[2:], axis =0).fillna(value = 'X')


    #------------------------Computing performance segregated by subjects--------------------------------###
    df_full = df_ans.copy().T.iloc[2:,:]
    df_full.columns =  df_ans.copy().T.iloc[1,:].values
    df_full.index = list(map(lambda x:re.compile(r'\d+').search(x).group(), df_full.index))
    df_full = pd.merge(df_key,df_full, how ='inner', left_on = 'questions', right_index= True)

    #labeling 1 for correct answers and 0 for incorrect
    columns = df_full.columns[2:]
    for col in columns:
        df_full.loc[df_full['answers'] == df_full[col].str.upper(),col] = 1
        df_full[col] = df_full[col].apply(lambda x: 0 if x != 1 else x)

    df_full['subjects'] = df_full['questions'].apply(lambda var: 'geography' if var == '1' else ('biology'
                                                                                if var == '11' else ('chemistry'
                                                                                if var == '21' else ('history'
                                                                                if var == '31' else ('math'
                                                                                if var == '41' else ('physics'
                                                                                if var == '51' else ('literature'
                                                                                if var == '61' else ('portuguese'
                                                                                if var == '69' else ('english'
                                                                                if var == '77' else ('interdisciplinary')
                                                                            if var == '82' else np.nan))))))))).fillna(method = 'ffill')
    #Calculating  students performance (%)
    df_sub = df_full.iloc[:,2:].groupby(by ='subjects', axis = 0).sum()
    #df_sub['median'] = df_sub.median(axis = 1)
    
    #Data Type Requirements ---> subject columns: DECIMAL(5,4) ; student_code: CHAR(6)
    df_final = df_sub.T
    df_final = df_final.assign(geography = lambda x: round(x.geography/10,4),
                biology = lambda x: round(x.biology/10,4),
                chemistry = lambda x: round(x.chemistry/10,4),
                history = lambda x: round(x.history/10,4),
                math = lambda x: round(x.math/10,4),
                physics = lambda x: round(x.physics/10,4),
                literature = lambda x: round(x.literature/8,4),
                portuguese = lambda x: round(x.portuguese/8,4),
                english = lambda x: round(x.english/5,4),
                interdisciplinary = lambda x: round(x.interdisciplinary/9,4),
                exame_number = exame_number)

    df_final= df_final.reset_index().rename(columns = {'index': 'student_code'}).astype({'student_code': str})
    
    #reordering columns
    return df_final[['student_code',
                     'exame_number',
                     'geography',
                     'biology',
                     'chemistry',
                     'history',
                     'math',
                     'physics',
                     'portuguese',
                     'literature',
                     'english',
                     'interdisciplinary']].sort_values(by = 'student_code', ascending = True)


