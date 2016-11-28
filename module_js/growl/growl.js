// =============================================================================
// write      : moto
// update     : 2016.10.30.
// dependency : jquery / bootstrap3 / jquery.bootstrap-growl.min.js
// =============================================================================




var OBJSAMPLE = function() {

    var successMessage = function(message, in_delay) {
        $.bootstrapGrowl(message, {
            type: 'success',
            offset: {
                from: 'top',
                amount: 150
            },
            align: 'center',
            width: 'auto',
            delay: in_delay,
            allow_dismiss: false
        });
    };

    var errorMessage = function(message, in_delay) {
        $.bootstrapGrowl(message, {
            type: 'danger',
            offset: {
                from: 'top',
                amount: 150
            },
            align: 'center',
            width: 'auto',
            delay: in_delay,
            allow_dismiss: false
        });
    };


    //public start =============================================================
    var OBJSAMPLE_PUBLIC = {

        public_sample_process: function(e) {

            var tData = {
                name: $('#name').val(),
            };

            if (tData.name === "") {
                errorMessage("이름을 입력해주세요.", 1000);
            }
            else {
                $.ajax({
                    type: "post",
                    data: tData,
                    beforeSend: function(request) {
                        request.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                    },
                    url: "/test/",
                    error: function(response) {
                        errorMessage("동일한 이름을 찾을 수 없습니다.", 1000);
                    },
                    success: function(response) {
                        successMessage("이름을 찾았습니다.", 1000);
                    },
                    complete: function() {
                    }
                });
            }
        },

        public_sample_process2: function(e) {
        }

    }; //public end =============================================================

    return OBJSAMPLE_PUBLIC;
};
