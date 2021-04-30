from flask import Blueprint,request
from Decentraland.APIs import Dailyparcel
from Decentraland.APIs import Dailymanawon
from Decentraland.APIs import Historydetail
import json




bp= Blueprint('chathook',__name__,url_prefix='/')

@bp.route('/chathook',methods=['GET','POST'])
def chat():
    req= request.get_json(force=True)
    if req['queryResult']['intent']['displayName'] == 'CurrentPrice':
        result=Dailyparcel()
        result2=Dailymanawon()
        result=result['price']
        result3=result*result2
        senddata = '오늘의 1파셀의 평균가격은' + str(result) + ' MANA입니다.' + '1MANA의 가격은' + str(result2) + '원입니다.' + ' 1파셀의 평균가격을 원화로 환산하면' + \
                   str(result3) + ' 원입니다.'

    elif req['queryResult']['intent']['displayName'] == 'Date':
        date = req['queryResult']['queryText']
        result=Historydetail(date)
        senddata = date+ '의 1파셀의 평균가격은' + str(result['price']) + ' MANA입니다.' + ' 1MANA의 가격은' + str(result['mana per won'])+ '원입니다.' + ' 1파셀의 평균가격을 원화로 환산하면' + \
                   str(result['won price']) + ' 원입니다.'

    return {'fulfillmentText': senddata}
