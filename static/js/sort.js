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
                '<td class="col-name">' + data[i].project_name + '</td>' +
                '<td class="col-number">' + data[i].project_number + '</td>' +
                '<td class="col-client">' + data[i].client + '</td>' +
                '<td class="col-pro-manager">' + data[i].project_manager + '</td>' +
                '<td class="col-last-review">' + data[i].last_review + '</td>' +
                '<td class="col-scope">' + data[i].scope_of_work + '</td>' +
                '<td class="col-col-cat">' + data[i].category + '</td>' +
                '<td class="col-risk">' + data[i].desc + '</td>' +
                '<td class="col-prob">' + data[i].probability + '</td>' +
                '<td class="col-impact">' + data[i].impact + '</td>' +
                '<td class="col-score">' + (data[i].probability * data[i].impact) + '</td>' +
                '<td class="col-control">' + data[i].control_measures + '</td>' +
                '<td class="col-owner">' + data[i].owner + '</td>' +
                '<td class="col-status">' + data[i].status + '</td>' +
                '<td class="col-nearest">' + data[i].nearest_month + '</td>' +
                '<td class="col-cl-costs">£' + data[i].cl_costs + '</td>' +
                '<td class="col-pl-costs">£' + data[i].planned_costs + '</td>' +
                '<td class="col-cont-costs">£' + data[i].cont_costs + '</td>' +
                '<td class="col-bud-costs">£' + data[i].costs_in_budget + '</td>' +
                '</tr>');
            }
        },
        error: function(error){
            console.log(error);
        },
    });
    const colCheckboxes = document.querySelectorAll('.col-checkbox');
    $('th').css('display','table-cell');

    colCheckboxes.forEach(element => {
        // Set checked by Default
        element.checked = true;
        const colName = element.getAttribute('data-col');

        hideShowTableCol(colName, checked);
    });
    function hideShowTableCol(colName, checked) {
        const cells = document.querySelectorAll(`.${colName}`);
        cells.forEach( cell => {
            cell.style.display = (checked) ? 'table-cell' : 'none';
        });
    }
});


const colCheckboxes = document.querySelectorAll('.col-checkbox');

colCheckboxes.forEach(element => {
    // Set checked by Default
    element.checked = true;
    element.addEventListener('change', (event) => {
        const checked = event.target.checked;
        const colName = element.getAttribute('data-col');

        hideShowTableCol(colName, checked)
    });
});

function hideShowTableCol(colName, checked) {
    const cells = document.querySelectorAll(`.${colName}`);
    cells.forEach( cell => {
        cell.style.display = (checked) ? 'table-cell' : 'none';
    });
}