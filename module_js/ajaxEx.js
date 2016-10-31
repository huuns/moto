// =============================================================================
// write        : moto
// update       : 2016.10.31.
// ajax example : post & get
// dependency   : jQuery
// =============================================================================




// post ========================================================================

$.ajax({
    type: "post",
    data: {
        "A": $('.EXAMPLE').val()
    },
    beforeSend: function(request) {
        //for django
        request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
    },
    url: "/restapi/endpoint/",
    error: function(response) {
        console.log("error:" + response);
    },
    success: function(response) {
        console.log(response);
    },
    complete: function() {}
});

// post ========================================================================



// get =========================================================================

var INPUTDATA = {
    AA: "aa",
    BB: "bb",
    CC: "cc"
}

$.ajax({
    type: "get",
    data: INPUTDATA,
    url: "/restapi/endpoint/",
    error: function(response) {
        console.log("error:" + response);
    },
    success: function(response) {
        console.log(response);
    },
    complete: function() {}
});

// get =========================================================================
