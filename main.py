from flask import Flask, request, render_template, redirect, url_for,jsonify
from requests import get
from list_bucket import list_bucket_name
from create_bucket import create_buckets,number_of_buckets,create_region_buckets

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])

def index(): 
     return render_template('index.html')

@app.route('/list_buckets',methods=['GET', 'POST'])

def list_buckets(): 
     aws_region = request.form.get('region')
     response=list_bucket_name(aws_region)
     result={
         'get_bucket':response
     }
   
     return result



@app.route('/create_bucket',methods=['GET', 'POST'])

def create_bucket(): 
     bucket = request.form.get('bucket_name')
     print(bucket)
     response=create_buckets(bucket)
     return response

@app.route('/create_number_of_bucket',methods=['GET', 'POST'])
    
def number_of_bucket():
    bucket = request.form.get('bucket_name')
    num=int(request.form.get('number-of-buckets'))
    response=number_of_buckets(bucket,num)
    return response

@app.route('/choose_region',methods=['GET', 'POST'])
    
def create_choose_region():
    bucket = request.form.get('bucket_name_region')
    region_arr = request.form.get('aws_region')
    print(region_arr)
    # response=create_region_buckets(bucket,region_arr)
    return "true"
      
@app.route('/file_upload',methods=['GET', 'POST'])

def file_upload():
    # buc_name = request.form.get('buck_name')
    # buc_num = request.form.get('buck_num')
    # file = request.form.get('data_upload')
    file = request.files['file_key']
    print(file)
    # print(buc_name+buc_num+file)
    return"true"

























if __name__ == '__main__':
  app.run(debug=False,host="localhost",port=8102)