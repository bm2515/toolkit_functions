import requests
import json

def pretty_print_request(request):
    print( '\n{}\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()))
    )

def pretty_print_response(response):
    print('\n{}\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()))
    )

    response_object = json.loads(response.text)

    if (type(response_object) == list):
        for each in response_object:
            for key, value in each.items():
                print(key, ':' , value)
            print('\n')

    elif (type(response_object) == dict):
        for key, value in response_object.items():
            print(key, ':' , value)
        print('\n')
        
    return response_object
    
           
def make_post_get_requests(method, url, token, payload=None):
    #url = 'https://api.github.com/users/bm2515'
    
    # Additional headers.
    auth = "Bearer " + token
    headers = {'Content-Type': 'application/json',
              "Authorization": auth}
    # Body
    if method == "POST":

        # convert dict to json by json.dumps() for body data. 
        resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))

    elif method == "GET":

        resp = requests.get(url, headers=headers)

    
    # Validate response headers and body contents, e.g. status code.
    #assert resp.status_code == 200
    #resp_body = resp.json()
    
    
    # print full request and response
    pretty_print_request(resp.request)
    response_object = pretty_print_response(resp)
    return response_object

if __name__ == '__main__':

    #Example demonstration
    token = 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NTQwNDkyMiwiZXhwIjoxNTk2MDA5NzIyfQ.eyJpZCI6MSwidXNlcl90eXBlIjoiQXBpVXNlciJ9.Mrk_Tvag28C-I9mfPWjvLJGYHnfcfwat_MSDC69S1YvbkCdZdUsuQ2ynKqN4l3FaZuO9CGKqWy589yF65I4YpA'
    url = 'http://localhost:5000/siha-api/v1/data/distance/patientid/1/start/2020-04-01/end/2020-04-30'
    response = make_post_get_requests("GET", url, token, payload=None)


    
