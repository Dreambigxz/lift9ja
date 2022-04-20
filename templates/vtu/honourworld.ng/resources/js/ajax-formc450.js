$(function() {

    AjaxHonour.Profile();
    AjaxHonour.AjaxForms();
    AjaxHonour.UpgradeForm();

});


var AjaxHonour = {};



AjaxHonour.Profile = function () {
    $(".js-resend-verification-email").on("click", function () {
        var $this = $(this);
        var $alert = $this.parents(".alert");

        if ($alert.hasClass("onprogress")) {
            return;
        }

        $alert.addClass('onprogress');
        $.ajax({
            url: $this.data("url"),
            type: 'POST',
            dataType: 'jsonp',
            data: {
                action: 'resend-email'
            },

            error: function () {
                $this.remove();
                $alert.find(".js-resend-result").html(__("Oops! An error occurred. Please try again later!"));
                $alert.removeClass("onprogress");
            },

            success: function (resp) {
                $this.remove();
                $alert.find(".js-resend-result").html(resp.msg);
                $alert.removeClass("onprogress");
            }
        });
    });
}



/**
 * Add msg to the $resobj and displays it
 * and scrolls to $resobj
 * @param {$ DOM} $form jQuery ref to form
 * @param {string} type
 * @param {string} msg
 */
var __form_result_timer = null;
AjaxHonour.DisplayFormResult = function($form, type, msg)
{
    var $resobj = $form.find(".form-result");
    msg = msg || "";
    type = type || "error";

    if ($resobj.length != 1) {
        return false;
    }


    var $reshtml = "";
    switch (type) {
        case "error":
            $reshtml = "<div class='alert alert-danger' role='alert'> "+msg+"</div>";
            break;

        case "success":
            $reshtml = "<div class='alert alert-success' role='alert'> "+msg+"</div>";
            break;

        case "info":
            $reshtml = "<div class='alert alert-info' role='alert'> "+msg+"</div>";
            break;
    }

    $resobj.html($reshtml).stop(true).fadeIn();

    clearTimeout(__form_result_timer);
    __form_result_timer = setTimeout(function() {
        $resobj.stop(true).fadeOut();
    }, 10000);

    var $parent = $("html, body");
    var top =$resobj.offset().top - 85;
    if ($form.parents(".skeleton-content").length == 1) {
        $parent = $form.parents(".skeleton-content");
        top = $resobj.offset().top - $form.offset().top - 20;
    }

    $parent.animate({
        scrollTop: top + "px"
    });
}


/**
 * Ajax forms
 */
AjaxHonour.AjaxForms = function()
{
    var $form;
    var $result;
    var result_timer = 0;

    var pleaseWait = $("#pleaseWaitDialog");


    showPleaseWait = function () {
        pleaseWait.modal("show");
    };

    hidePleaseWait = function () {
        pleaseWait.modal("hide");
        pleaseWait.removeClass("in");
        $(".modal-backdrop").remove();
        pleaseWait.hide();
    };


    $("body").on("submit", ".js-ajax-form", function(){

        $form = $(this);
        $result = $form.find(".form-result")
        submitable = true;

        $form.find(":input.js-required").not(":disabled").each(function(){
            if (!$(this).val()) {
                $(this).addClass("error");
                submitable = false;
            }
        });


        if ($(".js-query-datadest").length == 1) {
            var target = $(".js-query-datadest");
        }

        if ($('#contact_opt').length == 1) {


            if ($('#contact_opt').value == 1) {
                $('#contact_list_div').show();
                $('#phone_num_div').hide();
                $("#phone_num").attr('disabled', 'disabled');
                $("#custom-select-contact").removeAttr('disabled');

            }

            if ($('#contact_opt').value == 2) {
                $("#phone_num").removeAttr('disabled');
                $('#phone_num_div').show();
                $('#contact_list_div').hide();
                $("#custom-select-contact").attr('disabled', 'disabled');
            }
        }

        if (submitable) {
            showPleaseWait();
            $.ajax({
                url: $form.attr("action"),
                type: $form.attr("method"),
                dataType: "jsonp",
                data: $form.serialize(),
                error: function() {
                    hidePleaseWait();
                    AjaxHonour.DisplayFormResult($form, "error", ("Oops! An error occured. Please try again later!"));
                    Swal.fire({
                        title: "Error!",
                        text: "Oops! An error occured. Please try again later!",
                        type: "error",
                        confirmButtonText: "Ok"
                    }).then((result) => {

                    });
                },

                success: function(resp) {

                    hidePleaseWait();
                    if (typeof resp.redirect === "string") {
                        window.location.href = resp.redirect;
                    } else if (typeof resp.msg === "string") {
                        var result = resp.result || 0;
                        var reset = resp.reset || 0;
                        switch (result) {
                            case 1:

                                if ($(".js-query-datadest").length == 1) {
                                    if(resp.datamaillistcount > 0){
                                        target.html('').select2({data: JSON.parse(resp.datamaillist)});
                                        if(resp.selectedlist != null){
                                            target.val(resp.selectedlist).trigger('change');
                                        }else{
                                            target.html('').select2({data: [{id: '', text: ''}]});
                                        }

                                        var newOption = new Option("", "Select a list", false, false);
                                        target.append(newOption).trigger('change');
                                    }
                                }
                                AjaxHonour.DisplayFormResult($form, "success", resp.msg);
                                if (reset) {
                                    $form[0].reset();
                                }
                                // alert(resp.msg);
                                Swal.fire({
                                    title: "Successful!",
                                    text: resp.msg,
                                    type: "success",
                                    confirmButtonText: "Ok"
                                }).then((result) => {
                                    if (result.value) {
                                        setTimeout(function () {
                                            //  window.location.reload();
                                        }, resp.delaytime);
                                        if (typeof resp.url === "string") {
                                            window.location.href = resp.url;
                                        }

                                        if (typeof resp.reload === "string") {
                                              window.location.reload();
                                        }
                                    } else {
                                    }
                                });
                                break;

                            case 2: //
                                AjaxHonour.DisplayFormResult($form, "info", resp.msg);

                                Swal.fire({
                                    title: "Successful! Info:",
                                    text: resp.msg,
                                    type: "success",
                                    confirmButtonText: "Ok"
                                }).then((result) => {
                                    if (result.value) {
                                        setTimeout(function () {
                                            //  window.location.reload();
                                        }, resp.delaytime);
                                        if (typeof resp.url === "string") {
                                            window.location.href = resp.url;
                                        }
                                    } else {
                                    }
                                });
                                break;
                            default:
                                AjaxHonour.DisplayFormResult($form, "error", resp.msg);

                                Swal.fire({
                                    title: "Error!",
                                    text: resp.msg,
                                    type: "error",
                                    confirmButtonText: "Ok"
                                }).then((result) => {
                                    if (result.value) {
                                        setTimeout(function () {
                                            //  window.location.reload();
                                        }, resp.delaytime);
                                        if (typeof resp.url === "string") {
                                            window.location.href = resp.url;
                                        }
                                    } else {
                                    }
                                });
                                break;
                        }

                    } else {
                        AjaxHonour.DisplayFormResult($form, "error", ("Oops! An error occured. Please try again later!"));
                    }

                }
            });
        } else {

            AjaxHonour.DisplayFormResult($form, "error", ("Fill required fields"));
        }

        return false;
    });
}




/**
 * Ajax forms
 */
AjaxHonour.UpgradeForm = function()
{
    var $form;
    var $result;
    var result_timer = 0;

    var pleaseWait = $("#pleaseWaitDialog");


    showPleaseWait = function () {
        pleaseWait.modal("show");
    };

    hidePleaseWait = function () {
        pleaseWait.modal("hide");
        pleaseWait.removeClass("in");
        $(".modal-backdrop").remove();
        pleaseWait.hide();
    };


    $("body").on("submit", ".js-ajax-upgrade-form", function(){

        $form = $(this);
        $result = $form.find(".form-result")
        submitable = true;

        $form.find(":input.js-required").not(":disabled").each(function(){
            if (!$(this).val()) {
                $(this).addClass("error");
                submitable = false;
            }
        });


        if (submitable) {
            showPleaseWait();
            $.ajax({
                url: $form.attr("action"),
                type: $form.attr("method"),
                dataType: "jsonp",
                data: $form.serialize(),
                error: function() {
                    hidePleaseWait();
                    AjaxHonour.DisplayFormResult($form, "error", ("Oops! An error occured. Please try again later!"));
                    Swal.fire({
                        title: "Error!",
                        text: "Oops! An error occured. Please try again later!",
                        type: "error",
                        confirmButtonText: "Ok"
                    }).then((result) => {

                    });
                },

                success: function(resp) {

                    hidePleaseWait();
                    if (typeof resp.redirect === "string") {
                        window.location.href = resp.redirect;
                    } else if (typeof resp.msg === "string") {
                        var result = resp.result || 0;
                        var reset = resp.reset || 0;

                        if (result === 1){


                            AjaxHonour.DisplayFormResult($form, "success", resp.msg);
                            if (reset) {
                                $form[0].reset();
                            }
                            Swal.fire({
                                title: "Successful!",
                                text: resp.msg,
                                type: "success",
                                confirmButtonText: "Ok"
                            }).then((result) => {
                                if (result.value) {
                                    setTimeout(function () {
                                        //  window.location.reload();
                                    }, resp.delaytime);
                                    if (typeof resp.url === "string") {
                                        window.location.href = resp.url;
                                    }

                                    if (typeof resp.reload === "string") {
                                        window.location.reload();
                                    }
                                } else {
                                }
                            });

                        }

                    } else {
                        AjaxHonour.DisplayFormResult($form, "error", ("Oops! An error occured. Please try again later!"));
                    }

                }
            });
        } else {

            AjaxHonour.DisplayFormResult($form, "error", ("Fill required fields"));
        }

        return false;
    });
}
