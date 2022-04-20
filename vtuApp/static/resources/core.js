$(function () {
    AjaxHonour.RemoveListItem();
    AjaxHonour.ActivateItem();
    AjaxHonour.CancelListItem();
    AjaxHonour.RefundListItem();

});


var AjaxHonour = {};


/**
 * Add msg to the $resobj and displays it
 * and scrolls to $resobj
 * @param {$ DOM} $form jQuery ref to form
 * @param {string} type
 * @param {string} msg
 */
var __form_result_timer = null;
AjaxHonour.DisplayFormResult = function ($form, type, msg) {
    var $resobj = $form.find(".form-result");
    msg = msg || "";
    type = type || "error";

    if ($resobj.length != 1) {
        return false;
    }


    var $reshtml = "";
    switch (type) {
        case "error":
            $reshtml = "<div class='alert alert-danger' role='alert'> " + msg + "</div>";
            break;

        case "success":
            $reshtml = "<div class='alert alert-success' role='alert'> " + msg + "</div>";
            break;

        case "info":
            $reshtml = "<div class='alert alert-info' role='alert'> " + msg + "</div>";
            break;
    }

    $resobj.html($reshtml).stop(true).fadeIn();

    clearTimeout(__form_result_timer);
    __form_result_timer = setTimeout(function () {
        $resobj.stop(true).fadeOut();
    }, 10000);

    var $parent = $("html, body");
    var top = $resobj.offset().top - 85;
    if ($form.parents(".skeleton-content").length == 1) {
        $parent = $form.parents(".skeleton-content");
        top = $resobj.offset().top - $form.offset().top - 20;
    }

    $parent.animate({
        scrollTop: top + "px"
    });
}


AjaxHonour.ActivateItem = function () {

    $("body").on("click", "a.js-activate-item", function () {
        var item = $(this).parents(".js-list-item");
        var id = $(this).data("id");
        var status = $(this).data("status");
        var url = $(this).data("url");

        var pleaseWait = $("#pleaseWaitDialog");
        var msg ="";
        if(status === "off"){
            msg = "You will be charged again for this action. This is irreversible.";
        }else{

            msg = "This is an irreversible action, consider this for a second.";
        }


        showPleaseWait = function () {
            pleaseWait.modal("show");
        };

        hidePleaseWait = function () {
            pleaseWait.modal("hide");
            pleaseWait.removeClass("in");
            $(".modal-backdrop").remove();
            pleaseWait.hide();
        };

        showPleaseWait();
        Swal.fire({
            title: "Are you  sure?",
            text: msg,
            type: "warning",
            reverseButtons: true,
            showCancelButton: true,
            confirmButtonText: "Proceed"
        }).then((result) => {
            if (result.value) {
                setTimeout(function () {


                    $.ajax({
                        url: url,
                        type: "POST",
                        dataType: "jsonp",
                        data: {
                            action: "statusupdate",
                            status: status,
                            id: id
                        },
                        success: function (resp) {

                            if (typeof resp.redirect === "string") {
                                window.location.href = resp.redirect;
                            } else if (typeof resp.msg === "string") {
                                var result = resp.result || 0;
                                var reset = resp.reset || 0;
                                switch (result) {
                                    case 0: //
                                        hidePleaseWait();
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
                                            } else {
                                            }
                                        });
                                        break;
                                    case 1: //
                                        hidePleaseWait();
                                        Swal.fire({
                                            title: "Successful!",
                                            text: resp.msg,
                                            type: "success",
                                            confirmButtonText: "Ok"
                                        }).then((result) => {
                                            if (result.value) {
                                                setTimeout(function () {
                                                    window.location.reload();
                                                }, resp.delaytime);
                                            }
                                        });
                                        break;
                                    case 2: //
                                        hidePleaseWait();
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
                                            }
                                        });
                                        break;


                                }

                            } else {
                                Swal.fire({
                                    title: "Error!",
                                    text: "Oops! An error occured. Please try again later!",
                                    type: "error",
                                    confirmButtonText: "Ok"
                                }).then((result) => {
                                    if (result.value) {
                                        setTimeout(function () {
                                            //  window.location.reload();
                                        }, resp.delaytime);
                                    } else {
                                    }
                                });
                            }
                            hidePleaseWait();
                        },
                        error: function () {
                            hidePleaseWait();
                            Swal.fire({
                                title: "Error!",
                                text: "Oops! An error occurred. Please try again later!",
                                type: "error",
                                confirmButtonText: "Ok"
                            }).then((result) => {
                                if (result.value) {
                                    setTimeout(function () {
                                        //  window.location.reload();
                                    }, resp.delaytime);
                                } else {
                                }
                            });
                        }
                    });

                });
            } else {

            }

            $("#pleaseWaitDialog").modal("hide");
        });


    });
}


AjaxHonour.RemoveListItem = function () {


    $("body").on("click", "a.js-remove-list-item", function () {
        var item = $(this).parents(".js-list-item");
        var id = $(this).data("id");
        var url = $(this).data("url");

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

        showPleaseWait();

        Swal.fire({
            title: "Are you  sure?",
            text: "This is an irreversible action, consider this for a second.",
            type: "warning",
            reverseButtons: true,
            showCancelButton: true,
            confirmButtonText: "Ok"
        }).then((result) => {
            if (result.value) {
                setTimeout(function () {

                    $.ajax({
                        url: url,
                        type: "POST",
                        dataType: "jsonp",
                        data: {
                            action: "remove",
                            id: id
                        },
                        success: function (resp) {

                            if (typeof resp.redirect === "string") {
                                window.location.href = resp.redirect;
                            } else if (typeof resp.msg === "string") {

                                var result = resp.result || 0;
                                var reset = resp.reset || 0;
                                switch (result) {
                                    case 0: //
                                        hidePleaseWait();
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
                                            } else {
                                            }
                                        });
                                        break;
                                    case 1: //
                                        hidePleaseWait();
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
                                            } else {
                                            }
                                        });
                                        break;

                                    case 2: //
                                        hidePleaseWait();
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
                                            } else {
                                            }
                                        });
                                        break;


                                }

                            } else {
                                Swal.fire({
                                    title: "Error!",
                                    text: "Oops! An error occured. Please try again later!",
                                    type: "error",
                                    confirmButtonText: "Ok"
                                }).then((result) => {
                                    if (result.value) {
                                        setTimeout(function () {
                                            //  window.location.reload();
                                        }, resp.delaytime);
                                    } else {
                                    }
                                });
                            }
                            hidePleaseWait();
                        },
                        error: function () {
                            hidePleaseWait();
                            Swal.fire({
                                title: "Error!",
                                text: "Oops! An error occured. Please try again later!",
                                type: "error",
                                confirmButtonText: "Ok"
                            }).then((result) => {
                                if (result.value) {
                                    setTimeout(function () {
                                        //  window.location.reload();
                                    }, resp.delaytime);
                                } else {
                                }
                            });
                        }
                    });
                    item.fadeOut(500, function () {
                        item.remove();
                    });

                });
            } else {

            }

            $("#pleaseWaitDialog").modal("hide");
        });


    });
}

AjaxHonour.CancelListItem = function () {


    $("body").on("click", "a.js-cancel-list-item", function () {

        var id = $(this).data("id");
        var url = $(this).data("url");

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

        showPleaseWait();

        Swal.fire({
            title: "Are you  sure?",
            text: "This is an irreversible action, kindly consider this for a second.",
            type: "warning",
            reverseButtons: true,
            showCancelButton: true,
            confirmButtonText: "Proceed"
        }).then((result) => {
            if (result.value) {
                setTimeout(function () {

                    $.ajax({
                        url: url,
                        type: "POST",
                        dataType: "jsonp",
                        data: {
                            action: "cancel",
                            id: id
                        },
                        success: function (resp) {

                            if (typeof resp.redirect === "string") {
                                window.location.href = resp.redirect;
                            } else if (typeof resp.msg === "string") {

                                var result = resp.result || 0;
                                var reset = resp.reset || 0;
                                switch (result) {

                                    case 0: //
                                        hidePleaseWait();
                                        Swal.fire({
                                            title: "Error!",
                                            text: resp.msg,
                                            type: "error",
                                            confirmButtonText: "Ok"
                                        }).then((result) => {
                                            if (result.value) {
                                                setTimeout(function () {
                                                    window.location.reload();
                                                }, resp.delaytime);
                                            } else {
                                            }
                                        });
                                        break;
                                    case 1: //
                                        hidePleaseWait();
                                        Swal.fire({
                                            title: "Successful!",
                                            text: resp.msg,
                                            type: "success",
                                            confirmButtonText: "Ok"
                                        }).then((result) => {
                                            if (result.value) {
                                                setTimeout(function () {
                                                    window.location.reload();
                                                }, resp.delaytime);
                                            } else {
                                            }
                                        });
                                        break;

                                    case 2: //
                                        hidePleaseWait();
                                        Swal.fire({
                                            title: "Successful!",
                                            text: resp.msg,
                                            type: "success",
                                            confirmButtonText: "Ok"
                                        }).then((result) => {
                                            if (result.value) {
                                                setTimeout(function () {
                                                    window.location.reload();
                                                }, resp.delaytime);
                                            } else {
                                            }
                                        });
                                        break;


                                }

                            } else {
                                Swal.fire({
                                    title: "Error!",
                                    text: "Oops! An error occured. Please try again later!",
                                    type: "error",
                                    confirmButtonText: "Ok"
                                }).then((result) => {
                                    if (result.value) {
                                        setTimeout(function () {
                                            window.location.reload();
                                        }, resp.delaytime);
                                    } else {
                                    }
                                });
                            }
                            hidePleaseWait();
                        },
                        error: function () {
                            hidePleaseWait();
                            Swal.fire({
                                title: "Error!",
                                text: "Oops! An error occured. Please try again later!",
                                type: "error",
                                confirmButtonText: "Ok"
                            }).then((result) => {
                                if (result.value) {
                                    setTimeout(function () {
                                        window.location.reload();
                                    }, resp.delaytime);
                                } else {
                                }
                            });
                        }
                    });


                });
            } else {

            }

            $("#pleaseWaitDialog").modal("hide");
        });


    });
}

AjaxHonour.RefundListItem = function () {


    $("body").on("click", "a.js-refund-list-item", function () {

        var id = $(this).data("id");
        var url = $(this).data("url");

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

        showPleaseWait();

        Swal.fire({
            title: "Are you  sure?",
            text: "This is an irreversible action, consider this for a second.",
            type: "warning",
            reverseButtons: true,
            showCancelButton: true,
            confirmButtonText: "Proceed"
        }).then((result) => {
            if (result.value) {
                setTimeout(function () {

                    $.ajax({
                        url: url,
                        type: "POST",
                        dataType: "jsonp",
                        data: {
                            action: "refund",
                            id: id
                        },
                        success: function (resp) {

                            if (typeof resp.redirect === "string") {
                                window.location.href = resp.redirect;
                            } else if (typeof resp.msg === "string") {

                                var result = resp.result || 0;
                                var reset = resp.reset || 0;
                                switch (result) {

                                    case 0: //
                                        hidePleaseWait();
                                        Swal.fire({
                                            title: "Error!",
                                            text: resp.msg,
                                            type: "error",
                                            confirmButtonText: "Ok"
                                        }).then((result) => {
                                            if (result.value) {
                                                setTimeout(function () {
                                                    window.location.reload();
                                                }, resp.delaytime);
                                            } else {
                                            }
                                        });
                                        break;
                                    case 1: //
                                        hidePleaseWait();
                                        Swal.fire({
                                            title: "Successful!",
                                            text: resp.msg,
                                            type: "success",
                                            confirmButtonText: "Ok"
                                        }).then((result) => {
                                            if (result.value) {
                                                setTimeout(function () {
                                                    window.location.reload();
                                                }, resp.delaytime);
                                            } else {
                                            }
                                        });
                                        break;

                                    case 2: //
                                        hidePleaseWait();
                                        Swal.fire({
                                            title: "Successful!",
                                            text: resp.msg,
                                            type: "success",
                                            confirmButtonText: "Ok"
                                        }).then((result) => {
                                            if (result.value) {
                                                setTimeout(function () {
                                                    window.location.reload();
                                                }, resp.delaytime);
                                            } else {
                                            }
                                        });
                                        break;


                                }

                            } else {
                                Swal.fire({
                                    title: "Error!",
                                    text: "Oops! An error occured. Please try again later!",
                                    type: "error",
                                    confirmButtonText: "Ok"
                                }).then((result) => {
                                    if (result.value) {
                                        setTimeout(function () {
                                            window.location.reload();
                                        }, resp.delaytime);
                                    } else {
                                    }
                                });
                            }
                            hidePleaseWait();
                        },
                        error: function () {
                            hidePleaseWait();
                            Swal.fire({
                                title: "Error!",
                                text: "Oops! An error occured. Please try again later!",
                                type: "error",
                                confirmButtonText: "Ok"
                            }).then((result) => {
                                if (result.value) {
                                    setTimeout(function () {
                                        window.location.reload();
                                    }, resp.delaytime);
                                } else {
                                }
                            });
                        }
                    });


                });
            } else {

            }

            $("#pleaseWaitDialog").modal("hide");
        });


    });
}

/**
 * Profile
 */
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
                $alert.find(".js-resend-result").html(__("Oops! An error occured. Please try again later!"));
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


/* Functions */

/**
 * Validate Email
 */
function isValidEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
}

/**
 * Get scrollbar width
 */
function scrollbarWidth() {
    var scrollDiv = document.createElement("div");
    scrollDiv.className = "scrollbar-measure";
    document.body.appendChild(scrollDiv);
    var w = scrollDiv.offsetWidth - scrollDiv.clientWidth;
    document.body.removeChild(scrollDiv);

    return w;
}


/**
 * Validate URL
 */
function isValidUrl(url) {
    return /^(https?|s?ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&"\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i.test(url);
}


/**
 * Get the position of the caret in the contenteditable element
 * @param  {DOM}  DOM of the input element
 * @return {obj}  start and end position of the caret position (selection)
 */
function getCaretPosition(element) {
    var start = 0;
    var end = 0;
    var doc = element.ownerDocument || element.document;
    var win = doc.defaultView || doc.parentWindow;
    var sel;

    if (typeof win.getSelection != "undefined") {
        sel = win.getSelection();
        if (sel.rangeCount > 0) {
            var range = win.getSelection().getRangeAt(0);
            var preCaretRange = range.cloneRange();
            preCaretRange.selectNodeContents(element);
            preCaretRange.setEnd(range.startContainer, range.startOffset);
            start = preCaretRange.toString().length;
            preCaretRange.setEnd(range.endContainer, range.endOffset);
            end = preCaretRange.toString().length;
        }
    } else if ((sel = doc.selection) && sel.type != "Control") {
        var textRange = sel.createRange();
        var preCaretTextRange = doc.body.createTextRange();
        preCaretTextRange.moveToElementText(element);
        preCaretTextRange.setEndPoint("EndToStart", textRange);
        start = preCaretTextRange.text.length;
        preCaretTextRange.setEndPoint("EndToEnd", textRange);
        end = preCaretTextRange.text.length;
    }
    return {start: start, end: end};
}