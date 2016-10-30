// =============================================================================
// write      : moto
// update     : 2016.10.30.
// dependency : jquery / bootstrap3 / etc
// =============================================================================




var OBJSAMPLE = function() {


    // private variables -------------------------------------------------------
    var info;
    var status = true;
    var color = 0x384439;

    var description_array = [
            'A1',
            'A2',
            'A3',
            'A4'
        ]
    // private variables -------------------------------------------------------




    // private functions -------------------------------------------------------
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

    var check_status = function(){
        // using private variable **********************************************
        if(status === true){
        // using private variable **********************************************
            console.log("status true");
        }
    };
    // private functions -------------------------------------------------------




    // public functions --------------------------------------------------------
    var OBJSAMPLE_PUBLIC = {

        public_sample_process: function(e) {

            // call private function *******************************************
            successMessage("이름을 찾았습니다.", 1000);
            errorMessage("동일한 이름을 찾을 수 없습니다.", 1000);
            // call private function *******************************************

        },

        public_sample_process2: function(e) {
            // call private function *******************************************
            check_status();
            // call private function *******************************************
        },

        get_color: function(e){
            // using private variable ******************************************
            return color
            // using private variable ******************************************
        }

    };
    // public functions --------------------------------------------------------


    return OBJSAMPLE_PUBLIC;
};
