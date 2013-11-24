function create_timeline(data) {
    console.log(data);
    for (var i = 0; i < data.length; i++) {
	var new_element = document.createElement("li");
	var desc = document.createElement("p");
	for (var j = 0; j < data[i][1].length; j++) {
	    if (j != 0)
		desc.innerHTML += "<hr/>"
	    desc.innerHTML += data[i][1][j];
	}
	var date = document.createElement("span");
	date.innerHTML = data[i][0];

	new_element.appendChild(desc);
	new_element.appendChild(date);
	$(".timeline").append($(new_element).hide().fadeIn("slow"));
    }
}

$("#src_input").bind('keypress', function(e) {
    if(e.keyCode==13){
	$(".timeline").empty();
	$.post("/extractor",
	       {url : $("#src_input").val()},
	       function (data) {
		   $("#header_rule").empty().append("<hr/>");
		   data = JSON.parse(data);
		   create_timeline(data);
	       }
	      );
    }
});
