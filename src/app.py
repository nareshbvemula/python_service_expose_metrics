from flask import Flask, Response
import time , requests
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client.exposition import CONTENT_TYPE_LATEST
import prometheus_client


HTTP_ERROR = "https://httpstat.us/503"
HTTP_SUCCESS = "https://httpstat.us/200"

app = Flask(__name__)


class CustomCollector(object):
    def __init__(self):
        pass

    def url_resp( self, URL ):
        start_time = time.time ( )
        result = requests.get ( URL )
        print ( "Response Code: " , result.status_code )
        time_diff = time.time ( ) - start_time
        if result.status_code == 503:
            response_code = 0
        else:
            response_code = 1
        return time_diff, response_code

    def collect(self):
        g = GaugeMetricFamily("sample_external_url_up", 'Help text', labels=['url'])
        c = GaugeMetricFamily ( "sample_external_url_response_ms" , 'URl Response in ms' , labels=[ 'url' ])

        t,r = self.url_resp(HTTP_ERROR)

        g.add_metric ( [ HTTP_ERROR ] , r )
        c.add_metric([HTTP_ERROR], t )

        t , r = self.url_resp ( HTTP_SUCCESS )
        g.add_metric ( [ HTTP_SUCCESS ] , r )
        c.add_metric([HTTP_SUCCESS], t )

        yield g
        yield c


@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    REGISTRY.register ( CustomCollector ( ) )
    app.run(host='0.0.0.0')
