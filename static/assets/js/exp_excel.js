

function decide() //This function decides the browser and calls the respective function for porting this to excel
{ 
	if (navigator.userAgent.search("MSIE") >= 0)
	 { 
	 	write_to_excel();
	 }
	 
	else if (navigator.userAgent.search("Chrome") >= 0) 
	{ 
		exportchrome(); 
	} 
} 





function exportchrome() { 
var dt = new Date();
 var day = dt.getDate();
  var month = dt.getMonth() + 1;
   var year = dt.getFullYear();
    var hour = dt.getHours(); 
    var mins = dt.getMinutes();
     var postfix = day + "." + month + "." + year + "_" + hour + "." + mins;
      //creating a temporary HTML link element (they support setting file names) 
      var a = document.createElement('a'); 
      //getting data from our div that contains the HTML table
      var data_type = 'data:application/vnd.ms-excel'; 
      var table_div = document.getElementById('Table_div'); 
      var table_html = table_div.outerHTML.replace(/ /g, '%20'); 
      a.href = data_type + ', ' + table_html;
      //setting the file name 
      a.download = 'exported_table_' + postfix + '.xls';
       //triggering the function 
      		a.click(); 
       //just in case, prevent default behaviour 
       event.preventDefault(); 
} 




//The bootstrap file above is required for the UI to show up
//Function to Export the table into excel in IE  
function write_to_excel()  
{ 
 	var i, j, str, 
 	myTable = document.getElementById('tab'), 
 	rowCount = myTable.rows.length, 
 	excel = new ActiveXObject('Excel.Application'); // Activates Excel 
 			excel.Wbrkbooks.Add(); // Opens a new Workbook 
 			excel.Application.Visible = true; // Shows Excel on the screen 
 			for (i = 0; i < rowCount; i++) 
 			{
 				 for (j = 0; j < myTable.rows[i].cells.length; j++) 
				{
 
 				str = myTable.rows[i].cells[j].innerText; 
 				excel.ActiveSheet.Cells(i + 1, j + 1).Value = str; // Writes to the sheet 
 
				}
  			}
  			return; 
}
 var data = ""; 

