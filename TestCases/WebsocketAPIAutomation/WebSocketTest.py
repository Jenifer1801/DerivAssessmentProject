import json
import pandas as pd
from websocket import create_connection


def test_webSockTest():
    # Create connection and send data to Websockets
    ws = create_connection("wss://ws.derivws.com/websockets/v3?app_id=1089")
    data = '{"states_list": "US"}'
    ws.send(data)

    # Receiving response from websockets
    while True:
        result = ws.recv()
        print("Received '%s'" % result)
        print(type(result))
        if result:
            break
    # Closing the websockets
    ws.close()
    dict1 = json.loads(result)
    df = pd.json_normalize(dict1, "states_list")
    # print(df)
    path = r"C:\Users\jenilobo\PycharmProjects\DerivAssessment\TestCases\WebsocketAPIAutomation\ExpectedResult.xlsx"
    excel_data_df = pd.read_excel(path, sheet_name='America')

    # Comparing 2 data frames to get any values if not matching
    df_diff = pd.concat([df, excel_data_df]).drop_duplicates(keep=False)
    print(df_diff)
    assert df_diff.empty
