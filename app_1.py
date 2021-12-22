from flask import Flask,jsonify,request
from flask_restful import Api,Resource

#request is used to fetch json file from the provided url that contains parameters
#Resource is class that helps create multiple methods like get,post etc for a specific url with end points

#we will ask the server to perform operations therefore we will need post method

app=Flask(__name__)
api=Api(app) #api will work on some created application and add resources to it
#resource is package of functions with some endpoint defined


class Add(Resource):
    def post(self):

        input_params=request.get_json()
        x=int(input_params['x'])
        y=int(input_params['y'])
        res=x+y

        response_json={
        'ans':res,
        'status_code':200
        }
        return jsonify(response_json)

    def get(self):
        return 'I am working'

class Subtract(Resource):
    pass
class Divide(Resource):
    pass
class Multiply(Resource):
    pass


#Add resources(package of get,post ... functions so now we dont need to define method separately) to api

api.add_resource(Add,'/add')#Parameters for this method--> resource clas and endpoint

if '__name__' == '__main__':
    app.run(debug=True)
