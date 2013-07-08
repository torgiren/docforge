var iter=0;
function deleteRow(param)
{
    param.parentNode.parentNode.parentNode.parentNode.deleteRow(param.parentNode.parentNode.sectionRowIndex);
}
function addRow()
{
    var tab = document.getElementById('tabela');
    var row = tab.insertRow(-1);
    var ceilLeft = row.insertCell(0)
    var textNode = document.createTextNode(iter)
    ceilLeft.appendChild(textNode)

    var cellRight= row.insertCell(1);
    var el = document.createElement('input');
    el.type = 'text';
    el.name = 'nazwa_' + iter;
    cellRight.appendChild(el);

    var cellRightSel = row.insertCell(2);
    var sel = document.createElement('select');
    sel.name = 'typ_' + iter;
    $.ajax({
        url:"http://localhost:6543/ajax/typy",
        success: function(data) 
        {
            for(var i in data)
            {
                sel.options[i] = new Option(data[i][1], data[i][0])
            }
        }
    });
    cellRightSel.appendChild(sel);

    var cellDel = row.insertCell(3);
    var del = document.createElement('input');
    del.type = 'button';
    del.value = 'Usuń';
    del.name = 'del_'+iter
    del.setAttribute('onclick', 'deleteRow(this)')
    cellDel.appendChild(del);
    iter++;
};
