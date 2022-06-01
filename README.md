# Passing-list-strings-between-java-and-python 
## Libraries Used
#### 1. flask:    A python framework used to make api
#### 2. requests: To use an api 
#### 3.jsonify:   To convert output into json file
#### 4.picke:     To make  list ,strings into pkl file that can be used in any python program 
            

_________________________________________________________________________________________________________

## User defined Functions:
### string :  It take input of user name
### home   :  It makes dictionary and return json file of this
_________________________________________________________________________________________________________

## Target: We have to pass list ,string through python api to a java program. 
_________________________________________________________________________________________________________
## Working of code
#### Stringpass.py
In this first we take input from user in variable 'data'  And then we will pass into pkl file using dump method.We can pass lists,strings using pickle.We are using binary
write mode.
      
      with open("stringpass.pkl","wb") as sp:
       pickle.dump(data,sp)
#### Stringpass2.py
First we will load our pickle file .We use read binary to read file.Now we have loaded our pickle file in data which contains strings entered by user.

    with open("stringpass.pkl","rb") as sp:
    data=pickle.load(sp)

Then we start making api using flask framework. 

      app=Flask(__name__)
      @app.route("/")
Next in home function we are making dictionary 'fruitdict' using two lists 'fruits' and 'count' using zip method.It will make dict in which 'count' is key .

            fruitdict=dict(zip(count,fruits))
Now we can return fruitdict dictionary or data which we loaded from pkl file.

     return jsonify(fruitdict)
     return jsonify(data)
And in last we will run our app using below code.We set debug to true so it will show any error in browser.

    if __name__=="__main__":
    app.run(debug=True)
    
#### APIMain.java
In this we will import first httpclient,httpserver,httprequest .
First we will create var url,response,request,client 
Note:The below method can be used in java 9 or above
We will paste our url in var url

            var url="----------------"
Request generated using:

    var request=HttpRequest.newBuilder().GET().uri(URI.create(url)).build();
Then client generated using

        var client=HttpClient.newBuilder().build();
Response generated ,type expected here is string

        var response=client.send(request, HttpResponse.BodyHandlers.ofString());
We wil print response  using 

            System.out.println(response.body());
