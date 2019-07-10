function checkInput () {
    var event = window.event || event.which;
    if (event.keyCode == 13) {
        event.preventDefault()
        addLine(document.getElementById("textinput").value);
        document.getElementById("textinput").value = "(Agent:1765678) > ";
    }

    document.getElementById("textinput").style.height = (document.getElementById("textinput").scrollHeight) + "px";
}

function addLine (line) {
    var textNode = document.createTextNode(line);
    var lineBreak = document.createElement("br");
    document.getElementById("consoletext").appendChild(textNode);
    document.getElementById("consoletext").appendChild(lineBreak);
}
