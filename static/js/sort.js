var sort_by = document.getElementById('sort_projects_by');
var table = document.getElementById('projects');

sort_by.addEventListener('change',function(){
    var sort_by = this.value;
    $.ajax({
        url: '/sort/'+sort_by,
        type: 'GET',
        success: function(data){
            $('#projects').empty();
            for(var i = 0; i < data.length; i++){
                $('#projects').append('<tr>' + 
                '<td>' + data[i].project_name + '</td>' +
                '<td>' + data[i].project_number + '</td>' +
                '<td>' + data[i].client + '</td>' +
                '<td>' + data[i].project_manager + '</td>' +
                '<td>' + data[i].last_review + '</td>' +
                '<td>' + data[i].scope_of_work + '</td>' +
                '<td> <a href="/get_risk/' + data[i].project_name +'"'+ 'class="btn btn-success btn-sm">Check Now</a></td>'+
                '</tr>');
            }
        },
        error: function(error){
            console.log(error);
        },
    });
});