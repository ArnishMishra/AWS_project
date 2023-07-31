//  us-east-1
// us-east-2
// us-west-1
// us-west-2
// ca-central-1

function display_buckets(){

let region_name=document.getElementById("region").value
console.log(region_name)
aws_region=""

switch(region_name) {
    case "US-East(N. Virginia)":
        aws_region="us-east-1"
        break;
    
    case "US-East(Ohio)":
        aws_region="us-east-2"
         break;
    
    case "US-West(N. California)":
        aws_region="us-west-1"
        break;

    case "US-West(Oregon)":
        aws_region="us-west-2"
         break;
      
    case "Canada(Central)":
        aws_region="ca-central-1"
        break;
      
    default:
      break
  }

  $.ajax({
    url: '/list_buckets',
    type: 'POST',
    data: {
        
        'region': aws_region,
        
    },

    success: function (response) {

        let n=response['get_bucket'].length
        for(let i=0;i<n;i++){
            console.log(response['get_bucket'][i])
            table=document.getElementById("table_body").innerHTML
            document.getElementById("table_body").innerHTML=table+`
        
            <tr>
            <td>${response['get_bucket'][i]}</td>
            <td>${aws_region}</td>
        </tr>
            `
        }
       
        
        
    },

});

}





function create_bucket(){
let b_name=""
 b_name=document.getElementById("b_name").value
console.log(b_name)
    
$.ajax({
    url: '/create_bucket',
    type: 'POST',
    data: {
        
        'bucket_name':b_name,
    },

    success: function (response) {

        if(response['ResponseMetadata']['HTTPStatusCode']==200){
            console.log("successfully created bucket")
        }
        else{
            console.log(response['Error']['Message'])
        }
        
        
    }

});


}



function number_of_buckets(){
    let b_name=""
    let num
     b_name=document.getElementById("b_name").value
     num=document.getElementById("number_of_buckets").value
    console.log(b_name)
        
    $.ajax({
        url: '/create_number_of_bucket',
        type: 'POST',
        data: {
            
            'bucket_name':b_name,
            'number-of-buckets':num,

        },
    
        success: function (response) {
    
            if(response['ResponseMetadata']['HTTPStatusCode']==200){
                console.log("successfully created bucket")
            }
            else{
                console.log(response['Error']['Message'])
            }
            
            
        }
    
    });
    
    
    }



    

function create_choose_region(){

    let b_name_region=document.getElementById("b_name_region").value
     let region1=document.getElementById("region1").value
     let region2=document.getElementById("region2").value
     let aws_region
    let regions=[region1,region2]
    let aws_regions={}


     for(let i=0;i<regions.length;i++){
        switch(regions[i]) {
            case "US-East(N. Virginia)":
                aws_region="us-east-1"
                break;
            
            case "US-East(Ohio)":
                aws_region="us-east-2"
                 break;
            
            case "US-West(N. California)":
                aws_region="us-west-1"
                break;
        
            case "US-West(Oregon)":
                aws_region="us-west-2"
                 break;
              
            case "Canada(Central)":
                aws_region="ca-central-1"
                break;
              
            default:
              break
          }
    
          aws_regions[`${i}`]=aws_region
          
     }

     console.log(aws_regions)
    
     
     $.ajax({
        url: '/choose_region',
        type: 'POST',
        data: {
            
            'bucket_name_region':b_name_region,
            'aws_region':JSON.stringify(aws_regions)
            

        },
    
        success: function (response) {
    
            if(response['ResponseMetadata']['HTTPStatusCode']==200){
                console.log("successfully created bucket")
            }
            else{
                console.log(response['Error']['Message'])
            }
            
            
        }
    
    });



}


function upload_files(){
    const InputFile=document.getElementById("file_upload")
    const bucketname=document.getElementById("buc_name").value
    const buc_num=document.getElementById("num_of_buc").value
    InputFile.click();

    InputFile.onchange=({target})=>{
        let file =target.files[0]
        const formdata=new FormData();
        formdata.append('file_key',file)
        //console.log(formdata)
        console.log(file)
        // console.log(bucketname)

        $.ajax({
            url: '/file_upload',
            type: 'POST',
            data: {
                formdata,
    
    
            },
            processData: false,
            contentType: false,
        
            success: function (response) {
        
                if(response['ResponseMetadata']['HTTPStatusCode']==200){
                    console.log("successfully created bucket")
                }
                else{
                    console.log(response['Error']['Message'])
                }
                
                
            }


            })


    
    
    
    
    }




}