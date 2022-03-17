var tab1 = document.getElementById('tab1');
var tab2 = document.getElementById('tab2');
var prevBtn = document.getElementById('prevBtn');
var nextBtn = document.getElementById('nextBtn');
var submitBtn = document.getElementById('submitBtn');
var form = document.getElementById('form');
var project_number = document.getElementById('projectNumber');
var valid = true;
var valid_tab2 = true;


nextBtn.addEventListener("click",function(){
    var x = document.getElementsByClassName('tab1');
    for (var i = 0; i < x.length; i++) {
        if (x[i].value.length != 0) {
            console.log('passed');
            valid = true;
        }else{
            console.log('failed');
            valid = false;
            break;
        }
    }
    if(valid && $('#project_number_error').css('display') == 'none'){
        $('#prevBtn').css('display','block');
        $('#nextBtn').css('display','none');
        $('#submitBtn').css('display','block');
        $('#tab2').css('display','block');
        $('#tab1').css('display','none');
        $('#req_inputs').css('display','none');
    }else{
        $('#req_inputs').css('display','block');
    }
});
  

prevBtn.addEventListener("click",function(){
    $('#prevBtn').css('display','none');
    $('#submitBtn').css('display','none');
    $('#nextBtn').css('display','block');
    $('#tab1').css('display','block');
    $('#tab2').css('display','none');
});

submitBtn.addEventListener("click",function(e){
    e.preventDefault();
    var y = document.getElementsByClassName('tab2');
    for (var i = 0; i < y.length; i++) {
        if (y[i].value.length != 0) {
            console.log('passed');
            valid_tab2 = true;
        }else{
            console.log('failed');
            valid_tab2 = false;
            break;
        }
    }
    if(valid_tab2){
        $('#req_inputs').css('display','none');
        form.submit();
    }else{
        $('#req_inputs').css('display','block');
    } 
});

project_number.addEventListener('change',function(){
    var project_number = this.value;
    $.ajax({
        url: '/project/'+project_number,
        type: 'GET',
        success: function(data){
            if(data == 'done!'){
                $('#project_number_error').css('display','none');
            }else{
                $('#project_number_error').css('display','block');
            }
        },
        error: function(error){
            console.log(error);
        },
    });
});




