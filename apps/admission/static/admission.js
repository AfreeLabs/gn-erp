jQuery(document).ready(function(){

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-registration .modal-content").html("");
        $("#modal-registration").modal("show");
      },
      success: function (data) {
        $("#modal-registration .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          console.log("deleted")
          $("#modal-registration").modal("hide");
        }
        else {
          $("#modal-registration .modal-content").html(data.html_form);
        }
      }
    });
    return false;
    
  };

  $(".btn-delete").on("click", loadForm);
  $(".js-delete-registration-form").on("submit", saveForm);

  // Disabling Admission process form submit button until the first select box are filled
  // $("#id_pass_admission_test", "#id_pass_bac", 
  //   "#id_pass_medical_test", "#id_approved_by_commitee").on

  var checked = $("#id_pass_admission_test");
  checked.on('click', function(){
        alert("cool")
        // var empty = false;
        // if (checked.is('checked')){
        //   empty = true
        //   alert("true");
        // }

    
  }
  });
        if (empty){
      $('#new-process-submit-button').attr('disabled', false);
    }else{
      $('#new-process-submit-button').attr('disabled', true);

  //  checked.each(function(element){
  //   if (element.is('checked')){
  //   $('#new-process-submit-button').show();
  //   }else{
  //    $('#new-process-submit-button').attr('disabled', 'disabled');
  // }

  //  });

  


  
});


