from fastapi import APIRouter, Query,HTTPException
from pydantic import BaseModel,field_validator
from datetime import datetime
from app.influx import write_api, query_api
from app import config
from influxdb_client import Point

router = APIRouter()

class SensorData(BaseModel):
    device_id: str
    temperature: float
    humidity: float
    pressure: float
    timestamp: datetime

    @field_validator("temperature")
    def validate_temperature(cls, v):
        if not -40 <= v <= 100:
            raise ValueError("Temperature must be between -40 and 100°C")
        return v

    @field_validator("humidity")
    def validate_humidity(cls, v):
        if not 0 <= v <= 100:
            raise ValueError("Humidity must be between 0 and 100%")
        return v

    @field_validator("pressure")
    def validate_pressure(cls, v):
        if not 800 <= v <= 1200:
            raise ValueError("Pressure must be between 800 and 1200 hPa")
        return v

@router.post("/ingest")
def ingest(data: SensorData):
    try:
        point = (
            Point("iot_data")
            .tag("device_id", data.device_id)
            .field("temperature", data.temperature)
            .field("humidity", data.humidity)
            .field("pressure", data.pressure)
            .time(data.timestamp)
        )
        write_api.write(bucket=config.INFLUXDB_BUCKET, record=point)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to write to InfluxDB: {str(e)}")

@router.get("/metrics")
def get_metrics(
    device_id: str,
    start: str = Query(..., example="-1h"),
    stop: str = Query(..., example="now()")
):
    query = f'''
    from(bucket: "{config.INFLUXDB_BUCKET}")
        |> range(start: {start}, stop: {stop})
        |> filter(fn: (r) => r["_measurement"] == "iot_data" and r["device_id"] == "{device_id}")
        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
    '''
    result = query_api.query(org=config.INFLUXDB_ORG, query=query)
    readings = []
    for table in result:
        for record in table.records:
            readings.append({
                "time": record["_time"],
                "temperature": record["temperature"],
                "humidity": record["humidity"],
                "pressure": record["pressure"]
            })
    return {"data": readings}
