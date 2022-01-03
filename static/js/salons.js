$(document).ready(function () {
    $.ajax({
        url: '/api/v1/salons',
        method: 'GET',
        success: function (response) {
            for (let salon of response) {
                let el = " <li class='list-group-item'>" + salon.name + "</li>";
                $('#salons').append(el);
            }
        }
    })
});


