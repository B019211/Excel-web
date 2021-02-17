#Excel用ライブラリの読み込み
import openpyxl

#Excelファイルを開く
v_wb=openpyxl.load_workbook('.\交通費.xlsx')

#アクティブなシートを変数へ
v_ws = v_wb.active

for i in range(2,v_ws.max_row+1):

    #b列(出発駅)を変換へ
    v_Excelfrom = v_ws['b'+str(i)].value
    
    #c列(到着駅)を変換へ
    v_Excelto = v_ws['c'+str(i)].value
    
    #ブラウザ用ライブラリの読み込み
    from selenium import webdriver
    
    #Edge用ドライバの読み込み
    v_browser = webdriver.Edge(executable_path='C:\Devlopment\Python\Python38\etc\msedgedriver.exe')

    #路線検索サイトを開く
    v_browser.get('http://transit.yahoo.co.jp')

    #サイトの出発駅の場所を特定
    v_sfrom = v_browser.find_element_by_id('sfrom')

    #出発駅を入力
    v_sfrom.send_keys(v_Excelfrom)

    #サイトの到着駅の場所を特定
    v_sto = v_browser.find_element_by_id('sto')

    #到着駅を入力
    v_sto.send_keys(v_Excelto)

    #検索ボタンを押す
    v_sto.submit()

    #運賃を取得し、円を取り除く
    v_fare = v_browser.find_element_by_class_name('fare').text.replace('円','')

    #運賃からカンマを取り除く
    v_fare_int = v_fare.replace(',','')

    #Excelへの書き込み
    v_ws['e'+str(i)].value = int(v_fare_int)

    #ブラウザを閉じる
    v_browser.close()

#Excelファイルを保存する
v_wb.save('.\交通費.xlsx')
