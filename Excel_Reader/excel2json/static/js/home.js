$(document).ready(function() {
  
    $('#upload').click(function(){
        var file = $('#excel')[0].files[0]
        if (file) {
            const filedata = new FormData()
            filedata.append('excel', file)
            let target = encodeURI(window.location.href + 'upload/');
            $.ajax({
                url: target,
                type: "POST",
                processData: false,
                contentType : false,
                data : filedata,
            })
            .done(function(data){
                $('#result').html(data.data)
            })
        }
    })

});