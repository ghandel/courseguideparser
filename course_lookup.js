javascript:
/*var patron=document.getElementById('circulation-form-general.PATRON').innerHTML.split('>')[1].split('<')[0];
patron = patron.split(' ')[1] + ',' + patron.split(' ')[0];
location = location.href;
void window.open('http://database.gchandel.com/courselookup.php?patron='+patron+'&location='+location,'Lookup','width=700,height=500,toolbar=0,menubar=0,location=0,status=0,titlebar=0,scrollbars=1,resizable=1,left=0,top=0');
function updateCourse(selection) {
	document.getElementById('CIRCULATION-FORM-OPTIONS-GENERAL.EVENT-DESCRIPTION').value=selection;
}*/
var script = document.createElement('script');
var script_text = document.createTextNode("function updateCourse(selection) {document.getElementById('CIRCULATION-FORM-OPTIONS-GENERAL.EVENT-DESCRIPTION').value=selection;}function openWindow() {var patron=document.getElementById('circulation-form-general.PATRON').innerHTML.split('>')[1].split('<')[0];patron = patron.split(' ')[1] + ',' + patron.split(' ')[0];location = location.href;void window.open('http://database.gchandel.com/courselookup.php?patron='+patron+'&location='+location,'Lookup','width=700,height=500,toolbar=0,menubar=0,location=0,status=0,titlebar=0,scrollbars=1,resizable=1,left=0,top=0');return false;}");
script.appendChild(script_text);
void(document.body.appendChild(script));
openWindow();