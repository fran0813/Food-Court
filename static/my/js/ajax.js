function cliente(){

	$.ajax({url:"/cliente_id",
       
        type: "POST",
        //contentType:"application/json; charset=utf-8",
        //dataType:"json",
        success: function (data, textStatus, jqXHR) {
        	data=JSON.parse(data);
            console.log(data);
            // if (data) {
            //     res='<div class="alert alert-danger">Ya existe una Calificación asociada a este usuario</div>';
            //     $('#result').html(res);
            // }else{
            //     ingresarCalificacion(star);
            //     //console.log('no esta');
            // }
            // //$('#res1').html("<img src='images/app/"+data+".jpg' class='img-responsive' alt=''/>");
                
        },
        error: function (jqXHR, textStatus, errorThrown)
        {
            console.log(jqXHR);
        }

        });
}