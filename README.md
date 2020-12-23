# Test API
This is a stand-in for a real API that yields data.  The API accepts GET requests with the arguments `id` and `interval` to /api/.  You can try it out [here](https://solar-flaare.herokuapp.com/api/?id=myproject&interval=5) or with curl `curl 'https://solar-flaare.herokuapp.com/api/?id=with-curl&interval=5'`

`id` is the project id.  The API accepts any and all project id's and will generate a project for that id with a random number of sensors between 0 and 10.  
`interval` is the update interval, i.e. how often the timestamp of the sensors will change.  If you query the API multiple times within an interval it will return the same information both times.

The API and returns a json object of the form:
{
  "xxxx": {
    "field1":  single number corresponding to timestamp
    "field2": single number corresponding to time stamp
    "timestamp": "isoformatted time stamp in UTC"
...
    }
}
Note: xxxx is the id given in the request.

The only guaranteed field in the response will be "timestamp" which will always be iso-formatted and in UTC (with the "Z") convention.

The number of fields is unknown, will return a random amount between 0 and 10 (inclusive)
