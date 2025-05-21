from influxdb_client import InfluxDBClient, Point, WritePrecision
from app import config
from influxdb_client.client.write_api import ASYNCHRONOUS

client = InfluxDBClient(
    url=config.INFLUXDB_URL,
    token=config.INFLUXDB_TOKEN,
    org=config.INFLUXDB_ORG
)

write_api = client.write_api(write_options=ASYNCHRONOUS)
query_api = client.query_api()
