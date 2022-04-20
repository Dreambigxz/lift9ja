// $(".loading").css({
//     display: "block",
// });
$(".loading").hide();

function submitForm(btn1, btn2, action, red = 0, loc = "") {
    $("#" + action + "Alert").empty();
    $("#" + btn1 + ",#" + btn2).toggle();
    var formData = "key=" + action + "&" + $("#" + action).serialize();
    $.get("../class.html", formData, function (data) {
        // alert(data);
        response = JSON.parse(data);
        res = response.res;
        msg = response.msg;
        if (res == 1) {
            success(msg, action);
            $("#" + btn1 + ",#" + btn2).toggle();
            if (red == 1) {
                setTimeout(function () {
                    location.href = loc;
                }, 3000);
            }
        } else {
            error(msg, action);
            $("#" + btn1 + ",#" + btn2).toggle();
        }
    });
}


function uploadPOP() {
    // var name = $(".TopaccName").val();
    // var num = $(".TopaccNum").val();
    var phone = $(".Topphone").val();
    var amt = $(".Topamount").val();
    if (phone == "" || amt == "") {
        error("All fields are required", "Top");
    } else if (amt < 10000) {
        error("Minimum top up amount is N10,000", "Top");
    } else {
        $("#topbtn1,#topbtn2").toggle();
        var fd = new FormData();
        var files = $("#file")[0].files;
        // Check file selected or not
        if (files.length > 0) {
            fd.append("file", files[0]);
            $.ajax({
                url: "upload.php",
                type: "post",
                data: fd,
                contentType: false,
                processData: false,
                success: function (response) {
                    response = JSON.parse(response);
                    pid = response.pid;
                    res = response.res;
                    if (res == 1) {
                        var formdata2 =
                            "key=TopUp&pid=" + pid + "&" + $("#TopUpForm").serialize();
                        $.get("../class.html", formdata2, function (data) {
                            if (data == 1) {
                                $("#topbtn1,#topbtn2").toggle();
                                success(
                                    "Your payment details has been successfully sent",
                                    "Top"
                                );
                                setTimeout(function () {
                                    $("#topup").modal("hide");
                                }, 3000);
                            } else {
                                $("#topbtn1,#topbtn2").toggle();
                                error(data, "Top");
                            }
                        });
                    } else {
                        $("#topbtn1,#topbtn2").toggle();
                        error(res, "Top");
                    }
                },
            });
        } else {
            $("#topbtn1,#topbtn2").toggle();
            error("Choose a file to upload", "Top");
        }
    }
}
reload = (className) => {
    var formData = "Class=" + className;
    $.get("reload.html", formData, function (data) {
        $("." + className).html(data);
    });
};

function success(res, pos) {
    //   $("#MySuccessMsg").html(res);
    //   $("#mySuccessModal").modal("show");
    $("#" + pos + "Alert").html(
        '<div style="margin:10px;" class="alert alert-success alert-with-icon alert-dismissible"><button type="button" aria-hidden="true" class="close" data-dismiss="alert" aria-label="Close">&times;</button><span class="text-center">' +
        res +
        "</span></div>"
    );
    //   setTimeout(function () {
    //     $("#" + pos + "Alert").html("");
    //   }, 5000);
}

function error(res, pos) {
    //   $("#MyErrorMsg").html(res);
    //   $("#myErrorModal").modal("show");
    $("#" + pos + "Alert").html(
        '<div style="margin:10px;" class="alert alert-danger alert-with-icon alert-dismissible"><button type="button" aria-hidden="true" class="close" data-dismiss="alert" aria-label="Close">&times;</button><span class="text-center">' +
        res +
        "</span></div>"
    );
    //   setTimeout(function () {
    //     $("#" + pos + "Alert").html("");
    //   }, 5000);
}


function redirect(loc) {
    location.href = loc;
}

function SellShares(method, id, type, text, step = 1) {
    if (step == 1) {
        $("." + id + "hideme").hide();
        $("." + type + id).show();
        // if (type == "reinvestAll") {
        //     $(".proceed" + id).show();
        // } else {
        //     $("." + id + "PaymentMethod").show();
        // }
        $(".proceed" + id).show();
        $("#SharespaymentType").val(type)
        $("#SharesText").val(text)
        $("#SharespaymentMethod").val(method)
    } else if (step == 2) {
        var payment = $("#SharespaymentMethod").val()
        var type = $("#SharespaymentType").val()
        var text = $("#SharesText").val()
        $("." + type + id).attr('disabled', true);
        $(".proceed" + id).attr('disabled', true);
        $(".proceed" + id).html('Loading...');
        var formData = "key=SellShares&type=" + type + "&Shareid=" + id + "&payment=" + payment
        $.get("../class.html", formData, function (data) {
            var data = JSON.parse(data);
            var code = data.code
            var res = data.res
            if (code == 1) {
                success(res, id + "SellShares")
                setTimeout(function () {c
                    reload("DashboardDiv")
                }, 2000)
            } else if (code == 0) {
                error(res, id + "SellShares")
            }
        })
    }


}