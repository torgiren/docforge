var actual = $('#main');
var wynik = "";
function get_class(obj)
{
	return $('#object_type')[0].value;
}
function get_inner(obj)
{
	return $(obj.children('span')[0]);
};
function setter()
{
	$(".content").draggable({distance: 20, containment: 'parent'});
	$(".content").resizable({containment: 'parent'});
	$(".editable").click(function(e) {
		select($(this),e);
	});
//	$("#editable").mouseleave(function(e) {
//		leave($(this),e);
//	});
};
function update_edit_field()
{
	pos = actual.position();
	var wynik="";
	wynik+="Nazwa: <input type='text' id='object_nazwa' value='" + actual.attr('id') + "'><br/>";
	wynik+="Size: <input type='text' id='object_width' style='width: 50px;' value='" + actual.width() +"'>";
	wynik+="<input type='number' id='object_height' style='width: 50px;' value='" + actual.height() + "'><br/>";
	wynik+="Position <input type='number' id='object_posx' style='width: 50px;' value='" + pos.left + "'> ";
	wynik+="<input type='number' id='object_posy' style='width: 50px;' value='" + pos.top + "'></br>";

	wynik+="Zawartosc: <br/><textarea id='object_content' type='text' cols=40 rows=5 value=''></textarea><br/>";
	wynik+="<button id='object_save'>Zapis</button><br/>";

	pola = $('#main').html().match(/{{[a-zA-Z0-9]*}}/g);
	if(pola)
	{
		wynik+="<ul>";
		for(i=0; i < pola.length; i++)
		{
			var nazwa = pola[i].slice(2,-2);
			wynik += "<hr>";
			wynik += nazwa + ":<br/>";
			wynik += "<form id='form_" + i + "' class='template_forms'>";
			wynik += "<input type='hidden' name='nazwa' value='" + nazwa + "'/>";
			wynik += "<select name='typ'>"
			wynik += "<option>Input</option>";
			wynik += "<option>Checkbox</option>";
			wynik += "</select>";
			wynik += "</form>";
		};
		wynik+="</ul>";
	};


	$("#edit_field").html(wynik);

	var wew = get_inner(actual)
	$('#object_content')[0].value = wew.html();

	$('#object_save').click(function(e){
		var wew = get_inner(actual);
		var width = $('#object_width')[0].value;
		var height = $('#object_height')[0].value;
		var posx = Number($('#object_posx')[0].value);
		var posy = Number($('#object_posy')[0].value);
		var id = $('#object_nazwa')[0].value;
		wew.html($('#object_content')[0].value);
		actual.attr('id', id);

		actual.css({'position': "absolute", "top": posy, "left": posx});
		actual.width(width);
		actual.height(height);

				wew.html($('#object_content')[0].value);
	});
	
};
function select(obj,e)
{
	leave(actual,e);
	obj.css('color', 'red');
	obj.css('border', '2px solid blue');
	actual = obj;
	$('#akt').html(actual.attr('id'));
	e.stopImmediatePropagation();
	update_edit_field();
};
function leave(obj,e)
{
	obj.css('color', 'black');
	obj.css('border', '1px black solid');
	e.stopImmediatePropagation();
		obj.children('span').children('input').css('width', obj.width() - 4 );
};
function dump(obiekt,ind)
{	
	var indent=ind;
	var children = $("#"+obiekt).children(".content");
	var len = children.size()
	var obj = $('#'+obiekt);
//	for(i=0;i<ind;i++)
//		wynik += " ";
	wynik += "&ltdiv id='";
	wynik += obiekt + "' ";
	pos = obj.position();
	wynik += "left='" + pos.left + "' ";
	wynik += "top='" + pos.top + "' ";
	wynik += "width='" + obj.width() + "' ";
	wynik += "heigth='" + obj.height() + "' ";
	wynik += "&gt<br/>";
	wynik += obj.children('span')[0].innerHTML + "<br/>";
	var i=0;
	for(; i < len; i++)
	{
		dump(children[i]["id"],indent+1);
	};
//	for(i=0;i<ind;i++)
//		wynik += " ";
	wynik += "&lt/div&gt<br/>";
};
$(function() {
	$("#add").click(function() {
		i = 1 + Math.floor(Math.random() * 100);
		d = document.createElement('div');
		$(d).attr('id','zew'+i);
		//$(d).addClass('ui-widget-content').
		$(d).addClass('content').
			appendTo($(actual)).
			click(function(e) { select($(this),e);}).
			css('border', '1px black solid').
			css('color', 'black');
//			html("Nowy element");
		e = document.createElement('span');
		$(e).attr('id','content'+i);
		$(e).appendTo($(d)).html('Nowy element2');
		setter();

	});
	$("#del").click(function() {
		if($(actual).attr('id') != 'main')
		{
			actual.remove();
		};
	});
	$(".editable").resizable({resize: function(event, ui) {
		$(this).css('width','1024px');
		}
	});
	$("#export").click(function() {
		wynik = "";
//		wynik += $('#nazwa')[0].value + "<br/>";
		dump("main",0);
		forms = $('.template_forms');;
		forms2 = Array();
		for(i=0; i<forms.length; i++)
		{
			var obj = $('#'+forms[i].id);
			forms2.push(obj.serialize());
//			wynik += obj.serialize() + "<br/>";
		};
		$.ajax({
			type: "POST",
			url: "/api/zapisz_template",
			data: {
				nazwa: $('#nazwa')[0].value,
				template: wynik,
				pola: forms2
			},
			success: function(msg) {
				console.log("success");
				console.log(msg);
			},
			complete: function(r) {
				console.log("complete");
				console.log(r);
			},
			error: function(error) {
				console.log("error");
				console.log(error);
			}		
		})
		$("#export_field").html(wynik);
		wynik = "";
	});



	setter();
});


