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
	var wynik="";
	wynik+="Nazwa: <input type='text' name='nazwa' value='" + actual.attr('id') + "'><br/>";
	pos = actual.position();
	wynik+="Position <input type='number' name='posx' value='" + pos.left + "'> ";
	wynik+="<input type='number' name='posy' value='" + pos.top + "'></br>";

	wynik+="Typ: <select id='object_type' name='type'>";
	wynik+="<option value='1' ";
		if(actual.attr("klasa")==1)
			wynik+="selected=1";
	wynik+=">Input</option>";
	wynik+="<option value='0' ";
		if(actual.attr("klasa")==0)
			wynik+="selected=1";
	wynik+=">Tekst</option>";
	wynik+="</select><br/>";
	

	wynik+="Zawartosc: <input id='object_content' type='text' value=''><br/>";


	$("#edit_field").html(wynik);

	var klasa = actual.attr('klasa');
	if(klasa == '0')
	{
		var wew = get_inner(actual)
		$('#object_content')[0].value = wew.html();
	}

	$('#object_content').change(function(e){
		var wew = get_inner(actual);
		wew.html($('#object_content')[0].value);
	});

	$('#object_type').change(function(e){
		var klasa = $('#object_type')[0].value;
		actual.attr('klasa',klasa);
		var wew = get_inner(actual);
		switch(klasa)
		{
			case '0':
				wew.html($('#object_content')[0].value);
				break;
			case '1':
				wew.html($("<input type='text'>"));
				break;
			default:
				alert("cc");
		};
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
		$(d).attr('klasa', 0);
		$(d).addClass('ui-widget-content').
			addClass('content').
			appendTo($(actual)).
			click(function(e) { select($(this),e);});
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
		dump("main",0);
		$("#export_field").html(wynik);
	});



	setter();
});


