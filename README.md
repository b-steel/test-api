#Test_API

The endpoint takes an "id" as a param (as in http://some.address.com/somestuff?id=xxxx) and returns a json object of the form:
{
  "xxxx": {
    "field1":  single number corresponding to timestamp
    "field2": single number corresponding to time stamp
    "timestamp": "isoformatted time stamp in UTC"
...
    }
}
note xxxx in the json is the id given in the request

The only guaranteed field in the response will be "timestamp" which will always be iso-formatted and in UTC (with the "Z") convention.   Timestamp will update in 5 minute increments

The number of fields is unknown, will return a random amount (including 0)