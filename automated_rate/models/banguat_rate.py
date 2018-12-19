from odoo import api, fields, models, SUPERUSER_ID
#Import logger
import logging
import time
import zeep
import datetime
import pytz
#Get the logger
_logger = logging.getLogger(__name__)
class BanguatRate(models.Model):
    _name = 'banguat.rate'
    
    name = fields.Char(string=" ")    
    @api.model
    def get_daily_rate(self):
        self.currency_gtq_id = self.env.ref("base.GTQ").id

        today_date = datetime.datetime.now(pytz.timezone('America/Guatemala')).__format__('%Y-%m-%d')

        rateCount = self.env['res.currency.rate'].search_count([('name', '=', today_date),('currency_id','=',self.currency_gtq_id)])

        _logger.info('line: The rate for today is  already registered')
        
        if rateCount==0:
            second_wsdl = 'http://www.banguat.gob.gt/variables/ws/TipoCambio.asmx?WSDL'
            client = zeep.Client(wsdl=second_wsdl)
            service_response = client.service.TipoCambioDia()
            rate_date = service_response['CambioDolar']['VarDolar'][0]['fecha']
            rate_value = service_response['CambioDolar']['VarDolar'][0]['referencia']

            strRate = repr(rate_value)
            strGTQ = str(self.currency_gtq_id)
            _logger.info('line: WSLD Response '+ rate_date + '-----' + strRate + ' GTQid: ' +strGTQ)

            self.env['res.currency.rate'].create({
                'name': rate_date,
                'rate': rate_value,
                'currency_id': self.currency_gtq_id,
            })    
        