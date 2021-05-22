
$(document).ready(function() {
    $( "#entry_form_div" ).hide()
    $('.error_msg').hide();

    function validateClientname() {
        let clientname = $('#name').val();
        if (clientname.length == '') {
            $('#client_error').show();
            return false;
        } 
        else {
            $('#client_error').html('');
            return true;
        }
    }

    function validateEmail() {
        let email = $('#email').val();
        let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;

        if (email.length == '') {
            $('#email_error').show();
            return false;
        }
        else if( regex.test(email) )
        {
            $('#email_error').html('');
            return true
        }
        else {
            $('#email_error').show();
            $('#email_error').html("**Invalid Email");
            return false
        }
    }

    function validateInvoice() {
        let inv = $('#inv_no').val();
        let regex = /^[A-Za-z0-9]+$/;

        if (inv.length == '') {
            $('#invoice_error').show();
            return false;
        }
        else if( regex.test(inv) )
        {
            $('#invoice_error').html('');
            return true
        }
        else {
            $('#invoice_error').show();
            $('#invoice_error').html("**Invalid Invoice Number - should be alphanumeric");
            return false
        }
    }

    function validateProject() {
        let project = $('#project').val();
        if (project.length == '') {
            $('#project_error').show();
            return false;
        }
        else
        {
            $('#project_error').html('');
            return true
        }

    }

    function validateAmount() {
        let amount = $('#amount').val();
        let regex = /^[0-9.]+$/;

        if (amount.length == '') {
            $('#amount_error').show();
            return false;
        }
        else if( regex.test(amount) )
        {
            $('#amount_error').html('');
            return true
        }
        else {
            $('#amount_error').show();
            $('#amount_error').html("**Invalid Amount Value");
            return false
        }
    }

    $( "#but_submit" ).click(function(e) {
        e.preventDefault();
        var username = $("#txt_uname").val().trim();
        var password = $("#txt_pwd").val().trim();
        var csrftoken = $('[name="csrfmiddlewaretoken"]').val()
        
        if( username != "" && password != "" ){
            $.ajax({
                url:'http://localhost:8000/login/',
                type:'post',
                data:{username:username,password:password},
                headers: {'X-CSRFToken': csrftoken},
                success:function(response){
                    if(response['status'] == true){
                        window.location.href = 'http://localhost:8000/client-invoice/';
                    }
                    else{
                        console.log(response['message'])
                        $("#message").html(response['message']);
                    }
                },
                error: function(XMLHttpRequest, textStatus, errorThrown) { 
                   $("#message").html("Invalid Username/Password");
                }    
            });
        }
    });    



    $( "#add_btn" ).click(function(e) {
        e.preventDefault();
        $( "#list_table" ).hide()
        $( "#entry_form_div" ).show()
        
    });

    $( "#cancel_btn" ).click(function(e) {
        e.preventDefault();
        $(".form_field").val('');
        $(".error_msg").html('');
        $( "#list_table" ).show()
        $( "#entry_form_div" ).hide()
        
    });


    $( "#submit_btn" ).click(function(e) {
        validateClientname();
        validateEmail();
        validateInvoice();
        validateProject();
        validateAmount();
        e.preventDefault();
        
        if( validateClientname() && validateEmail() && validateInvoice() && validateProject() && validateAmount() )
        {
            let clientname = $('#name').val();
            let email = $('#email').val();
            let inv = $('#inv_no').val();
            let project = $('#project').val();
            let amount = $('#amount').val();
            var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
            $.ajax({
                url:'http://localhost:8000/client-invoice/',
                type:'post',
                data:{client_name: clientname, client_email: email, invoice_number: inv, project_name: project, amount_charged: amount},
                headers: {'X-CSRFToken': csrftoken},
                success:function(response){
                    console.log('hereeeeeeeee')
                    if(response['status'] == true){
                        location.reload();  
                    }
                    else{
                        console.log(response['message'])
                        $("#err_message").html(response['message']);
                    }
                },
                error: function(XMLHttpRequest, textStatus, errorThrown) { 
                   $("#err_message").html("Could not create invoice entry. Please try again");
                }    
            });
        }
    });


    $( "#logout" ).click(function(e) {
        var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
        $.ajax({
                url:'http://localhost:8000/logout',
                type:'get',
                headers: {'X-CSRFToken': csrftoken},
                success:function(response){
                    console.log(response)
                    if(response['status'] == true){
                        window.location.href = 'http://localhost:8000/signin/';
                    }
                   
                },
            });

    });







});