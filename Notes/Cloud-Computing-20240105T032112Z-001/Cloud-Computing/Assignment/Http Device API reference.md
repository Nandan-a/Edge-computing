Http Device API reference

https://thingsboard.io/docs/reference/http-api/


    400 Bad Request - Invalid URL, request parameters or body.
    401 Unauthorized - Invalid $ACCESS_TOKEN.
    404 Not Found - Resource not found.


Telemetry upload API

http(s)://host:port/api/v1/$ACCESS_TOKEN/telemetry

{"key1":"value1", "key2":"value2"}

curl -v -X POST --data "{"temperature":42,"humidity":73}" http://$THINGSBOARD_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"

curl -v -X POST -d @telemetry-data-with-ts.json https://demo.thingsboard.io/api/v1/ABC123/telemetry --header "Content-Type:application/json"

https://requests.readthedocs.io/en/latest/

