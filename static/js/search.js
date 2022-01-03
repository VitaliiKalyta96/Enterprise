$(document).ready(function () {
    $('#searchInput').on('keyup', function (event) {
        $("#searchResults").on('keyup', function (event) {
            let text = $(this).val()
            console.log(text)
            $.ajax(
                {
                    url: ("/api/v1/search?q=" + text),
                    method: "GET",
                    success: function (response) {
                        console.log(response)
                        for (let element of response) {
                            if (element.name) {
                                let element_name = $(this).val("<li>" + element.name + "</li>");
                                $('#searchResults').append(element_name)
                                console.log(element_name)
                            }
                            if (element.location) {
                                let element_location = $(this).val("<li>" + element.location + "</li>");
                                $('#searchResults').append(element_location);
                                console.log(element_location)
                            }
                            if (element.email) {
                                let element_email = $(this).val("<li>" + element.email + "</li>");
                                $('#searchResults').append(element_email);
                                console.log(element_email)
                            }
                            if (element.address) {
                                let element_address = $(this).val("<li>" + element.address + "</li>");
                                $('#searchResults').append(element_address);
                                console.log(element_address)
                            }
                        }
                    }
                }
            )
        })
    })
});
