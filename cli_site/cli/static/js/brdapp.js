function sendCommand () {
    var event = window.event || event.which;
    if (event.keyCode == 13) {
	event.preventDefault()
	    
	// send post request
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
		//document.getElementById("console").innerHTML = this.responseText
	    }
	};
	// make this go to cli.html
	xhttp.open("POST", document.getElementById("textinput").value, true);
	xhttp.send()
        
	addLine(document.getElementById("textinput").value);
	document.getElementById("textinput").value = "(Agent:1765678) > ";
    }
    document.getElementById("textinput").style.height = (document.getElementById("textinput").scrollHeight) + "px";
}

// Add a line to the terminal
function addLine (line) {
    var textNode = document.createTextNode(line);
    var lineBreak = document.createElement("br");
    document.getElementById("consoletext").appendChild(textNode);
    document.getElementById("consoletext").appendChild(lineBreak);
}
