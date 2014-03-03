var actual = $('#main');
var wynik = "";
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
	var wynik="";
	wynik+="Nazwa: <input type='text' name='nazwa' value='" + actual.attr('id') + "'><br/>";
	pos = actual.position();
	wynik+="Position <input type='number' name='posx' value='" + pos.left + "'> ";
	wynik+="<input type='number' name='posy' value='" + pos.top + "'></br>";
	wynik+="Typ: <select id='container_type' name='type'>";
	wynik+="<option value='1' ";
		if(actual.is("input"))
			wynik+="selected=1";
	wynik+=">Input</option>";
	wynik+="<option value='0' ";
		if(actual.is("div"))
			wynik+="selected=1";
	wynik+=">Div</option>";

	$("#edit_field").html(wynik);

	$('#container_type').change(function(e){
		display="";
		for(a in e)
		{
			display+=a+"\n";
		};
		alert(display);
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
};
function dump(obiekt,ind)
{	
	var indent=ind;
	var children = $("#"+obiekt).children(".content");
	var len = children.size()
	for(i=0;i<ind;i++)
		wynik += "_";
	wynik += "&ltdiv id = '";
	id = obiekt;
	wynik += id + "'&gt<br/>";
	var i=0;
	for(; i < len; i++)
	{
		dump(children[i]["id"],indent+1);
	};
	for(i=0;i<ind;i++)
		wynik += "_";
	wynik += "&lt/div&gt<br/>";
};
$(function() {
	$("#add").click(function() {
		i = 1 + Math.floor(Math.random() * 100);
		d = document.createElement('div');
		$(d).attr('id','zew'+i);
		$(d).addClass('ui-widget-content').
			addClass('content').
			appendTo($(actual)).
			click(function(e) { select($(this),e);}).
			html("Nowy element");
		setter();

	});
	$("#del").click(function() {
		if($(actual).attr('id') != 'editable')
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
		dump("main",0);
		$("#export_field").html(wynik);
	});



	setter();
});


