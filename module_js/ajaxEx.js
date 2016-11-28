// =============================================================================
// write        : moto
// update       : 2016.11.28.
// ajax example : post & get
// dependency   : jQuery
// =============================================================================

var INPUTDATA = {
    AA: "aa",
    BB: "bb"
};

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


// patch =======================================================================

var target_id = 1;

$.ajax({
    type: "patch",
    data: INPUTDATA,
    beforeSend: function(request) {
        //django
        request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
    },
    url: "/restapi/endpoint/" + target_id + "/",
    error: function(response) {
        console.log("error:" + response);
    },
    success: function(response) {
        console.log(response);
    },
    complete: function() {}
});

// patch =======================================================================


// delete ======================================================================

var target_id = 1;

$.ajax({
    type: "DELETE",
    beforeSend: function(request) {
        //for django
        request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
    },
    url: "/restapi/endpoint/" + target_id + "/",
    error: function(response) {
        console.log("error:" + response);
    },
    success: function(response) {
        console.log(response);
    },
    complete: function() {}
});

// delete ======================================================================
