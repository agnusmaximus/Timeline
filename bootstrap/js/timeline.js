$("#src_input").bind('keypress', function(e) {
    if(e.keyCode==13){	
	$(".timeline").clear();
	$.post("/extractor",
	       {url : $("#src_input").val()},
	       function (data) {
		   console.log(data);
	       }
	      }
    }
});


		    
